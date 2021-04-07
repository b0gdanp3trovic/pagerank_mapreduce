#!/usr/bin/python3
import sys



for line in sys.stdin:
    line = line.split(' ')
    source = line[0].strip().replace('\n', '').replace('\t', '')
    rank = line[1].strip().replace('\n', '').replace('\t', '')
    destinations = line[2:]
    for destination in destinations:
        destination = destination.strip().replace('\n', '').replace('\t', '')
        print('%s\t%s %s %s' % (destination, source, rank, len(destinations)))
