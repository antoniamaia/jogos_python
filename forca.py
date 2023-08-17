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

        enforcou = erros == 6

        # Redefinindo a variável = se tiver "_" signfica que ainda não acertou
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

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

def imprime_mensagem_vencedor():
    print("Você ganhou!!")

def imprime_mensagem_perdedor():
    print("Você perdeu! :(")

# Quando o programa for o principal, python assume a variavel __name__ 
# pode ser importado, não executa antes do tempo e quando aberto sozinho funciona!    
if(__name__== "__main__"):
    jogar()