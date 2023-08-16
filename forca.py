def jogar():
    print("**********************************")
    print("***Bem vindo ao jogo da Forca!!***")
    print("**********************************")
    print(end="\n")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    # Enquanto não enforcou e ainda não acertou
    # Enquanto (true e true)
    while( not enforcou and not acertou):
        # Declarando as variáveis para utilizar no laço 
        chute = input("Qual letra? ")
        chute = chute.strip() # Tratando a informação enviada pelo jogador, retira todos os espaços

        index = 0

        for letra in palavra_secreta:
            # Comparação indiferente da letra ser maiúscula ou minúscula
            if (chute.upper() == letra.upper()):
                # Utilizando lista para mostrar ao jogador as letras acertadas
                letras_acertadas[index] = letra
                

            index = index + 1


        print(letras_acertadas)

    print("Fim do Jogo")

# Quando o programa for o principal, python assume a variavel __name__ 
# importa e não executa antes do tempo, quando aberto sozinho, funciona

if(__name__== "__main__"):
    jogar()