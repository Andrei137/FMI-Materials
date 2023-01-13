# -*- coding: utf-8 -*-
"""Lab_PA_1_Sg1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EfHNAjHyVE0gER0rbF1LxeX0IbtsqUDR
"""

print("Hello World")

a = input()

a

b = input("Pune o variabile: ")

b

# This is a comment

a = 5 # this a comment

# multi
# line
# comment

"""
This 
is a multi
line
comment
"""

# Variabile
a = 10 # int
b = 5.2 # float/double
c = 'salut' # str
d = [1, 2] # list

print(a, b, c, d)

type(c)

from math import sqrt

# Operatii pe numere
print(int(a + b))
print(a + b)
c = 7
d = a - b
e = a * b
f = a / b
g = a // c
print(d, e, f, g, sep='\n')

print(10 ** 4)
print(64 ** 0.5)
print(sqrt(64))
print(f)

# String
a = 'this an string'
b = "this another string"
c = "this is Nicu's string"
d = 'this is Nicu\'s string'

print(d)
print(a[0], a[1])
print(a[0:5]) # [a, b)
print(a[0:7:2])

print(a[-5:-2])
print(a[-1])

rev_a = a[::-1]
rev_a

# Metode string-uri
a = 'this an string\n'
print(a.lower())
print(a.upper())
print(a)
print(a.capitalize())
print(a.isalpha())

print(a.split("a"))

a, b, c = 1, 2, 3
a, *_ = [1, 2, 4]

print(a, b)

_ = 2

# Liste
a = []
a.append(1)
a.append(2)
a.append('Salut')
# a.pop()

a

a.pop()

a

a.pop(0)

a = [1, 2, 3]
b = ["Salut", "Papa"]

a.extend(b)

a

print(a[0])
print(a[-1])
print(a[::-1])

a[-1] = 10
a

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

mat[0][1]

mat5 = 0 # todo

# If, booleans, conditionals
if 3 < 5:
  print("Mai mic")
elif 3 == 5: 
  print("Egal")
else:
  print("Nu egal")

print(3 < 5)
print(3 == 5)
print(3 > 5)
print(3 <= 5, 3 >= 5)
print(3 != 5)

# c = (3 < 5) ? 'da' : 'nu'
c = 'da' if 3 < 5 else 'nu'
print(c)

print(3 < 5 and 3 < 10)
print(3 > 10 or 3 == 3)
print(not 3 != 3)
a = 5
b = 3
c = 10
if a < b and (b < c or c < a):
  print("haha")

# For
# for (int i = 0; i <= n; i ++) { ... }
n = 10
for i in range(0, n, 2):
  print(i)

for i in range(n, -1, -1):
  print(i)

a = [1, 2, 3, 4, 5, 6, 10]
n = len(a)

for i in range(len(a)):
  print(a[i])

for x in a:
  print(x)

for i, x in enumerate(a):
  print(i, x)

# List comprehension
a = [i for i in range(100, 10, -2) if i % 2 == 0]
a

b = [i // 2 for i in a]
b

c = [tupl for tupl in enumerate(a)]
c

# Tuplu
a = (1, 2, 3)
a

a[0] = 4

# Set
s = set()
b = []
for i in range(100):
  s.add(i // 10)
  b.append(i // 10)

print(s)
print(b)

s.remove(1)

s

a = 2
if a in s:
  print(True)

len(s)

# Dictionare
d = dict()

for i, x in enumerate(range(10, 1, -1)):
  d[i] = x ** 2

print(d)

d['salut'] = 'hello'

d

print(1 in d)
print(100 in d)

print(d.keys())
for key in d.keys():
  print(d[key])

print(d.values())

print(d.items())

# Functiile
def func(x):
  if x < 10:
    return x ** 2
  return x ** 3

print(func(10))
print(func(5))

def func(x, y, z):
  print(x - y * z)

func(10, 2, 'salut')

a = lambda x, y: x ** y

type(a)

a(5, 6)

a = [10, -1, 15, 2, 0, 100, 83, 3]
a.sort()
a

sorted(a)
a

a = [10, -1, 15, 2, 0, 100, 83, 3]
a.sort(key=lambda x: x % 3)

a

mat = [0] * 10
mat

# GRESIT
mat = [[0] * 5] * 5
mat

mat[0][1] = 5

mat

# CORECT
n, m = 7, 10
mat = [[0] * (m - i + 1) for i in range(n)]
mat

a = [1, 2, 3, 4, 5]
b = a.copy()
print(b)

b = mat.copy()
b[0][1] = 5

b

mat

from copy import deepcopy
b = deepcopy(mat)
b[0][2] = 10

b

mat
