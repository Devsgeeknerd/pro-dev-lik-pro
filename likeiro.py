# Curtir fotos e videos no feed do Instagram, Facebook, Twitter e LinkedIn.
# Fazer as mudanças necessárias de acordo com a rede social preferida.

# Importando as bibliotecas necessárias.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

__version__ = "0.0.0.1"

class likeiro:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--lang=pt-BR")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-notifications")
