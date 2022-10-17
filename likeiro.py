# Curtir fotos e videos no feed do Instagram, Facebook, Twitter e LinkedIn.
# Fazer as mudanças necessárias de acordo com a rede social preferida.

# Importando as bibliotecas necessárias.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

__version__ = "0.0.0.1"

class likeiro:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--lang=pt-BR")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(
            executable_path=r"./chromedriver.exe", options=chrome_options
        )
        self.driver.set_window_size(450, 768)
        self.wait = WebDriverWait()

test = likeiro()
test.start()
