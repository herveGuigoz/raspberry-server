## Traefik server for Raspberry Pi.

### Services

|           | Doc
|-----------|-----
| Traefik   | [documentation](https://docs.traefik.io/getting-started/concepts/)
| Firefly   | [documentation](https://docs.firefly-iii.org/)
| PiHole    | [documentation](https://docs.pi-hole.net/)

### Installation

* Edit `.env` file, then run:

```
make install
```

### Cron for db backup

- edit `crontab` file:
```
crontab -e
```

- add this line:
```
0 0 * * * make db-backup
```
