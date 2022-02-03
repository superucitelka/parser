# https://realpython.com/beautiful-soup-web-scraper-python/
# Modul requests (pip install requests)
import requests
# Import knihovny BeautifulSoup4 (pip install beautifulsoup4), která usnadňuje web scraping
from bs4 import BeautifulSoup

# Konstanta obsahující adresu webu, z něhož chceme získávat data
# Žebříček 250 nejlépe hodnocených filmů podle serveru imdb.com
URL = 'https://www.imdb.com/chart/top'

# Odeslání požadavku metodou get na určenou URL adresu - HTTP server vrací zpět obsah stránky
page = requests.get(URL)
# Vytvoření objektu parseru stránky
soup = BeautifulSoup(page.content, 'html.parser')
# Získání názvů filmů z žebříčku pomocí vhodně zvoleného selektoru (td.titleColumn>a)
titles = soup.select('td.titleColumn>a')
# Získání roků vzniku filmů
years = soup.select('td.titleColumn>span')
# Kontrolní výpis získaných údajů
for i in range(0, len(titles)):
    print(f'{i + 1}. {titles[i].text} {years[i].text}')