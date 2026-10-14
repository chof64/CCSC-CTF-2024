#!/bin/sh
# Usage: ./up.sh [--build]
if [ "$1" = "--build" ]; then
  docker compose up -d --build
else
  docker compose up -d
fi
docker compose ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"
