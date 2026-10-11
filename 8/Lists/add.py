# Add List Items

# Append Item
print('\nAppend Item')
a = ["apple", "banana", "cherry"]
a.append("orange")
print(a)  # ['apple', 'banana', 'cherry', 'orange']

# Insert Item
print('\nInsert Item')
b = ["apple", "banana", "cherry"]
b.insert(1, "orange")
print(b)  # ['apple', 'orange', 'banana', 'cherry']

# Extend List
print('\nExtend List')
c = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
c.extend(tropical)
print(c)  # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Extend List with Tuple
print('\nExtend List with Tuple')
d = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
d.extend(thistuple)
print(d)  # ['apple', 'banana', 'cherry', 'kiwi', 'orange']