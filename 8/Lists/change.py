# Change List Items

# Change Single Item
print('\nChange Single Item')
a = ["apple", "banana", "cherry"]
a[1] = "blackcurrant"
print(a)  # ['apple', 'blackcurrant', 'cherry']

# Change Range of Items
print('\nChange Range of Items')
b = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
b[1:3] = ["blackcurrant", "watermelon"]
print(b)  # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# Replace One Item with Multiple Items
print('\nReplace One Item with Multiple Items')
c = ["apple", "banana", "cherry"]
c[1:2] = ["blackcurrant", "watermelon"]
print(c)  # ['apple', 'blackcurrant', 'watermelon', 'cherry']