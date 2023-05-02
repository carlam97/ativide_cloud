from unidecode import unidecode

with open("jackson.txt", "r") as texto:
    conteudo = texto.read()
print(f"O texto original é",{conteudo})

texto_limpo = False

pergunta_global = 1
while pergunta_global != '0':

    menu = input('''
        Escolha uma das opções abaixo:

        1 - Retire os acentos e exiba o texto reescrito.
        2 - Realize a contagem das palavras (que deverão ser ranqueadas em forma decrescente).
        3 - Permita ao usuário saber qual(is) palavra(s) que e quantas aparições de cada uma.
        4 - Exibir a com mais aparição e a com menos aparição.
        0 - Sair do programa

        Desejo a opção: 
        '''
    )

    palavrass = []
    quantidade = []
    numeros = []
    numeross = []
    lista_menor = []
    lista_maior = []


    if (menu == '2' or menu == '3' or menu == '4') and not texto_limpo:
       input("Não é possivel escolher essa opção agora, tente outra: ")

    # Limpar o conteudo
    if menu == '1':
        texto_sem_acentos = unidecode(conteudo)
        print(f"O texto limpo é: ",texto_sem_acentos)
        texto_limpo = True

    # Realize a contagem das palavras (que deverão ser ranqueadas em forma decrescente).
    elif menu == '2':
        palavras = texto_sem_acentos.split()

        frequencia = {}
        for palavra in palavras:
            if palavra in frequencia: 
                frequencia[palavra] += 1
            else:
                frequencia[palavra] = 1

        palavras_ordenadas = sorted(frequencia, key=frequencia.get, reverse=True)

        print("O texto possui", len(palavras), "palavras")
        print("Palavras ranqueadas de forma decrescente")
        for palavra in palavras_ordenadas:
            print(palavra, ":", frequencia[palavra])

    # Permita ao usuário saber qual(is) palavra(s) que e quantas aparições de cada uma
    elif menu == '3':
        #palavrass = []
        #quantidade = []

        for palavra in palavras_ordenadas:
            palavrass.append(palavra)
            quantidade.append(frequencia[palavra])


        while True: 
            pergunta = str(input("Qual palavra você deseja: "))

            if not pergunta:
                print("Saindo...")
                break

            elif pergunta in palavrass:
                print(f"A palavra {pergunta} apareceu {quantidade[palavrass.index(pergunta)]} vezes no texto")

            else: 
                input(print(f"A palvra {pergunta} não está presente no texto"))


    # Exibir a com mais aparição e a com menos aparição
    elif menu == '4':
        #numeros = []
        #numeross = []
        #lista_menor = []
        #lista_maior = []

        palavra_menos_frequente = min(quantidade)
        palavra_mais_frequente = max(quantidade)


        for i, numero in enumerate(quantidade):
            if numero == palavra_menos_frequente:
                numeros.append(i)
            else:
                numero == palavra_mais_frequente
                numeross.append(i)

        for x in numeros:
            lista_menor.append(palavrass[x])

        for y in numeross:
            lista_maior.append(palavrass[y])

        print(lista_menor)
        print(lista_maior)

    elif menu == '0':
        pergunta_global = '0'
    
    else:
        input("Esse valor não está dentro do menu, tente novamente com um dos valores abaixo: ")
