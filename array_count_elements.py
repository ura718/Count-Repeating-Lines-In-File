#!/usr/bin/python

d = dict()
a = [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1]
for item in a:
  try:
    d[item]+=1
  except KeyError:
    d[item]=1

print a
for k,v in d.items():
  print "%s,%s" % (k,v)
