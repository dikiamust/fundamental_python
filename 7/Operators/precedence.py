# Precedence Order

# ()
print('\nParentheses ()')
a = (2 + 3) * 4
print(a)  # 20

# **
print('\nExponentiation (**)')
b = 2 ** 3
print(b)  # 8

# +x -x ~x
print('\nUnary Plus, Unary Minus, and Bitwise NOT')
c = +5
print(c)  # 5

d = -5
print(d)  # -5

e = ~5
print(e)  # -6

# * / // %
print('\nMultiplication, Division, Floor Division, and Modulus')
f = 4 * 3
print(f)  # 12

g = 10 / 2
print(g)  # 5.0

h = 10 // 3
print(h)  # 3

i = 10 % 3
print(i)  # 1

# + -
print('\nAddition and Subtraction')
j = 5 + 3
print(j)  # 8

k = 5 - 3
print(k)  # 2

# << >>
print('\nBitwise Left and Right Shifts')
l = 5 << 1
print(l)  # 10

m = 8 >> 1
print(m)  # 4

# &
print('\nBitwise AND (&)')
n = 5 & 3
print(n)  # 1

# ^
print('\nBitwise XOR (^)')
o = 5 ^ 3
print(o)  # 6

# |
print('\nBitwise OR (|)')
p = 5 | 3
print(p)  # 7