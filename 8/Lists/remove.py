# Remove List Items

# Remove Item
print('\nRemove Item')
a = ["apple", "banana", "cherry"]
a.remove("banana")
print(a)  # ['apple', 'cherry']

# Remove First Matching Item
print('\nRemove First Matching Item')
b = ["apple", "banana", "cherry", "banana", "kiwi"]
b.remove("banana")
print(b)  # ['apple', 'cherry', 'banana', 'kiwi']

# Remove Item Using pop(index)
print('\nRemove Item Using pop(index)')
c = ["apple", "banana", "cherry"]
c.pop(1)
print(c)  # ['apple', 'cherry']

# Remove Last Item Using pop()
print('\nRemove Last Item Using pop()')
d = ["apple", "banana", "cherry"]
d.pop()
print(d)  # ['apple', 'banana']

# Delete Item Using del
print('\nDelete Item Using del')
e = ["apple", "banana", "cherry"]
del e[0]
print(e)  # ['banana', 'cherry']

# Delete Entire List
print('\nDelete Entire List')
f = ["apple", "banana", "cherry"]
del f
print(f)  # NameError: name 'f' is not defined