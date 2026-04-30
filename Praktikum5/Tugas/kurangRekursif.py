def min(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return min(a - 1, b - 1)
    
# Aplikasi
print(min(7, 4))