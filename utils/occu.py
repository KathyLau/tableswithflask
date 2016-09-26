import random

"""
Args:
    File name to be read
Returns:
    Dictionary version of csv in : { job title: [start, end, link] } format.
    Ex: { Maintenance: [0, 65, link] }
"""

def create_dictionary(filename):
    lfile = open(filename, 'r').readlines()
    d = {}
    uppBound = 0

    for row in lfile[1:-1]:
        #make all occupation titles w/o quotes and split them from reverse direction to 3 items
        row = row.replace('"', '').rsplit(',', 2)
        title = row[0]
        percent = row[1]
        link = row[2]

        #set new lower and upper bounds for random choosing usage
        lowBound = uppBound
        uppBound = float(percent) + lowBound
        d[title] = [lowBound, uppBound, link]
    return d


"""
Args:
    Dictionary to be read
Returns:
    Job title randomly generated
    based on percentage value
"""

def chooser(d):
    rand = int(random.random() * 99.8)
    for key in d:
        if rand > d[key][0] and rand < d[key][1]:
            return key
