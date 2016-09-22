from flask import Flask, render_template

app = Flask(__name__)

import random

"""
Args:
    File name to be read
Returns:
    List of csv in [start, end, job title] format.
    Ex: [0, 65, Maintenance]
"""

def listify(filename):
    tmp = 0
    L=[]
    lfile = open(filename, 'r').readlines()
    for row in lfile[1:-1]:
        num = int(10 * float(row[row.rfind(',')+1:])) # get percentage
        start = tmp
        tmp = num + start
        L.append([start, tmp, row[:row.rfind(',')]])
    return L

"""
Args:
    None
Returns:
    Job title randomly generated
    based on percentage value
"""

def chooser():
    rand = int(random.random() * 1000)
    L = listify('occupations.csv')
    for row in L:
        if rand > row[0] and rand < row[1]:
            return row[2]

@app.route("/")
def root():
    return render_template("template.html", foo="Occupations", L=listify('occupations.csv'), randjob = chooser())

if __name__ == '__main__':
    app.run(debug=True)
