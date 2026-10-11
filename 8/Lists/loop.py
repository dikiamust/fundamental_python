# Loop Lists

# Loop Through List
print('\nLoop Through List')
a = ["apple", "banana", "cherry"]
for x in a:
    print(x)
# apple
# banana
# cherry

# Loop Through Index Numbers
print('\nLoop Through Index Numbers')
b = ["apple", "banana", "cherry"]
for i in range(len(b)):
    print(b[i])
# apple
# banana
# cherry

# Loop Through List Using While
print('\nLoop Through List Using While')
c = ["apple", "banana", "cherry"]
i = 0
while i < len(c):
    print(c[i])
    i = i + 1
# apple
# banana
# cherry

# Loop Using List Comprehension
print('\nLoop Using List Comprehension')
d = ["apple", "banana", "cherry"]
[print(x) for x in d]
# apple
# banana
# cherry