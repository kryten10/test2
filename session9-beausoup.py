from bs4 import BeautifulSoup
from urllib.request import urlopen
my_address = "https://www.bbc.co.uk/news"
html_page = urlopen(my_address)
html_text = html_page.read().decode('utf-8')
my_soup = BeautifulSoup(html_text, "html.parser")
for tag in my_soup.find_all("img"):
    if
print(my_soup.find_all('img src'))