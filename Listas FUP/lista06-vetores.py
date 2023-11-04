import random
# Questão 04
'''vet = []
vetQuad = []
for i in range(10):
    vet.append(random.())
    vetQuad.append(vet[i] * vet[i])
print(vet)
print(vetQuad)'''

# Questão 05
'''x = int(input("digite uma posição x <= 15:"))
y = int(input("digite um posição y <= 15:"))
vet = []
for i in range(15):
    vet.append(random.randint(0, 99))
print(vet)
print(f"a soma das posições {x} e {y} é {vet[x] + vet[y]}")'''

# Questão 06
'''vet = []
paresQuant = 0
for i in range(15):
    vet.append(random.randint(0, 99))
    if vet[i] % 2 == 0:
        paresQuant += 1
print(vet)
print(paresQuant)'''

# Questão 07
'''vet = []
for i in range(15):
    vet.append(random.randint(0, 99))
    if vet[i] % 2 == 1:
        print(f"{vet[i]} é ímpar")'''

# Questão 08
'''menor = 0
maior = 0
vet = []
for i in range(10):
    vet.append(random.randint(0, 20))
    if i == 0:
        menor = vet[i]
        maior = vet[i]
    if vet[i] < menor:
        menor = vet[i]
    if vet[i] > maior:
        maior = vet[i]
print(vet)
print(maior, menor)'''

# Questão 09
'''vet = []
for i in range(20):
    vet.append(random.randint(-10, 10))
    if vet[i] < 0:
        vet[i] = 0
print(vet)'''

# Questão 10
'''notas = []
soma = 0
for i in range(15):
    notas.append(random.randint(0, 10))
    soma += notas[i]
print(f"a média das notas é {soma/15:.2f}")'''