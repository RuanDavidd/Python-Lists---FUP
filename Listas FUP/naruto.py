# Boa tarde!

quantDeVezes = int(input("digite quantas vezes você quer que seja testado as corridas:"))
c = 1
while c <= quantDeVezes:
    c += 1
    narutoPosicao = int(input("digite a posição inicial de naruto:"))
    sasukePosicao = int(input("digite a posição inicial de sasuke"))
    narutoSpeed = int(input("digite a valocidade de naruto:"))
    sasukeSpeed = int(input("digite a velocidade de sasuke:"))

    while narutoPosicao < sasukePosicao and narutoSpeed > sasukeSpeed:
        narutoPosicao += narutoSpeed
        sasukePosicao += sasukeSpeed
        print(narutoPosicao)
        print(sasukePosicao)

    if narutoPosicao >= sasukePosicao:
        print(f"Naruto chegou até sasuke na posição {narutoPosicao}")
    else:
        print("Oh, Não! Sasuke Chegou no Esconderijo do Orochimaru")
