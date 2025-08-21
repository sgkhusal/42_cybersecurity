#!/bin/bash

BALANCE=$(curl http://localhost:8080/balance -s | jq -r '.balance')
echo "balance antes: $BALANCE"

curl -X POST -d "amount=$BALANCE" http://localhost:8080/transfer

BALANCE2=$(curl http://localhost:8080/balance -s | jq -r '.balance')
echo
echo "balance depois: $BALANCE2"