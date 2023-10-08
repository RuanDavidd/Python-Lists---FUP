# Questão 01
#print('Consegui faZer meu primeiro ProgRaminhAa')

# Questão 02
"""real = float(input("Quanto dinheiro você tem? R$:"))
dolar = real / 3.92
print(f"você compra US${dolar:.2f} com RS${real:.2f}")"""
import math

# Questão 03
"""a = int(input('Digite o tamanho de um lado do retângulo:'))
b = int(input('Digite o tamanho do outro lado do retângulo:'))
area = (a*b)
perimetro = 2*a + 2*b
print(f'A área do retângulo é {area} e o Perímetro é {perimetro}')
print(a+b)"""

# Questão 04
"""num = int(input("digite um numero inteiro: "))
print(f"O antecessor de {num} é {num - 1}")
print(f"O sucessor de {num} é {num + 1}")"""

# Questão 05
"""quad = int(input("Digite o tamanho de um lado de um quadrado:"))
print(f"A área deste quadrado é {quad * quad} metros quadrados")"""

# Questão 06
"""r = int(input('digite o valor do raio:'))
volume = 4 * math.pi * r**3/3
area = 4 * math.pi * r**2
print(f"o volume da esfera é {volume:.2f}")
print(f"e a area de sua superficie é {area:.2f}")"""

# Questão 07
"""num = float(input('Digite um numero inteiro:'))
print(f"o quadrado deste numero é {num * num:.2f}")"""

# Questão 08
'''f = int(input("digite uma temperatura em Fahrenheit para transformar em Celsius: "))
c = (f - 32) * 5/9
print(c)'''

# Questão 09
'''km = int(input("digite uma velocidade em km/h:"))
m = km / 3.6
print(f"a velocidade em metros é {m:.2f}m/s ")'''

# Questão 10
'''graus = int(input("digite um angulo em graus:"))
radianos = graus * 3.14 / 180
print(f"o {graus} em radianos é {radianos:.4f}")'''

# Questão 11
'''v1 = int(input("digite o primeiro valor:"))
v2 = int(input("digite o segundo valor:"))
v3 = int(input("digite o terceiro valor:"))
somadosquad = (v1**2 + v2**2 + v3**2)
quaddasoma = (v1 + v2 + v3)**2
print(f"A soma dos quadrados é {somadosquad} e o quadrado da soma é {quaddasoma}")'''

# Questão 12
'''salario = float(input("Digite o salario:"))
aumento = salario * 1.2137
print(f"o salario aumentado em 21.37% é {aumento:.2f}")'''

# Questão 13
'''total = float(input("Digite um valor para ser dividido:"))
pessoa1 = total * 0.46
pessoa2 = total * 0.32
pessoa3 = total * 0.22
print(f"os valores serão: {pessoa1:.2f}, {pessoa2:.2f} e {pessoa3:.2f}")'''

# Questão 14
'''num = int(input("digite um numero de 3 digitos:"))
numinv1 = num % 10
num = num // 10
numinv2 = num % 10
num = num // 10
numinv3 = num % 10
print(numinv1, numinv2, numinv3)'''

# Questão 15
''''num = int(input("digite um numero de 4 digitos:"))
num4 = num % 10
num = num // 10
num3 = num % 10
num = num // 10
num2 = num % 10
num = num // 10
num1 = num
print(num1)
print(num2)
print(num3)
print(num4)'''

# Questão 16
'''totalDeSeg = int(input("digite um numero inteiro positivo:"))
horas = totalDeSeg//60//60
minutos = totalDeSeg//60%60
segundos = totalDeSeg%60
print(f"{horas}:{minutos}:{segundos}")'''

# Questão 17
'''x = int(input("digite o valor de x:"))
y = int(input("digite o valor de y:"))
result = float((x**2 + y**2))**0.5
print(f"{result:.2f}")'''

# Questão 18
aposta1 = int(input("digite o primeiro valor da aposta:"))
aposta2 = int(input("digite o segundo valor:"))
aposta3 = int(input("digite o terceiro valor:"))
apostaTotal = aposta1 + aposta2 + aposta3
premio = 500
ganho1 = (aposta1 / apostaTotal) * premio
ganho2 = (aposta2 / apostaTotal) * premio
ganho3 = (aposta3 / apostaTotal) * premio
print(ganho1, ganho2, ganho3)

