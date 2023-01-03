import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(0,101)
    total_de_tentativas = 0
    pontos = 1000

    while(True):
        print('Qual a dificuldade!!!')
        print('Nivel 1 \nNivel 2 \nNivel 3')

        nivel = int(input('Digitel o nivel desejado: '))

        if nivel == 1:
            total_de_tentativas = 20
            break
        elif nivel == 2: 
            total_de_tentativas = 10
            break
        elif nivel == 3:
            total_de_tentativas = 5
            break
        else:
            print('Digite um nivel valido')

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa", rodada, "de", total_de_tentativas)
        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdido = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdido

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()