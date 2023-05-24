import requests, json
from bs4 import BeautifulSoup

url = "https://www.atlasdasaude.pt/doencasAaZ"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

divs = soup.find_all("div", class_="views-row")

lista=[]
for div in divs:
    title = div.div.h3.a.text
    #print(div, end="\n\n")
    des = div.find("div", class_="field-content").text
    lista.append({title.strip():des.strip()})

file = open("doencas.json", "w", encoding="utf-8")
json.dump(lista, file, ensure_ascii=False, indent=4)
file.close()