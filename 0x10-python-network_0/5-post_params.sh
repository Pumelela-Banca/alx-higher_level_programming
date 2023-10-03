#!/bin/bash
# sends post and prints results
curl -sLf "$1" -d '{"email": "test@gmail.com", "subject":"I will always be here for PLD" }' -X POST
