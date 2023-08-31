#!/bin/bash
# Sends a request with apice of information
curl -H "Content-Type: plain/text" -d "You got me!" "$1"
