#!/usr/bin/python3

import sys 

current_destination = None 
current_rank = None
dest_dict = {}
for line in sys.stdin:
    destination, source_info = line.split('\t')
    source_info = source_info.split(' ')
    source = source_info[0]
    source_rank = source_info[1]
    source_outdegree = source_info[2]
    if(source not in dest_dict):
        dest_dict[source] = {}
        dest_dict[source]['out'] = []
        dest_dict[source]['rank'] = 0
    if(destination not in dest_dict):
        dest_dict[destination] = {}
        dest_dict[destination]['out'] = []
        dest_dict[destination]['rank'] = 0

    dest_dict[source]['out'].append(destination)
    try:
        source_rank = source_rank.strip()
        source_rank = float(source_rank)
        source_outdegree = int(source_outdegree)
    except ValueError:
        continue
    if(current_destination == destination):
        if(destination != source):
            current_rank += source_rank/source_outdegree
    else:
        if(current_rank):
            dest_dict[destination]['rank'] = current_rank
        if(destination != source):
            current_rank = source_rank/source_outdegree
        else:
            current_rank = 0
        current_destination = destination
if(current_destination == destination):
    dest_dict[destination]['rank'] = current_rank

for key in dest_dict:
    print('%s %s %s' % (key, dest_dict[key]['rank'], ' '.join(map(str, dest_dict[key]['out']))))
