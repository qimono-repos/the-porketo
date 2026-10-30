# VPS deployment notes

For the first boot:

1. Install JDK 21 and Git.
2. Pull the repository and enter `no-sql/kotlin-service`.
3. Configure `MONGODB_URI`, `MONGODB_DATABASE=porketo`, and `PORT=8080` in the service environment.
4. Run `gradle run` or the Gradle wrapper once added.
5. Verify `/health` and `/ready` locally.
6. Then place the service behind the existing HTTPS reverse proxy and manage it with systemd.

Never put credentials in Git, shell history, screenshots, or chat. Restrict Atlas Network Access to the VPS's outbound public IP. Do not use `0.0.0.0/0` for Atlas access. Restrict inbound VPS firewall rules to the reverse proxy's public ports.
