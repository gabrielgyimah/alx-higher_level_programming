#!/bin/bash
# Sends a POST request to the passed URL
curl -s -X POST -H "email: test@gmail.com" -H "subject: I will always be here for PLD" "$1"
