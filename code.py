# provide code that iterates in multiples of A until X,
# then in multiples of A + 1 until 2X,
# then multiples of A + 2 until 3X
def multiples_func(x,a):
    a1 = a + 1
    x2 = 2 * x
    a2 = a + 2
    x3 = 3 * x
    a_0 = list(range(a, x, a))
    a_1 = list(range(a, x2, a1))
    a_2 = list(range(a, x3, a2))

    return a_0, a_1, a_2

# example x and a below:
y,z,b = multiples_func(20,2)
print(y)
print(z)
print(b)