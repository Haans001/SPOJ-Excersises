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




# KMP - wyszukiwanie wzorca w tekscie
patternLen = int(input("Enter a pattern length: "))
pattern = input("Enter a pattern: ")
text = input("Enter a text: ")

indexes = []

for i in range(len(text)- patternLen +1):
  patternIndex = 0
  isValid = True
  for j in range(i,i+patternLen):
    if text[j] != pattern[patternIndex]:
      isValid = False
    patternIndex+=1
  if(isValid):
    indexes.append(i)  

print(indexes)






# OSTSIL - Ostania niezerowa cyfra silni

def factorial(n):
  result = 1
  for i in range(1,n+1):
    result*=i
  return result

number = str(factorial(int(input("Enter a number: ")))) [::-1]

for c in number:
  if c != '0':
    finalResult = c
    break;

print(finalResult)








# TOPSES - Sezamie, otwórz się!


firstChain = list(input("firstChain: "))
secondChain = list(input("secondChain: "))
result = 'no'

for i in range(len(firstChain)):
  if(firstChain == secondChain):
    result = 'yes'
    break;

  secondChain.insert(0,secondChain.pop())

print(result)



