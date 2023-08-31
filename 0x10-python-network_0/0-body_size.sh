#!/usr/bin/env bash
# Displays the size of the body of an HTTP response

if [ "$#" != 1 ]; then
	exit
else
	curl -I -s "$1" | awk '/Content-Length/ {print $2}'
fi
