import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    # Esta função recebe um parâmetro, inicializa variável 
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False

    # Definindo a variável para contar a quantidade de jogadas
    erros = 0

    # Enquanto não enforcou e ainda não acertou
    # Enquanto (true e true)
    while(not enforcou and not acertou):
        
        chute = pede_chute()

        # Marcando as letras
        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            # Incrementando a variavel
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7

        # Redefinindo a variável = se tiver "_" signfica que ainda não acertou
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

# Isolando funções, melhorando a legibilidade do código:

def imprime_mensagem_abertura():
    print("**********************************")
    print("***Bem vindo ao jogo da Forca!!***")
    print("**********************************")
    print(end="\n")

def carrega_palavra_secreta():
    # Utilizando o arquivo para escolher as frutas aleatoriamente
    arquivo = open ("palavras.txt", "r")
    palavras = []

    # Laço para filtrar e deixar as palavras como desejamos
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    # Fechando o arquivo, boa prática!
    arquivo.close()

    # Inicializando a variável palavra_secreta, gerada randomicamente 
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    # Definindo o retorno esperado pela função
    return palavra_secreta

# Recebe parâmetro e inicializa função
def inicializa_letras_acertadas(palavra):
    # 'List comprehentions' para definir os espaços referentes às letras de cada palavra secreta 
    return ["_" for letra in palavra]

def pede_chute():
    # Declarando as variáveis para utilizar no laço 
    chute = input("Qual letra? ")
    # Tratando a informação enviada pelo jogador, retira todos os espaços e deixa em maiúsculo
    chute = chute.strip().upper()
    return chute 

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0

    for letra in palavra_secreta:
        # Comparação indiferente da letra ser maiúscula ou minúscula
        if (chute.upper() == letra.upper()):
            # Utilizando lista para mostrar ao jogador as letras acertadas
            letras_acertadas[index] = letra

        index += 1
        
# Desenhando a forca para o jogador
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

# Quando o programa for o principal, python assume a variavel __name__ 
# pode ser importado, não executa antes do tempo e quando aberto sozinho funciona!    
if(__name__== "__main__"):
    jogar()