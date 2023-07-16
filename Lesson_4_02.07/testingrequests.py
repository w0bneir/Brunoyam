import requests
from bs4 import BeautifulSoup
response = requests.get("https://lenta.ru/rss/top7")
with open("Lenta.ru.txt", "w") as file:
    file.write("Заголовки новостей \n")
# print(response.status_code)
# print(response.text)
def pars(text):
    soup = BeautifulSoup(text,"html")
    title = soup.find_all("title")
    for i in title:
        if i.getText() != "Lenta.ru":
            a = i.getText()
            with open("Lenta.ru.txt", "a") as file:
                file.write(a + '\n')
pars(response.text)
