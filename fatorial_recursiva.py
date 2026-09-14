def fatorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

n = int(input("Informe um número: "))

while n < 0:
    print("ERRO: informe um número positivo")
    n = int(input("Informe um número: "))

print(f"{n}! = {fatorial(n)}")