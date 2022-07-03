#!/usr/bin/env python3
import csv

def save_to_file(jobs):
    file = open('collect.csv',mode='w')
    writer = csv.writer(file)
    writer.writerow(['Company',' Title',' Location',' Link'])
    for job in jobs:
        if job is None:
            continue
        else:
            writer.writerow(job.values())
