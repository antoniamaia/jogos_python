# Importando outras bibliotecas
import random  

# Modularizando 
def jogar():
    # Apenas estético - iniciando o jogo
    print("**********************************")
    print("Bem vindo ao jogo de Adivinhação!!")
    print("**********************************")
    print(end="\n")


    # Atribuindo valor ao número que será adivinhado, randomicamente sempre que o jogo reinicia
    numero_secreto = random.randrange(1,101)

    # Atribuindo à variavel o total de tentativas (laço)
    total_de_tentativas = 0
    pontos = 1000

    # Mudando a dificuldade do jogo de acordo com os níveis (número de tentativas)
    print("Qual nível de dificuldade?")
    print("(1) Fácil  (2) Médio  (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5



    for rodada in range(1, total_de_tentativas + 1):
        # Mostra ao usuário quantas vezes ainda pode jogar  + função format(string interpolation)
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        # Função input - recebe o número do usuário, retorna uma string
        chute_str = input("Digite um número entre 1 e 100: ") 

        # Mostra ao usuário o número digitado
        print("Você digitou", chute_str) 

        # Utilizando a função int() para converter a string recebida no input
        chute = int(chute_str)

        # Verificando se o input é válido, dentro do solicitado (1,100)
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        # Atribuindo valores as variáveis - melhorando a legibilidade do código
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        # Verificação (jogo) se a numeração inserida é igual ao número secreto (type -> boolean)
        if (acertou):
            print("Você acertou e fez {} pontos!!".format(pontos))
            break                  #quebra o laço se o jogador acerta e finaliza o jogo
        else:
            # Definindo a pontuação do jogo - função abs() desconsidera números negativos
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}, você fez {} pontos".format(numero_secreto,pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}, você fez {} pontos".format(numero_secreto,pontos))
        

    print("Fim do Jogo")

# Chamando a função para jogar somente adivinhação
if(__name__== "__main__"):
    jogar()