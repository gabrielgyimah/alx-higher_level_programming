#!/bin/bash
# Displays all HTTP methods the server will accept
curl -Is "$1" -X OPTIONS | awk 'tolower($0) ~ /^allow:/ {print substr($0, 8)}'
