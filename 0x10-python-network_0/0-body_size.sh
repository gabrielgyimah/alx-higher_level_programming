#!/usr/bin/env bash
# Displays the size of the body of an HTTP response

curl -I "$1" | grep -iF 'content-length' | cut -d " " -f 2
