#!/bin/bash
# Displays only the status code of the response
curl -I -s -o /dev/null -w "%{http_code}" "$1"
