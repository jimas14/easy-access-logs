# easy-access-logs

I made this script because S3 access logs are an absolute nightmare to read through, let alone
parse at a large scale.

Given a directory full of access log files, this script will combine them into one file and
then parse that into a readable CSV.

Ordering is not maintained in this script, although outputted CSV will be easily sortable.

## Usage
    1. Download all access logs to a directory using AWS S3 cli or preferred method.
