def kali(a: int, b: int) -> int:
    if a == 0: 
        return 0
    elif b == 0:
        return 0
    else:
        return a + kali(a, b -1)
    
print(kali(3, 2))