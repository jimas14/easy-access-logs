# easy-access-logs

I made this script because S3 access logs are an absolute nightmare to read through, let alone
parse at a large scale.

Given a directory full of access log files, this script will combine them into one file and
then parse that into a readable CSV.

Ordering is not maintained in this script, although outputted CSV will be easily sortable.

This script is meant to be interpreted by Python 3.7

## Usage
    1. Download all access logs to one directory using AWS S3 cli or preferred method.
    2. Run `python easy-access-logs --directory=/full/path-to/logfiles`
