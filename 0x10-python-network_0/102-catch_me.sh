#!/bin/bash
# Sends a request with apice of information
curl -H "Content-Type: plain/text" -d "You got me!" 0.0.0.0:5000/catch_me
