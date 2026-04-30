def pangkatRekursif (a, b):
    if b == 0:
        return 1
    else:
        return a * pangkatRekursif(a, b-1)
    
print(pangkatRekursif(2, 3))