#Testar com apenas parte do json e html

import json
import re

with open("testejson.json", encoding="utf-8") as file:
    dicionario = json.load(file)

termos = dicionario.keys()

with open("testehtml.html", "r", encoding="utf-8") as file1:
    texto = file1.read()
    linhas = texto.splitlines()

texto = ""

for linha in linhas:
    palavras = re.sub(r"<.+?>", " ", linha) #retirar as tags
    palavras = re.findall(r"\b.+?\b", palavras) #isolar cada palavra
    for palavra in palavras:
        palavra = palavra.lower()
        if palavra in termos:
            linha = re.sub(palavra, f"<a href title='{dicionario.get(palavra)}'>{palavra}</a>", linha)
    texto += linha + "\n"

with open("testehtml.html", "w", encoding="utf-8") as file1:
    file1.write(texto)
