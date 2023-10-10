# Questão 9
'''c = 0
maior = 0
menor = 0
while c < 10:
    num = int(input("digite um numero:"))
    if c == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    c += 1
print(f"o maior é {maior} e o menor é {menor}")'''

#faça um programa q recebe um numero e devolva em uma letra equivalente no alfabeto
'''letras = ["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
num = int(input("digite um numero:"))
if 1 <= num <= 26:
    print(f"o numero {num} equivale a letra {letras [num - 1]}")
else:
    print("digite um valor dentro de 26")'''

# Questão 10
'''n = int(input("digite um numero: "))
imp = 1
for cont in range(1, n+1):
    print(f"{imp} é ímpar")
    imp += 2'''

# Questão 11
'''cont = 0
soma = 0
par = 0
while cont < 50:
    par += 2
    soma += par
    cont += 1
print(soma)'''

# Questão 12
'''n = int(input("digite um valor maior que zero: "))
cont = 1
fat = n
while cont < n:
    fat *= cont
    cont += 1
print(f"o fatorial de {n} é {fat}")'''

# Questão 13
'''n = int(input("digite um numero:"))
cont = 1
while cont <= n:
    if (n % cont) == 0:
        print(f"{cont} é divisor de {n}")
    cont += 1'''

# Questão 14
'''n = int(input("digite um valor maior que zero:"))
div = 0
cont = 1
while cont <= n:
    if (n % cont) == 0:
        div += 1
    cont += 1
if div == 2:
    print(f"O número {n} é primo")
else:
    print(f"{n} não é primo")
print(div)'''
