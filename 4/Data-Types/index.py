# string
print('String')
a = "Hello World"
print(a)  # Hello World

# int
print('\nInt')
b = 20
print(b)  # 20

# float
print('\nFloat')
c = 20.5
print(c)  # 20.5

# complex
print('\nComplex')
d = 1j
print(d)  # 1j

# list
print('\nList')
e = ["apple", "banana", "cherry"]
print(e)  # ['apple', 'banana', 'cherry']

# tuple
print('\nTuple')
f = ("apple", "banana", "cherry")
print(f)  # ('apple', 'banana', 'cherry')

# range
print('\nRange')
g = range(6)
print(g)  # range(0, 6)

# dict
print('\nDict')
h = {"name": "John", "age": 36}
print(h)  # {'name': 'John', 'age': 36}

# set
print('\nSet')
i = {"apple", "banana", "cherry"}
print(i)  # {'apple', 'banana', 'cherry'} (order may vary)

# frozenset
print('\nFrozenset')
j = frozenset({"apple", "banana", "cherry"})
print(j)  # frozenset({'apple', 'banana', 'cherry'}) (order may vary)

# bool
print('\nBool')
k = True
print(k)  # True

# bytes
print('\nBytes')
l = b"Hello"
print(l)  # b'Hello'

# bytearray
print('\nBytearray')
m = bytearray(5)
print(m)  # bytearray(b'\x00\x00\x00\x00\x00')

# memoryview
print('\nMemoryview')
n = memoryview(bytes(5))
print(n)  # <memory at 0x...> (address varies)

# NoneType
print('\nNoneType')
o = None
print(o)  # None