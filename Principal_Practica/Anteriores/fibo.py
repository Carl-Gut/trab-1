def fib(n):
  a, b = 0, 1
  while b<n:
    print(b, end=' ')
    a, b =b, a+b
    print()

def fib2(n):
  resultado = []
  a, b = 0, 1
  while b < n:
    resultado.append(b)
    a, b =b, a+b
  return resultado

fib(50)
