# Creating Variables
print('Creating Variables')
a = 'John'
b = 9
print(a) # John
print(b) # 9

# Variables - Assign Multiple Values
print('Variables - Assign Multiple Values')
c, d, e = "Orange", "Banana", "Cherry"
print(c) # Orange
print(d) # Banana
print(e) # Cherry

# One Value to Multiple Variables
print("\nOne Value to Multiple Variables")
f = g = h = "Orange"
print(f) # Orange
print(g) # Orange
print(h) # Orange

# Unpack a Collection
print('\nUnpack a Collection')
fruits = ["apple", "banana", "cherry"]
i, j, k = fruits
print(i) # apple
print(j) # banana
print(k) # cherry

# Output Variables
print('\nOutput Variables')
l = "Python"
m = "is"
n = "awesome"
print(l, m, n) # Python is awesome

# Global Variables
print('\nGlobal Variables')
# case 1
o = "awesome"

def myfunc():
  print("Python is", o)

myfunc() # Python is awesome   

# case 2
def myfunc2():
  o = "fantastic"
  print("Python is", o)

myfunc2() # Python is fantastic
