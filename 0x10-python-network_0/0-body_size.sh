#!/bin/bash
# gets body from web site
give_info=$(curl -s -i "$1")
echo "$give_info" | wc -l
