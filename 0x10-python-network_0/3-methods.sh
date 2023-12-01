#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -sI X OPTIONS "$1" | grep "Allow" | awk '{print $2}'
