# ativide_cloud

Importação da biblioteca unidecode que foi usada para remover os acentos do texto
- from unidecode import unidecode

Para ler o arquivo foi utilizado o código: 
- with open("jackson.txt", "r") as texto:
-   conteudo = texto.read()

Para realizar a limpeza do texto, uma nova variável foi criada "texto_sem_acentos" e armazenados na variavel "conteudo_limpo"
- texto_sem_acentos = conteudo.replace(",", "").replace(";", "").replace(".", "")
- conteudo_limpo = unidecode(texto_sem_acentos)

O código abaixo descreve como foi feita a contagem das palavras e a organização das mesmas em ordem descrescente
- palavras = texto_sem_acentos.split()
- frequencia = {}
- for palavra in palavras:
-    if palavra in frequencia: 
-        frequencia[palavra] += 1
-    else:
-        frequencia[palavra] = 1
- palavras_ordenadas = sorted(frequencia, key=frequencia.get, reverse=True)

O menu foi criado para que o usúrio possa escolher uma das opções e seguir para a execução
- menu = input('''Escolha uma das opções abaixo:
-     1 - Retire os acentos e exiba o texto reescrito.
-     2 - Realize a contagem das palavras (que deverão ser ranqueadas em forma decrescente).
-     3 - Permita ao usuário saber qual(is) palavra(s) que e quantas aparições de cada uma.
-     4 - Exibir a com mais aparição e a com menos aparição.
-     0 - Sair do programa
-     Desejo a opção: ''')


E o tratamento das opções escolhidas pelo usuário
- if (menu == '2' or menu == '3' or menu == '4') and not texto_limpo:
-     input("Não é possivel escolher essa opção agora, tente outra: ")
- elif menu == '1':
-     # Limpar o conteudo
- elif(menu == '3' or menu == '4') and not funcao:
-     input("Não é possivel escolher essa opção agora, tente outra")
- elif menu == '2':
-     # Realize a contagem das palavras (que deverão ser ranqueadas em forma decrescente).
- elif menu == '3':
