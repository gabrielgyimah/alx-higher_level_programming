#!/bin/bash
# Sends a POST request to the passed URL
curl -sX POST -F "email: test@gmail.com" -F "subject: I will always be here for PLD" "$1"
