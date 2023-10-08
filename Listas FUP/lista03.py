# Questão 03
'''a = int(input("digite um numero:"))
b = int(input("digite outro numero:"))
if a > b:
    print(f"{a} é maior que {b}")
elif b > a:
    print(f"{b} é maior que {a}")
else:
    print("os números são iguais")'''

# Questão 02
'''num = int(input("digite um número:"))
if num % 2 == 1:
    print(f"O número {num} é impar")
else:
    print(f"o número {num} é par")'''

# Questão 03
'''a = int(input("digite um número:"))
b = int(input("digite um número:"))
c = int(input("digite um número:"))
d = int(input("digite um número:"))
numpares = 0
if a % 2 == 0:
    numpares += a
if b % 2 == 0:
    numpares += b
if c % 2 == 0:
    numpares += c
if d % 2 == 0:
    numpares += d
if numpares == 0:
    print("foram somente números impares.")
else:
    print(f"a soma dos numeros pares é {numpares}")'''

#Questão 04
'''a = int(input("digite um valor:"))
b = int(input("digite um valor:"))
c = int(input("digite um valor:"))
if a > (b and c):
    print(f"{a} é o maior número")
elif b > (a and c):
    print(f"{b} é o maior número")
else:
    print(f"{c} é o maior número")'''

# Questão 05
'''num = int(input("Digite um número:"))
if num > 0:
    raizquad = num**0.5
    print(f"a raiz quadrada de {num} é {raizquad:.1f}")
else:
    print("Número inválido")'''

# Questão 06
'''nota1 = float(input("digite uma nota:"))
nota2 = float(input("digite uma nota:"))
nota3 = float(input("digite uma nota:"))
if 0 <= (nota1 and nota2 and nota3) <= 10:
    print(f"a média das notas é {(nota1+nota2+nota3)/3:.2f}")
else:
    print("Valores inválidos")'''

# Questão 07
'''salario = int(input("digite o seu salário:"))
emprestimo = int(input("digite o valor do emprestimo:"))
if emprestimo > (salario/5):
    print("Empréstimo não concedido")
else:
    print("Empréstimo Concedido")'''

# Questão 08
num = int(input("digite um numero:"))
if num%3 == 0 and num%5 == 0:
    print(f"{num} é divisivel pelos 2")
elif num%3 == 0:
    print(f"{num} é divisivel por 3")
elif num%5 == 0:
    print(f"{num} é divisivel por 5")
else:
    print(f"{type(num)} Não é divisel nem por 3, nem por 5")
# Questão 09
