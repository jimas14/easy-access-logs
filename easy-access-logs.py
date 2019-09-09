#!/usr/bin/python
# -*- coding: utf-8 -*-

# S3 Access Logs for Humans
# Author: James Schleicher (https://github.com/jimas14)
# Regex from https://gist.github.com/nathangrigg/2363393

import os
import re
import argparse
from pandas import DataFrame


parser = argparse.ArgumentParser(description='Get a CSV file from a directory of S3 access log files')
parser.add_argument('--directory', help='Absolute path to where access log files exist', required=True)

args = parser.parse_args()

# Define regex to convert an access log string to a tuple.
access_log_regex = re.compile(r'(?P<owner>\S+) (?P<bucket>\S+) (?P<time>\[[^]]*\]) (?P<ip>\S+) ' +
                              r'(?P<requester>\S+) (?P<reqid>\S+) (?P<operation>\S+) (?P<key>\S+) ' +
                              r'(?P<request>"[^"]*"|-) (?P<status>\S+) (?P<error>\S+) (?P<bytes>\S+) ' +
                              r'(?P<size>\S+) (?P<totaltime>\S+) (?P<turnaround>\S+) (?P<referrer>"[^"]*"|-) ' +
                              r'(?P<useragent>"[^"]*"|-) (?P<version>\S)')

# Combine access log files into a list.
access_logs = []
for f in os.listdir(args.directory):
    with open(args.directory + '/' + f, "rb") as infile:
        for line in infile:
            groups = re.match(access_log_regex, str(line))
            if groups:
                access_logs.append(groups.groups())

# Convert list of access logs to a CSV.
columns = ['Bucket_Owner', 'Bucket', 'Time', 'Remote_IP', 'Requester',
           'Request_ID', 'Operation', 'Key', 'Request_URI', 'HTTP_status',
           'Error_Code', 'Bytes_Sent', 'Object_Size', 'Total_Time',
           'Turn_Around_Time', 'Referrer', 'User_Agent', 'Version_Id']
df = DataFrame(access_logs, columns=columns)
df.to_csv('access-logs.csv', index=False)
