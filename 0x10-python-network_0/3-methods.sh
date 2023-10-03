#!/bin/bash
# lists all methods
curl -si $1 | grep -i "Allow" | cut -d ' ' -f 2
