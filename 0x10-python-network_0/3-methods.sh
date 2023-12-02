#!/bin/bash
# script to display all HTTP methods server will accept
curl -sI "$1" | grep -F "Allow" | sed s/"Allow: "//
