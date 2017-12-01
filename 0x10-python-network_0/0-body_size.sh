#!/bin/bash
#displays the size of the body of the response
curl -s -o /dev/null --write-out "%{size_download}\n" "$1"
