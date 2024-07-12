#!/usr/bin/python3
"""Log parsing module"""
import sys
import signal
import re

log_entry_pattern = re.compile(
    r'^(?P<ip>[^\s]+)\s*-\s*\[(?P<date>\d{4}-\d{2}-\d{2} \d{2}:' +
    r'\d{2}:\d{2}\.\d{6})\] "GET /projects/260 HTTP/1\.1" ' +
    r'(?P<status>\d{3}) (?P<size>\d+)$'
)

total_size = 0
code_lines = {}


def print_stuff():
    print(f"File size: {total_size}", flush=True)
    sorted_code_lines = list(code_lines.keys())
    sorted_code_lines.sort()

    for status_code in sorted_code_lines:
        print(f"{status_code}: {code_lines[status_code]}", flush=True)


def signal_handler(signal, frame):
    print_stuff()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


count = 0
for line in sys.stdin:
    match = log_entry_pattern.match(line.strip())
    if match:
        file_size = int(match.group('size'))
        try:
            status_code = int(match.group('status'))
        except Exception:
            continue
        total_size += file_size
        if status_code not in code_lines:
            code_lines[status_code] = 0
        code_lines[status_code] += 1
        count += 1

    if count % 10 == 0:
        print_stuff()

print_stuff()
