#!/bin/bash
# gets body from web site
curl -s -i "$1" | grep  -i | cut -d ' ' -f 2
