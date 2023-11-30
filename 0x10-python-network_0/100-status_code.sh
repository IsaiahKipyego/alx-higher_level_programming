#!/bin/bash
# script that prints only status code on terminal
curl -s "$1" -o /dev/null -w "%{http_code}"
