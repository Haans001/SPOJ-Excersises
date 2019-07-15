# IMIONA

import operator
f = open('index.txt', 'r',)
lines = f.read().split('\n')
names = []
namesDict = {}

for line in lines:
  names.append(line.split()[2].upper())

names.sort()

for name in names:
  if name in namesDict.keys():
    namesDict[name]+=1
  else:
    namesDict[name] = 1

sortedList = sorted(namesDict.items(), key=operator.itemgetter(1), reverse=True)

for el in sortedList:
  print(f"{el[0]} {el[1]}")
