import os, requests
from bs4 import BeautifulSoup

url = requests.get("https://meusitetc.netlify.app/")
html = url.content

site = BeautifulSoup(html, "html.parser")

footer = site.find('div', attrs={'class': 'box_1'})

if footer:
    t2 = footer.find('h2')
    resp = t2.text
    print(resp)

else:
    print("A id nao foi encontrada")

os.system("pause")