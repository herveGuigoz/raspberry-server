#!/bin/bash

if [ "$1" ]; then
  docker exec -it fireflydb pg_restore -d firefly $1
else 
    echo "Missing file argument"
fi