package com.qimono.porketo

import io.ktor.client.request.get
import io.ktor.client.statement.bodyAsText
import io.ktor.server.testing.testApplication
import kotlin.test.Test
import kotlin.test.assertContains

class ApplicationTest {
    @Test
    fun healthEndpointWorksWithoutDatabase() = testApplication {
        application { porketoModule(database = null, databaseName = "porketo") }
        val response = client.get("/health")
        assertContains(response.bodyAsText(), "\"status\":\"ok\"")
    }

    @Test
    fun readinessReportsMissingDatabaseConfiguration() = testApplication {
        application { porketoModule(database = null, databaseName = "porketo") }
        val response = client.get("/ready")
        assertContains(response.bodyAsText(), "MONGODB_URI is not configured")
    }
}
