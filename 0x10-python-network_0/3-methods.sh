#!/bin/bash
# Displays all HTTP methods the server will accept
curl -Is "$1" | awk 'tolower($0) ~ /allow/ {print $2}'
