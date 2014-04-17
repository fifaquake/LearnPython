from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
c = a * b
print(c.numerator)
print(c.denominator)
print(c)
print(float(c))
print(c.limit_denominator(8))

x = 3.75
print(type(x.as_integer_ratio()))

# x.as_integer_ration() returns a tuple (a, b)
# as we want use the tuple as the parameters,
# we can pass the tuple by using *(a,b)
y = Fraction(*x.as_integer_ratio())
print(y)
