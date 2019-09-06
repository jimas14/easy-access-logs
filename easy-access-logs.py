import argparse

parser = argparse.ArgumentParser(description='Get a readable CSV file from a directory of access log files')
parser.add_argument('--directory', help='Directory where access log files exist', required=True)
parser.add_argument('--shorten-names', help='If your access log filenames are large, include this argument')

args = parser.parse_args()

# Shorten file names if specified

# Combine access log files into one text file

# Parse text file into readable CSV
