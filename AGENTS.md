# AGENTS.md — Autoscript Tunneling v7

## Project Overview

This repository is a Bash-based VPN tunneling auto-installer ("Autoscript Tunneling v7") targeting Ubuntu/Debian/Kali Linux servers. It installs and configures Xray (VLESS, VMESS, Trojan, Shadowsocks), SSH tunneling, OpenVPN, SlowDNS, UDP-Custom, Fail2ban, and a Telegram bot panel.

**Primary language:** Bash  
**Target OS:** Ubuntu 20.04/22.04/24.04 LTS, Debian 10/11/12, Kali Rolling  
**Architecture:** x86_64 only  
**Minimum requirements:** 512 MB RAM, 10 GB SSD, 1 vCPU

---

## Repository Structure

```
/
├── install.sh          # Main installer — full VPN stack setup
├── install.sh.bak      # Backup of previous installer version
├── update.sh           # Updates menu binaries from GitHub
├── botrs.sh            # Installs cybervpn Telegram bot (Python/Telethon)
├── kyt.sh              # Installs kyt Telegram bot panel
├── gotop.sh            # Installs gotop monitor + 1 GB swap
├── udp-custom.sh       # Installs UDP-Custom service
├── limit/              # Binary assets, configs, zips deployed by installer
│   ├── menu/           # Menu shell scripts deployed to /usr/local/sbin/
│   ├── menu.zip        # Packed menu archive (password-protected)
│   ├── xray.conf       # Xray base config
│   ├── nginx.conf      # Nginx reverse-proxy config
│   ├── haproxy.cfg     # HAProxy config
│   └── ...             # Other service configs and binaries
└── README.md           # User-facing install instructions (Indonesian)
```

---

## Key Conventions

### Shell Scripts
- All scripts use `#!/bin/bash` shebang.
- ANSI color variables are defined at the top of each script (Green, YELLOW, RED, LIME, NC, etc.).
- `print_install` / `print_success` helper functions are used for status output.
- `export DEBIAN_FRONTEND=noninteractive` is set before any `apt` calls.
- Scripts self-delete after completion (`rm -rf /root/scriptname.sh`).
- Systemd unit files are written inline via heredoc (`cat > /etc/systemd/system/...`).

### Secrets / Credentials
- Bot tokens and Telegram IDs are written to `var.txt` files at runtime via `read` prompts.
- **Never hardcode production bot tokens or API keys in committed scripts.**
- The `install.sh.bak` file contains a hardcoded bot token — this must not be replicated.

### Asset Distribution
- Binary assets and configs are stored in `limit/` and fetched at install time via `wget`.
- Password-protected zips use `7z x` for extraction.
- Menu binaries are deployed to `/usr/local/sbin/` and made executable.

### Service Management
- All long-running services use systemd units with `Restart=always`.
- Services are started, enabled, and restarted in sequence after unit file creation.

---

## What Agents Should and Should Not Do

### Do
- Keep all scripts POSIX-compatible where possible; use Bash-specific features only when necessary.
- Preserve the existing color/output style when modifying user-facing scripts.
- Test architecture and OS detection logic before modifying it — the installer exits early on unsupported platforms.
- When adding new service installers, follow the pattern in `kyt.sh`: venv setup → config write → systemd unit → start/enable/restart → cleanup.
- Keep `limit/` assets in sync with what `install.sh` expects to download.

### Do Not
- Do not commit real bot tokens, Telegram IDs, or API keys.
- Do not remove the `export DEBIAN_FRONTEND=noninteractive` guard from any script that calls `apt`.
- Do not change port assignments without updating both the Xray config and the README port table.
- Do not add ARM/i386 support without testing — the installer explicitly rejects non-x86_64.
- Do not modify `menu.zip` contents without re-packing with the correct password.

---

## Common Tasks

### Adding a new protocol or service
1. Add the systemd unit template to the relevant installer script.
2. Add the port to the README port table.
3. Add the binary/config to `limit/` if needed.
4. Update `install.sh` to call the new setup function.

### Updating menu binaries
- Repack `limit/menu/` into `menu.zip` with the existing password.
- Push to the `main` branch — `update.sh` fetches from `main`.

### Modifying the Telegram bot
- `botrs.sh` installs the `cybervpn` Python package from `limit/cybervpn.zip`.
- `kyt.sh` installs the `kyt` Python package from `limit/kyt.zip`.
- Bot credentials are stored in `var.txt` inside the respective package directory.

---

## Testing

There is no automated test suite. Manual verification steps:
1. Spin up a fresh Ubuntu 22.04 or Debian 12 VM (x86_64, ≥1 GB RAM).
2. Run `install.sh` end-to-end and confirm the menu opens.
3. Verify each protocol port is reachable from a client.
4. Run `update.sh` and confirm menu binaries are refreshed.

---

## Known Issues / Debt

- `install.sh.bak` contains a hardcoded Telegram bot token — should be removed or sanitized.
- No input validation on domain/IP prompts in `kyt.sh` and `botrs.sh`.
- `udp-custom.sh` downloads binaries from Google Drive with cookie-based auth — fragile.
- `update.sh` calls `netfilter-persistent` unconditionally before any check that it is installed.
- Color variable `RED` in `install.sh` is missing the leading `\` (`RED='033[0;31m'` → should be `RED='\033[0;31m'`).

## Fixed Issues

### VPS berat/lambat setelah reboot (SSH delay 1–2 menit)

Root cause: tiga bug yang saling berkaitan menyebabkan DNS sistem mati total setelah reboot.

1. **`dnsxx()`** — `chattr +i /etc/resolv.conf` mengunci file, lalu `systemd-resolved` dihidupkan kembali padahal sudah di-disable. Resolved gagal tulis ke resolv.conf yang immutable → DNS broken. **Fix:** `chattr -i` sebelum edit, hapus `start/enable systemd-resolved`.

2. **`rc.local`** — redirect semua DNS (port 53 → 5300) tanpa cek apakah SlowDNS running. SlowDNS tidak punya systemd service yang di-enable, jadi port 5300 kosong → semua DNS query timeout. **Fix:** redirect hanya jika `systemctl is-active slowdns`.

3. **`limit/sshd`** — `UseDNS` dan `GSSAPIAuthentication` dikomentari (default aktif). sshd melakukan reverse DNS lookup setiap koneksi masuk, timeout karena DNS sudah broken. **Fix:** `UseDNS no` dan `GSSAPIAuthentication no` diaktifkan eksplisit, plus `sed` hardening di `ins_SSHD()` sebagai fallback.
