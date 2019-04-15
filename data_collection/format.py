#!/usr/bin/python

from datetime import datetime
import sys
import time

def get_data():
    return open('data.txt').read()

def save(*args):
    with open('data.csv', 'a') as f:
        f.write(','.join(map(str, args)))
        f.write('\n')

def collect_data():
    dump = get_data()
    station = None

    for line in dump.split('\n'):
        line_type = 'detail' if line.startswith('\t') else 'meta'
        line_part = line.split()
        if line_type == 'meta':
            if station:
                save(timestamp, station, rx_bytes, tx_bytes, rx_packets, tx_packets, signal, rx_bitrate, tx_bitrate, inactive_time, tag)
                station = None
            if line.strip().isdigit():
                timestamp = int(line.strip())
            elif line.startswith('Station'):
                station = line_part[1]
            else:
                tag = line.strip()
        elif line_type == 'detail':
            if line_part[0] == 'rx' and line_part[1] == 'bytes:':
                rx_bytes = int(line_part[2])
            elif line_part[0] == 'rx' and line_part[1] == 'packets:':
                rx_packets = int(line_part[2])
            elif line_part[0] == 'tx' and line_part[1] == 'bytes:':
                tx_bytes = int(line_part[2])
            elif line_part[0] == 'tx' and line_part[1] == 'packets:':
                tx_packets = int(line_part[2])
            elif line_part[0] == 'signal:':
                signal = int(line_part[1])
            elif line_part[0] == 'rx' and line_part[1] == 'bitrate:':
                rx_bitrate = float(line_part[2])
            elif line_part[0] == 'tx' and line_part[1] == 'bitrate:':
                tx_bitrate = float(line_part[2])
            elif line_part[0] == 'inactive' and line_part[1] == 'time:':
                inactive_time = int(line_part[2])

if __name__ == '__main__':
    collect_data()
