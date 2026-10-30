# Porketo Kotlin API

A small Ktor HTTP service for the Porketo MongoDB Atlas project.

## Stack

- Kotlin/JVM
- Ktor server with Netty
- MongoDB Kotlin Coroutine Driver
- Kotlin serialization
- Gradle Kotlin DSL

The service deliberately starts as a thin connectivity/API slice. It does not import or mutate trading-book data yet. The DDD rules in ../DDD.md remain authoritative: immutable events, lot-level aggregate boundaries, and derived values computed from source facts.

## Requirements

- JDK 21
- MongoDB Atlas database user credentials
- Atlas network access for the VPS public egress IP

## Configuration

Set environment variables on the VPS:

```bash
export MONGODB_URI='mongodb+srv://<username>:<url-encoded-password>@<cluster-host>/?retryWrites=true&w=majority&appName=the-porketo-nosql'
export MONGODB_DATABASE='porketo'
export PORT='8080'
```

Do not commit the URI, passwords, or a real `.env` file.

The Atlas user shown in the connection modal is a database user. The password is the one created during Atlas security setup, not your GitHub or Atlas account password. URL-encode reserved characters in the password.

## Run

```bash
./gradlew run
```

Health check:

```bash
curl http://localhost:8080/health
```

MongoDB readiness check:

```bash
curl http://localhost:8080/ready
```

The readiness route performs a lightweight MongoDB ping and reports whether the application can reach the configured database.

## Initial routes

- `GET /health` process liveness, no database dependency
- `GET /ready` MongoDB connectivity check
- `GET /` service metadata

## Deployment notes

For first boot, run on localhost or behind an existing reverse proxy. Do not expose port 8080 directly to the public internet before configuring HTTPS and an application authentication strategy. Add the VPS public egress IP to Atlas Network Access; do not use `0.0.0.0/0`.

The app binds to `0.0.0.0` inside the VPS so a reverse proxy/container can reach it. Configure firewall rules to expose only the reverse proxy's public ports.
