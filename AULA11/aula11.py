import requests, json
from bs4 import BeautifulSoup

def extractDiseasePage(url):
    page_html = requests.get(url).text
    page_soup = BeautifulSoup(page_html, "html.parser")
    page_div = page_soup.find("div", class_="field-name-body")
    res = page_div.div.div
    res.name = "page"
    res.attrs = {}
    return str(res)

def extractDiseaseListPage(div):
    des = div.find("div", class_="field-content").text
    title = div.div.h3.a.text
    return title, des


url = "https://www.atlasdasaude.pt/doencasAaZ"
url2 = "https://www.atlasdasaude.pt"

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

divs = soup.find_all("div", class_="views-summary views-summary-unformatted")

urls = []
for div in divs:
    urls.append(url2 + div.a["href"])
#print("\n\n".join(urls))

lista = []
for u in urls:
    #print(u)
    html_= requests.get(u).text
    soup_= BeautifulSoup(html_, "html.parser")

    divs = soup_.find_all("div", class_="views-row")

    for div in divs:
        page_url = url2 + div.div.h3.a["href"]
        page_info = extractDiseasePage(page_url)
        title, des = extractDiseaseListPage(div)

        lista.append({title:{"des": des, "page": page_info}})

        #print(div, end="\n\n")
        #lista.append({title.strip():des.strip()})
print(lista)
file = open("doencas.json", "w", encoding="utf-8")
json.dump(lista, file, ensure_ascii=False, indent=4)
file.close()
