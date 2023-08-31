#!/usr/bin/env bash
# Displays the size of the body of an HTTP response

if [ "$#" -lt 1 ]; then
	return
else
	curl -I -s "$1" | awk '/Content-Length/ {print $2}'
fi
