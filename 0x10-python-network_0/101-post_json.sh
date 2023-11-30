#!/bin/bash
# sends json post request together with  file content
curl -sX POST "$1"  -H "Content-Type: application/json" -d @"$2"
