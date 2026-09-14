def f_recursiva(n: int) -> int:
    if n <= 1:
        return n
    else:
        return f_recursiva(n-1) + 2 * f_recursiva(n-2)

print(f_recursiva(4))