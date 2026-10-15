# SETUP — Windows host as CTF server (Docker Desktop)

All `ports:` in `docker-compose.yml` are bound to `0.0.0.0` so external users can reach them while containers are up. Players connect to `<HOST-IP>:<port>`, never `localhost`.

## 0. Prereqs (once)

- Windows 10/11 + Docker Desktop (WSL2 backend) installed and running.
- This repo cloned on the Windows machine.

## 1. Open firewall (Admin PowerShell, copy-paste)

```powershell
New-NetFirewallRule -DisplayName "CCSC-CTF" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 1337,1338,1339,1340,1341,1342,1343,1344,1345,13373,9745,9746,9747,8080,8083,3000,3001,3002,3003,3004,3005,3006,5001,8000
```

If you re-run and it errors "already exists", remove first:

```powershell
Remove-NetFirewallRule -DisplayName "CCSC-CTF"
```

## 2. Keep the machine awake (Admin PowerShell)

```powershell
powercfg /change standby-timeout-ac 0
powercfg /change hibernate-timeout-ac 0
```

Docker Desktop > Settings > General > check `Start Docker Desktop when you sign in`.

## 3. Find your HOST-IP (PowerShell)

```powershell
ipconfig
```

Use the `IPv4 Address` on your LAN adapter (e.g. `192.168.1.50`). Same-LAN players use this directly. For internet players, also do step 6.

## 4. Start all challenges (PowerShell, in repo root)

```powershell
docker compose up -d --build
docker compose ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"
```

Updates later (images already built):

```powershell
docker compose up -d
```

## 5. Verify ports are on 0.0.0.0 (PowerShell)

```powershell
netstat -an | findstr LISTENING | findstr "1337 3000 8080"
docker compose ps
```

Each port must show `0.0.0.0:<port>`. Quick connect test from the host:

```powershell
Test-NetConnection localhost -Port 1337
```

Ask one LAN player to test: `Test-NetConnection <HOST-IP> -Port 1337` or open `http://<HOST-IP>:3000` for web challenges.

## 6. Internet players only (skip if same LAN/Wi-Fi)

1. Router: give the Windows box a static DHCP lease (bind its MAC to e.g. `192.168.1.50`).
2. Router > Port Forwarding: forward each TCP port from step 1 to `192.168.1.50`.
3. Give players your public IP (`curl ifconfig.me` from host) + port.

If CGNAT / no router access / ISP blocks inbound, use Tailscale or Cloudflare Tunnel instead — port-forwarding cannot work there.

## 7. Player address table

Replace `<HOST-IP>` with step 3 (LAN) or public IP (step 6):

| Challenge | Address |
|---|---|
| andromeda-v1 | `nc <HOST-IP> 1337` |
| andromeda-v2 | `nc <HOST-IP> 1338` |
| inverted-oracle | `nc <HOST-IP> 13373` |
| armored-up | `nc <HOST-IP> 1339` |
| superguesser 1/2/3 | `nc <HOST-IP> 9745` / `9746` / `9747` |
| got-override | `nc <HOST-IP> 1340` |
| hijack | `nc <HOST-IP> 1341` |
| infiltration | `nc <HOST-IP> 1342` |
| model-scan | `nc <HOST-IP> 1343` |
| spilled | `nc <HOST-IP> 1344` |
| license-ops | `nc <HOST-IP> 1345` |
| tlv | `http://<HOST-IP>:8080` |
| arcane-runes | `http://<HOST-IP>:3000` |
| underground-watch-1 | `http://<HOST-IP>:3001` |
| underground-watch-2 | `http://<HOST-IP>:3002` |
| shodanql | `http://<HOST-IP>:3003` |
| portal | `http://<HOST-IP>:3004` |
| warriors-tech-shop | `http://<HOST-IP>:3005` |
| shodanql-revenge | `http://<HOST-IP>:3006` |
| cross-checked-report | `http://<HOST-IP>:5001` |
| microbuns-backend | `http://<HOST-IP>:8083` |

## Troubleshoot

```powershell
# container down? restart just it
docker compose up -d <service-name>
docker compose logs <service-name> --tail 50

# port conflict / Windows reserved range
netstat -ano | findstr :1337
netsh interface ipv4 show excludedportrange protocol=tcp

# full restart
docker compose down
docker compose up -d
```

Do not run `docker compose down` during the event — it removes containers and drops all ports.
