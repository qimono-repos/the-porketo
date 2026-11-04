# VPS deployment notes

For the first boot:

1. Pull this repository and the canonical dotfiles checkout on the VPS.
2. Run `sudo bash dotfiles/vps-ubuntu/scripts/deploy-porketo-api.sh`.
3. The script builds the Gradle distribution, creates the `porketo` service
   account, installs `porketo-api.service`, and binds to `127.0.0.1:8080`.
4. Verify with `curl http://127.0.0.1:8080/health` and inspect logs using
   `journalctl -u porketo-api`.
5. Set `MONGODB_URI` in `/etc/porketo-api/porketo.env` using `sudoedit`, then
   restart with `sudo systemctl restart porketo-api` and check `/ready`.
6. Configure the HTTPS reverse proxy only after the hostname, authentication,
   and exposure policy have been selected.

The systemd unit runs as the unprivileged `porketo` account with a 768 MiB
memory ceiling, a 75% CPU quota, and a 64-task limit. Service logs go to
journald. For rollback after a successful later deployment, run:

```bash
sudo bash dotfiles/vps-ubuntu/scripts/deploy-porketo-api.sh --rollback
```

Never put credentials in Git, shell history, screenshots, or chat. Restrict
Atlas Network Access to the VPS's outbound public IP. Do not use `0.0.0.0/0`.
The deployed API is loopback-only; no direct public port is required.
