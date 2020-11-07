#!/bin/bash

if [ "$1" ]; then
  docker exec -it fireflydb  pg_dump -Ufirefly --column-inserts --data-only "$1" > firefly_backup.sql
else 
    echo "Missing file argument"
fi