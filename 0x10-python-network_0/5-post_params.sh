#!/bin/bash
# sends post and prints results
curl -s -X POST -d '{"email": "test@gmail.com", "subject":"I will always be here for PLD" }' -X POST "$1"
