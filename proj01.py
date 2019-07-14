import numpy as np
import pandas as pd


def merge_csv_files():
    frame1 = pd.read_csv('commit.csv')
    frame2 = pd.read_csv('issues.csv')
    resulting_frame = frame1.merge(frame2, left_on = 'Key', right_on = 'Key')

def sort_by_column():
    resulting_frame_sorted = resulting_frame.sort_values(by='created', axis=1, ascending)

def group_by_author():
    a = 0
    resulting_frame_grouped = resulting_frame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False,
                            observed=False)

    while a < 10:
        for line in resulting_frame_grouped:
            print(line)
            a +=1

def show_commits_bug():
    resulting_frame_bug[resulting_frame.issue_type = Bug]
    print(resulting_frame_bug)

def show_commits_date_severity():
    a > 2016-04-01T00:00:00.000+0000 AND a < 2016-10-01T00:00:00.000+0000
    resulting_frame_date_severity[(resulting_frame.severity = 10) | (resulting_frame.created = a)]
    print(resulting_frame_date_severity)

def show_longest_commits():
    c = []
    r = 0
    v = b - a
    a = resulting_frame[resulting_frame.created]
    b = resulting_frame[resulting_frame.resolved]
    for line in resulting_frame:
        append.c(v)
    c.sort(reverse = True)
    while r < 10:
        for line in c:
            print(line)
            r += 1