# easy-access-logs

I made this script because S3 access logs are an absolute nightmare to read through, let alone
review at a large scale.

Given a directory full of S3 access log files, the script will generate a complete CSV of all access logs.

Make sure you are in a Python 3.7 environment before running.

## Usage
1. Download all access logs to one directory using AWS S3 cli or preferred method.
2. Run `python easy-access-logs.py --directory=/full/path-to/logfiles`
