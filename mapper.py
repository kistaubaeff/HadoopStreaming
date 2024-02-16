#!/usr/bin/env python
"""mapper.py"""
from datetime import datetime
import sys


def rounder(t):
    """
    Round a given datetime object to the nearest hour by setting the minutes and seconds to zero.
    Parameters:
    t (datetime): The datetime object to be rounded.
    Returns:
    datetime: The rounded datetime object.
    """
    if t.minute >= 30:
        return t.replace(second=0, microsecond=0, minute=0, hour=t.hour+1)
    return t.replace(second=0, microsecond=0, minute=0)


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().rstrip(';')
    # split the line into words
    words = line.split('\n')
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        sys.stderr.write("reporter:counter:testcountergroup,wordcounter,1\n")
        current = word.split(', ')
        try:
            date = rounder(datetime\
                        .strptime(current[0],\
                        '%d.%m.%Y %H:%M:%S.%f'))\
                        .strftime("%d.%m.%Y %H:%M:%S.%f")[:-3]
            print(f"{date}, {current[1]}, {current[2].split('_', 1)[1]}\t{current[3]}")
        except ValueError:
            # process dummy string
            continue
