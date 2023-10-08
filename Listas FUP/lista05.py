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
'''num = int(input("digite um numero que será convertido em anos, semanas e dias:"))
anos = num // 365
semanas = num % 365 // 7
dias = num % 365 % 7
print (f"anos:{anos}, semanas: {semanas}, dias: {dias}")'''

n1 = int(input("digite um numero:"))
n2 = int(input("digite um numero:"))
n3 = int(input("digite um numero:"))
if n1 >= n2 >= n3:
    print(n1, n2, n3)
elif n1 >= n3 >= n2:
    print(n1, n3, n2)
elif n2 >= n1 >= n3:
    print(n2, n1, n3)
elif n2 >= n3 >= n1:
    print(n2, n3, n1)
elif n3 >= n1 >= n2:
    print(n3, n1, n2)
else:
    print(n3, n2, n1)