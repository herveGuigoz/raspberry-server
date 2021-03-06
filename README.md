## Traefik server for Raspberry Pi.

### Services

|             | Doc                                                                 | Path
|-------------|---------------------------------------------------------------------|-------------------
| Traefik     | [documentation](https://docs.traefik.io/getting-started/concepts/)  | `traefik.{domain}/dashboard/#/`
| Firefly     | [documentation](https://docs.firefly-iii.org/)                      | `firefly.{domain}`
| PiHole      | [documentation](https://docs.pi-hole.net/)                          | `pihole.{domain}/admin`
| Files Server |                                                                     | `files.{domain}`

### Installation

* `touch .env`
* `touch conf/acme.json`
* `chmod 600 conf/acme.json`
* `mkdir logs/`
* `touch logs/traefik.log`

Edit `.env` file, then run:

```
make install
```

### Cron for db backup

- edit `crontab` file:
```
crontab -e
```

- add this line (replace $(path)):
```
0 0 * * * docker exec -it fireflydb  pg_dump -Ufirefly --column-inserts --data-only firefly > $(path)/db/firefly_backup.sql
```

### import sql backup

`scp pi@${IP}:${PI_PATH}/firefly_backup.sql ${LOCAL_PATH}`

### Setup Pihole

#### Router / FAI

- Your raspberry must have static ip adress.
- Configure DNS Serveur of your router with the pi ip adress


#### Edit setting in admin panel

under `Settings`, `DNS`, `Interface listening behavior` select `Listen on all interfaces, permit all origins`.
