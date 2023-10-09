# Questão 01
'''n = int(input("digite um valor maior que zero: "))
for x in range(1, n):
    print("Que coisa não...")'''

# Questão 02
'''n = int(input("digite um valor:"))
for cont in range(1, n):
    print(cont)'''

# Questão 03
'''n = int(input("digite um valor:"))
soma = 0
for cont in range(1, n+1):
    soma += cont
print(soma)'''

# Questão 04
'''n = int(input("digite a quantidades de numeros que irá digitar:"))
menorValor = 0
maiorValor = 0
for cont in range(1, n+1):
   num = int(input("digite um valor inteiro:"))
   if cont == 1:
        menorValor = num
        maiorValor = num
   if num > maiorValor:
        maiorValor = num
   if num < menorValor:
        menorValor = num
print(f"o menor valor é {menorValor} e o maior é {maiorValor}")'''

# Questão 05
'''x = int(input("digite um valor:"))
n = int(input("digite um valor não negativo:"))
result = x
for cont in range(1, n):
    result *= x
print(result)'''

# Questão 06
'''n = int(input("digite um numero:"))
fatorial = n
for cont in range(1, n):
    fatorial = fatorial * cont
print(fatorial)'''
# Questão 07
'''k = int(input("digite um numero maior q zero: "))
n = int(input("digite um numero maior ou igual ao anterior: "))
fatN = n
fatK = k
fatC = n - k
for cont in range(1, n):
    fatN *= cont
for cont in range(1, k):
    fatK *= cont
for cont in range(1, n - k):
    fatC *= cont
result = fatN / (fatK * (fatC))
print(result)'''

# Questão 08
'''a = int(input("digite um numero:"))
b = int(input("digite outro numero:"))
c = a / b
print(f"{c:.0f}")'''

# Questão 09

# Questão 10
'''a = int(input("digite um valor: "))
b = int(input("digite um valor: "))
while b != 0:
    resto = a % b
    a = b
    b = resto
print(f"o mdc é {a}")'''

# Questão 11
'''mult = 1
a = 1
for cont in range(1, 10):
    for cont in range(1, 10):
        print(f"{cont}x{a} = {cont * a}")
    print("=========================================")
    a += 1'''

# Questão 12
'''n = int(input("digite um numero para saber se é número perfeito: "))
soma = 0
for cont in range(1, n):
    if n % cont == 0:
        soma += cont
if soma == n:
    print("O número é perfeito!")
else:
    print("O número é imperfeito :/")
    print(soma)'''

# Questão 13
'''for cont in range(1000, 2000):
    if cont % 11 == 5:
        print(f"{cont} % {11} = 5")'''

# Questão 14
'''soma = 1
for cont in range(1, 65):
    soma += (soma * 2)
print(soma)'''

# Questão 15
'''for cont in range(1000, 9999):
    num = cont
    first = num // 100
    last = num % 100
    soma = first + last
    quad = soma**2
    if quad == cont:
        print(f"{first} + {last} = {soma}")
        print(f"{soma}**2 = {quad}")
        print("===============")'''
