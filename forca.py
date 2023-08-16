def jogar():
    print("**********************************")
    print("***Bem vindo ao jogo da Forca!!***")
    print("**********************************")
    print(end="\n")

    palavra_secreta = "melancia".upper()
    # 'List comprehentions' para definir os espaços referentes às letras de cada palavra secreta 
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False

    # Definindo a variável para contar a quantidade de jogadas
    erros = 0

    print(letras_acertadas)

    # Enquanto não enforcou e ainda não acertou
    # Enquanto (true e true)
    while(not enforcou and not acertou):
        # Declarando as variáveis para utilizar no laço 
        chute = input("Qual letra? ")
        # Tratando a informação enviada pelo jogador, retira todos os espaços e deixa em maiúsculo
        chute = chute.strip().upper() 

        if(chute in palavra_secreta):
            index = 0

            for letra in palavra_secreta:
                # Comparação indiferente da letra ser maiúscula ou minúscula
                if (chute.upper() == letra.upper()):
                    # Utilizando lista para mostrar ao jogador as letras acertadas
                    letras_acertadas[index] = letra

                index += 1
        else:
            # Incrementando a variavel
            erros += 1

        enforcou = erros == 6
        # Redefinindo a variável = se tiver "_" signfica que ainda não acertou
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!")
    print("Fim do Jogo")

# Quando o programa for o principal, python assume a variavel __name__ 
# importa e não executa antes do tempo, quando aberto sozinho, funciona

if(__name__== "__main__"):
    jogar()