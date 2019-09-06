#!/bin/bash
# cd to directory provided by user
cd "$1" || exit
# iterate through all files, changing the name to the value of $i
i=0
for f in *; do
    i=$(( i + 1 ))
    cp "$f" $i;
done