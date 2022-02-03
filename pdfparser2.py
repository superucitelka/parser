# Alternativní parser PDF (pip install py-pdf-parser)
from py_pdf_parser.loaders import load_file

# Parsovaný dokument
document = load_file("presidents.pdf")

# Výběr všech elementů na určené stránce
elements = document.elements.filter_by_page(10)
# Výpis prostého textu z každého elementu
for element in elements:
    print(element.text())