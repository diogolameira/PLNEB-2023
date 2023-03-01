#AULA 1

from collections import Counter

#1 Print em maiúsculas
nome=input("Nome: ")
print(nome.upper())


#2 Recebe array e imprime pares
x = input("Números: ")

def pares(x):
    y = x.split(" ")
    lista=[]
    for i in y:
        if int(i) % 2 == 0:
            lista.append(i)
    print(lista)
pares(x)


#3 Recebe ficheiro e imprime linhas do ficheiro em ordem inversa
ficheiro = input("Nome do ficheiro ou path: ")

def linhas(ficheiro):
    x = list(open(ficheiro))
    print(x[::-1])

linhas(ficheiro)


#4 Recebe nome de ficheiro e imprime número de ocorrências das 10 palavras mais frequentes no ficheiro
def palavrasfrequentes():
    nome = input("Nome do ficheiro: ")
    ficheiro = open(nome, 'r')
    palavras = ficheiro.read().split()
    contagem = Counter(palavras)
    for palavra, cont in contagem.most_common(10):
        print(f"{palavra}: {cont}")

palavrasfrequentes()


#5 Função que recebe um texto como argumento e o ”limpa”: separa palavras e pontuação com espaços, converte para minúsculas, remove acentuação de caracteres, etc
def limpar_texto(texto):
    # Lista de caracteres especiais e pontuação
    acentos = "àáâãäèéêëìíîïòóôõöøùúûü"
    pontuacao = "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~£§€"

    # Converter para minúsculas e remover acentuação
    texto = texto.lower()
    for char in acentos:
        if char in "àáâãä":
            texto = texto.replace(char, 'a')
        elif char in "èéêë":
            texto = texto.replace(char, 'e')
        elif char in "ìíîï":
            texto = texto.replace(char, 'i')
        elif char in "òóôõöø":
            texto = texto.replace(char, 'o')
        elif char in "ùúûü":
            texto = texto.replace(char, 'u')

    # Substituir pontuação por espaços
    for char in pontuacao:
        texto = texto.replace(char, ' ')

    # Remover espaços extras
    texto = ' '.join(texto.split())

    print("Texto limpo:", texto)

limpar_texto("Olá!!€  túdo?? bEm")







