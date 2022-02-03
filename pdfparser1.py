# Připojení knihovny PyPDF2 (pip install pypdf2) pro práci s PDF soubory - použití modulu pro čtení a zápis PDF souboru
# * https://www.analyticsvidhya.com/blog/2021/09/pypdf2-library-for-working-with-pdf-files-in-python/
from PyPDF2 import PdfFileReader
# Modul requests (pip install requests)
import requests

# Funkce provede překlad s využitím experimentálního online překladače vyvíjeného na MFF CVUT: https://lindat.mff.cuni.cz/services/translation/
def translate(text='', src='en', tgt='cs'):
    '''
    :param text: text, který chceme přeložit
    :param src: jazyk zdroje (výchozí 'en' = angličtina)
    :param tgt: cílový jazyk (výchozí 'cs' = čeština)
    :return: přeložený text zbavený nadbytečných prázdných řádků
    '''
    # URL adresa, pomocí níž zasíláme požadavek na API překladače (viz https://lindat.mff.cuni.cz/services/translation/api/v2/doc)
    apiurl = f'https://lindat.mff.cuni.cz/services/translation/api/v2/languages/?src={src}&tgt={tgt}'
    # Nezbytné hlavičky požadavku
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    # Zasílaná data pro překladač
    data = {'input_text': text}
    # Odpověď je zaslána ve formátu JSON - rozdělena na samostatná souvětí
    res = requests.post(apiurl, data=data, headers=headers)
    result = ''
    # Rozparsování JSON dat z podoby Python list (samostatné věty) a jejich uložení do stringové proměnné result
    for sentence in res.json():
        result += sentence + ' '
    return result

# Načtení PDF souboru
pdf = PdfFileReader('presidents.pdf')
# Výpis počtu stránek dokumentu
print(f'Počet stran: {pdf.getNumPages()}')
# Výběr prostého textu z určené stránky
text = pdf.getPage(20).extractText()
# Překlad textu zadané stránky a uložení do proměnné page
page = translate(text=text.replace('\n', ' '))

# Uloženíí obsahu proměnné do textového souboru
with open('president.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(page)