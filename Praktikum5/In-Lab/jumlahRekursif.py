def Add(a: int, b: int) -> int: # gabisa buat pengurangan bilang negatif
    if b == 0:
        return a
    else:
        return Add (a - 1, b - 1)
# aplikasi
print(Add(10, 3))
print(Add(12, 13))


def Add2(a: int, b: int) -> int: # bisa untuk angka negatif
    if b == 0:
        return a
    elif b > 0: 
        return Add2(a + 1, b - 1)
    elif b < 0:
        return Add2(a - 1, b + 1)

# aplikasi
print(Add2(12, -13))

def fib(n): # fibonnaci
    if n==0: 
        return 0 
    elif n==1: 
        return 1
    else: 
        return fib(n - 1) + fib(n - 2)

# Aplikasi 
print(fib(4)) 
print(fib(10)) 
print(fib(0))


def factorial(n): # faktorial
    if n==0: 
        return 1 
    else: 
        return n * factorial(n - 1)
    
# Aplikasi
print(factorial(5))
print(factorial(4))