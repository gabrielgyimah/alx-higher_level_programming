#!/bin/env bash
# Displays response size only

curl -si "$1" | grep -iF "content-length" | cut -d " " -f 2
