# DECIMAL TO HEX
# import math

# signs = {"1":1, "2" : 2, "3":3, "4":4, "5": 5, "6":6,"7":7,"8" : 8, "9" : 9, "10":'A', "11":'B', "12":'C', "13":'D', "14":'E', "15" : "F" }

# number = 643450234
# result = ''

# while number != 0:
#   result += str(signs[str(number%16)])
#   number = math.floor(number/16)

# result = result [::-1]
# print(result)







# NIEKOLEJNE

# from random import randrange
# import time
# start_time = time.time()
# numbers = []
# iterations = 100000

# def swap(index):
#   swapIndex = randrange(iterations)

#   numbers[index], numbers[swapIndex] = numbers[swapIndex], numbers[index]

# def unsortItems():
#   unsorted = True
#   print('sorting')
#   for x in range(len(numbers)):
#     swap(x)

#   for x in range(1, len(numbers)-1):
#     if abs(numbers[x-1] - numbers[x]) < 3 or abs(numbers[x+1] - numbers[x]) < 3 :
#       unsorted = False

#   if not unsorted :
#     unsortItems()


# for x in range(iterations+1):
#   numbers.append(x)

# unsortItems();
# print(numbers)
# print(time.time() - start_time)







# PUNKTY W OKREGU
# import math
# circle = {}
# points = []
# results = []

# circleXY = input("Enter Circle center x y r: ")
# circle['x'] = int(circleXY.split()[0])
# circle['y'] = int(circleXY.split()[1])
# r = int(circleXY.split()[2])

# tests = int(input('How many tests: '))

# for x in range(tests):
#   point = {}
#   pointXY = input("Enter point x y: ")
#   point['x'] = int(pointXY.split()[0])
#   point['y'] = int(pointXY.split()[1])
#   points.append(point)


# for i in range(tests):
#   d = abs(math.sqrt(math.pow(circle['x'] - points[i]['x'], 2) + math.pow(circle['y'] - points[i]['y'], 2)))
#   if d > r:
#     results.append('O')
#   elif d < r :
#     results.append('I')
#   else :
#     results.append('E')  
  
# print(results)







# ROT13
# word = input("Enter a word to code it: ")
# result = ''

# def codeChar(c, islow):
#   asciiCode = ord(c)

#   for i in range(1, 14):
#     if asciiCode >= 90:
#       asciiCode = 64
#     asciiCode+=1
    
#   resultChar = chr(asciiCode)
#   return resultChar.lower() if islow else resultChar



# def codeDigit(c):
#   asciiCode = ord(c)

#   for i in range(1, 6):
#     if asciiCode >= 57:
#       asciiCode = 47
#     asciiCode+=1

#   return chr(asciiCode)


# for c in word:
#   islow = c.islower()
#   if c.isalpha():
#     c = c.upper()
#     result+=codeChar(c, islow)
#   elif c.isdigit():
#     result+=codeDigit(c)
#   else:
#     result+=c

   
# print(result)





# FORMULARZE
# import re
# valid = False
# result = 3

# inp = input("Enter a valid format: ")
# result = re.search("Imie: (.*); Nazwisko: (.*); Data ur.: (.*)", inp)

# # imie
# if re.match(r"^[A-Z][a-z]{1,10}$", result.group(1)):
#   print("Good name")
#   valid = True
# else:
#   result = 0;

# #nazwisko
# if re.match(r"^[A-Z][a-z]{1,20}$", result.group(2)) and valid:
#   print("Good surname")

# else:
#   result = 1
#   valid = False


# #data urodzenia
# if re.match(r"([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", result.group(3)) and valid:
#   print("good surname")



# PĄCZKI

# tests = int(input("Number of tests: "))

# for x in range(tests):
#   inp = input("c k w [liczba kotów, udźwig Harrego oraz waga pączka]")
#   c = int(inp.split()[0])
#   k = int(inp.split()[1])
#   w = int(inp.split()[2])

#   if(c*w>k):
#     print("poddaj sie")
#   else:
#     print("uda sie")  


