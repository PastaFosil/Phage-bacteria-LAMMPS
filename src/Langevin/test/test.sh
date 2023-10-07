#!/bin/bash

strMsg="ERROR"
# Call the Python script with the parameters
output=$(python3 test.py)

echo "$output"
if [ "$output" == "$strMsg" ]
then
    echo "They are equal c:"
else
    echo "They are NOT equal :c"
fi