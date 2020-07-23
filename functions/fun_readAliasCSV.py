import csv

def readAliasCSV(fileName):
    reader = csv.reader(open(fileName, 'r'))
    d = {}
    for row in reader:
	    k, v = row
	    d[k] = v

    return d




