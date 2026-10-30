package com.qimono.porketo

import com.mongodb.kotlin.client.coroutine.MongoClient
import io.ktor.http.ContentType
import io.ktor.server.application.Application
import io.ktor.server.engine.embeddedServer
import io.ktor.server.netty.Netty
import io.ktor.server.response.respondText
import io.ktor.server.routing.get
import io.ktor.server.routing.routing
import kotlinx.coroutines.runBlocking
import org.bson.Document

fun main() {
    val port = System.getenv("PORT")?.toIntOrNull() ?: 8080
    val mongoUri = System.getenv("MONGODB_URI")
    val databaseName = System.getenv("MONGODB_DATABASE") ?: "porketo"
    val mongoClient = mongoUri?.takeIf { it.isNotBlank() }?.let(MongoClient::create)
    val database = mongoClient?.getDatabase(databaseName)

    Runtime.getRuntime().addShutdownHook(Thread { mongoClient?.close() })

    embeddedServer(Netty, host = "0.0.0.0", port = port) {
        porketoModule(database, databaseName)
    }.start(wait = true)
}

fun Application.porketoModule(
    database: com.mongodb.kotlin.client.coroutine.MongoDatabase?,
    databaseName: String
) {
    routing {
        get("/") {
            call.respondText(
                """{"service":"the-porketo-api","status":"running","database":"$databaseName"}""",
                ContentType.Application.Json
            )
        }
        get("/health") {
            call.respondText("""{"service":"the-porketo-api","status":"ok"}""", ContentType.Application.Json)
        }
        get("/ready") {
            if (database == null) {
                call.respondText("""{"service":"the-porketo-api","status":"not_ready","detail":"MONGODB_URI is not configured"}""", ContentType.Application.Json)
                return@get
            }
            try {
                runBlocking { database.runCommand(Document("ping", 1)) }
                call.respondText("""{"service":"the-porketo-api","status":"ready","database":"$databaseName"}""", ContentType.Application.Json)
            } catch (exception: Exception) {
                call.respondText("""{"service":"the-porketo-api","status":"not_ready","detail":"MongoDB ping failed"}""", ContentType.Application.Json)
            }
        }
    }
}
