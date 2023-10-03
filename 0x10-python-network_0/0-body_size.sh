#!/bin/bash
# gets body from web site
curl -s -i "$1" | tail -n 1 | wc -c
