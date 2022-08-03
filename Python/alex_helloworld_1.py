import csv
from itertools import islice
from collections import OrderedDict

MAINDIR = "./"
val = input("Enter name of the PENDEJO you're looking for: ")
with open(MAINDIR + 'atp_matches_2022.csv') as mf:
  readit = csv.reader(mf,delimiter=',')
  csvdata = list(readit)
  i = 0
  while i < len(csvdata):
    if val in csvdata[i]:
      print(csvdata[i])
    i = i + 1
