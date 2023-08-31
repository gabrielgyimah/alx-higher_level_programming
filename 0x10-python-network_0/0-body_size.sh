#!/bin/bash
# Displays response size only
curl -Is "$1" | awk '/Content-Length/ {print $2}'
