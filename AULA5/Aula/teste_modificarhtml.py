#Testar com apenas parte do json e html

import json
import re

with open("testejson.json", encoding="utf-8") as file:
    dicionario = json.load(file)

termos = dicionario.keys()

with open("testehtml.html", "r", encoding="utf-8") as file1:
    texto = file1.read()
    linhas = texto.splitlines()

#AULA

blacklist = ["e", "de", "são"]
#blacklist = {"e", "de", "são"}

new_list = [designacao for designacao in termos if designacao not in blacklist]
#new_list = termos - blacklist


expressao = r"\b(" + "|".join(termos) + r")\b"
#print(expressao)


def anotaTermo(termo):
    termo = termo[1]
    res = "<a data-toggle='tooltip' href='' title='"+dicionario.get(termo)+"'>"+termo+"</a>"
    return res

res = re.sub(expressao, anotaTermo, texto)
print(expressao)


texto = ""

for linha in linhas:
    palavras = re.sub(r"<.+?>", "", linha) #retirar as tags
    #palavras = re.findall(r"\b.+?\b", palavras) #isolar cada palavra
    palavras = re.findall(r"\b[\w-]+\b", palavras)
    print(palavras)
    for palavra in palavras:
        palavra = palavra.lower()
        if palavra in termos:
            linha = re.sub(expressao, anotaTermo, linha)
            #linha = re.sub(palavra, f"<a href title='{dicionario.get(palavra)}'>{palavra}</a>", linha)
    texto += linha + "\n"


with open("teste2html.html", "w", encoding="utf-8") as file1:
    file1.write(texto)