import requests as requests
from bs4 import BeautifulSoup
import os

url = "https://www.gov.br/infraestrutura/pt-br/assuntos/transito/conteudo-Senatran/resolucoes-contran"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# links = soup.find_all('div', attrs={"id": "parent-fieldname-text"})
links = soup.find_all('a')

i = 0
for link in links:
    if '.doc' in link.get('href', []):
        print(link)
        i += 1
        print("Downloading file: ", i)
        response = requests.get(link.get('href'))
        pdf = open("doc" + str(i) + ".doc", 'wb')
        pdf.write(response.content)
        pdf.close()
        print("File ", i, " downloaded")



