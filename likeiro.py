# Curtir fotos e videos no feed do Instagram, Facebook, Twitter e LinkedIn.
# Fazer as mudanças necessárias de acordo com a rede social preferida.

# Importando as bibliotecas necessárias.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
import random
import time
import getpass
import os

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
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=12,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
            ]
        )

    def data_input(self):
        self.user = str(input("Usuário: "))
        self.valid_information = True
        try:
            while self.valid_information == False:
                self.data_input()
            if self.user == " ":
                print("Usuário não encontrado!")
                self.data_input()
            self.password = getpass.getpass(
                prompt="senha: ", stream=None
            )
            self.likes = int(input("Quantos likes você deseja? "))
        except ValueError:
            print("Dados inválidos")

    def home(self):
        self.driver.get("https://www.instagram.com/")
        self.login(self.user, self.password)
        self.notice()
        self.like(self.likes)
        self.opinion()

    def login(self, user, password):
        try:
            user = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//input[@name='username']")))
            user.click()
            time.sleep(3)

            for letter in user:
                user.send_keys(letter)
                time.sleep(random.randint(1, 9) / 60)

            password = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//input[@name='password']")))
            password.click()
            time.sleep(3)

            for letter in password:
                password.send_keys(letter)
                time.sleep(random.randint(1, 6) / 45)
            password.send_keys(Keys.ENTER)
            time.sleep(3)

            skip_login = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//button[@class='a8gzjk']")))

            if skip_login is not None:
                skip_login.click()

            if skip_login is None:
                pass
            time.sleep(3)

        except Exception:
            print("Dados inválidos, abra novamente!")

    def notice(self):

test = likeiro()
test.home()
