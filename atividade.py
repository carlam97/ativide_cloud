from unidecode import unidecode

with open("jackson.txt", "r") as texto:
    conteudo = texto.read()
print(f"O texto original é",{conteudo})

texto_limpo = False
funcao = False

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


    if (menu == '2' or menu == '3' or menu == '4') and not texto_limpo:
       input("Não é possivel escolher essa opção agora, tente outra: ")

    # Limpar o conteudo
    elif menu == '1':

        texto_sem_acentos = conteudo.replace(",", "").replace(";", "").replace(".", "")
        conteudo_limpo = unidecode(texto_sem_acentos)
        print("Texto Limpo: ")
        print()
        print(conteudo_limpo)

        texto_limpo = True

    elif(menu == '3' or menu == '4') and not funcao:

        input("Não é possivel escolher essa opção agora, tente outra")

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
            palavrass.append(palavra)
            quantidade.append(frequencia[palavra])

        funcao = True

    # Permita ao usuário saber qual(is) palavra(s) que e quantas aparições de cada uma
    elif menu == '3':

        while True: 
            print()
            pergunta = str(input("Qual palavra você deseja?: "))

            if not pergunta:
                print("Saindo...")
                break

            elif pergunta in palavrass:
                print(f"A palavra {pergunta} apareceu {quantidade[palavrass.index(pergunta)]} vezes no texto")

            else: 
                input(print(f"A palvra {pergunta} não está presente no texto, digite outra palavra"))


    # Exibir a com mais aparição e a com menos aparição
    elif menu == '4':

        numero_menos_frequente = min(quantidade)
        
        for i, numero in enumerate(quantidade):
            if numero == numero_menos_frequente:
                numeros.append(i)

        print(numeros)

        for x in numeros:
           lista_menores_valores.append(palavrass[x])

        print()
        print("Lista das palavras que menos aparecem: ")
        print()
        print(lista_menores_valores)

        numero_mais_frequente = max(quantidade)

        for en, number in enumerate(quantidade):
            if number == numero_mais_frequente:
                numeros1.append(en)
        
        for y in numeros1:
            lista_maiores_valores.append(palavrass[y])

        print()
        print("Lista das palavras que mais aparecem: ")
        print()
        print(lista_maiores_valores)


        if pergunta_p == '0':
            print()
            print("saindo do programa...............")
            print()
            pergunta_global = '0'
    
        else:
            print()
            input("Esse não é um numero disponível, tente outro... ")
            print()
