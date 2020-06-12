- Instead of make rederection per service, you could make traefik global middleware:

```
# global redirect to https
traefik.http.routers.http-catchall.rule: hostregexp(`{host:.+}`)
traefik.http.routers.http-catchall.entrypoints: web
traefik.http.routers.http-catchall.middlewares: redirect-to-https
traefik.http.middlewares.redirect-to-https.redirectscheme.scheme: https
```

