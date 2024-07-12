#!/usr/bin/python3
"""Log parsing module"""
import sys
import signal
import re

log_entry_pattern = re.compile(
    r'^(?P<ip>(?:\d{1,3}\.){3}\d{1,3}) - \[(?P<date>\d{4}-\d{2}-\d{2} \d{2}:' +
    r'\d{2}:\d{2}\.\d{6})\] "GET /projects/260 HTTP/1\.1" ' +
    r'(?P<status>\d{3}) (?P<size>\d+)$'
)
log_object = {
    "total_size": 0,
    "no_line_per_code": {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
}


def print_stuff():
    print(f"File size: {log_object['total_size']}")
    for status_code, number in log_object['no_line_per_code'].items():
        print(f"{status_code}: {number}")


def signal_handler(signal, frame):
    print_stuff()


signal.signal(signal.SIGINT, signal_handler)


count = 0
for line in sys.stdin:
    match = log_entry_pattern.match(line.strip())
    if match:
        log_object['total_size'] += int(match.group('size'))
        log_object['no_line_per_code'][match.group('status')] += 1
        count += 1

    if count % 10 == 0:
        print_stuff()
