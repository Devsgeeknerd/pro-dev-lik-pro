# Curtir fotos e videos no feed do Instagram, Facebook, Twitter e LinkedIn.
# Fazer as mudanças necessárias de acordo com a rede social preferida.

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

class devslike:
    def __init__(self):
        # Configurações do Chrome.
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--lang=pt-BR")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-notifications")
        
        # Inicialização do driver do Chrome.
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver.exe", options=chrome_options)
        self.driver.set_window_size(450, 768)
        
        # Configuração da espera explícita.
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=12,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
            ]
        )

    def data_input(self):
        # Solicita informações do usuário.
        self.user = str(input("Usuário: "))
        self.valid_information = True

        try:
            while self.valid_information == False:
                # Evita um loop infinito (pode haver um erro de lógica aqui).
                self.data_input()

            if self.user == " ":
                print("Usuário não encontrado!")
                self.data_input()

            # Solicita senha de forma segura.
            self.password = getpass.getpass(prompt="Senha: ", stream=None)

            # Solicita quantidade de likes desejados.
            self.likes = int(input("Quantos likes você deseja? "))

        except ValueError:
            print("Dados inválidos")

    def home(self):
        # Navega até a página inicial do Instagram.
        self.driver.get("https://www.instagram.com/")
        
        # Chama métodos para fazer login, exibir notificações, dar likes e fornecer opiniões.
        self.login(self.user, self.password)
        self.notice()
        self.like(self.likes)
        # Método opinion() não foi definido no código fornecido.

    def login(self, user, password):
        try:
            # Localiza e preenche campo de nome de usuário.
            user = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@name='username']")))
            user.click()
            time.sleep(3)

            for letter in user:
                user.send_keys(letter)
                time.sleep(random.randint(1, 9) / 60)

            # Localiza e preenche campo de senha.
            password = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@name='password']")))
            password.click()
            time.sleep(3)

            for letter in password:
                password.send_keys(letter)
                time.sleep(random.randint(1, 6) / 45)
            password.send_keys(Keys.ENTER)
            time.sleep(3)

            # Verifica se há um botão de "skip login".
            skip_login = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[@class='a8gzjk']")))

            if skip_login is not None:
                skip_login.click()

            if skip_login is None:
                pass
            time.sleep(3)

        except Exception:
            print("Dados inválidos, abra novamente!")

    def notice(self):
        # Mensagens indicando sucesso do login e contagem regressiva para iniciar as operações.
        print("Login feito com sucesso!!!")
        print("Vamos começar em breve!!!")

        for i in range(1, 6):
            time.sleep(3)
            print(f"Iniciando em {i} / 5")

    def like(self, likes):
        try:
            self.counting = 0

            for i in range(1, likes + 1):
                # Corrigindo o XPath para encontrar o botão de like (pode variar dependendo do site).
                like = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'br93n')]")))

                # Executa um script JavaScript para rolar a página.
                self.driver.execute_script("window.scrollBy(0, 1000);")

                # Verifica se o botão de like está visível antes de tentar clicar.
                if like.is_displayed():

                    # Verifica se o botão não está selecionado antes de clicar.
                    if not like.is_selected():
                        like.click()
                        print("Ja deixei meu like!!!")
                        time.sleep(6)

                    else:
                        print("Ja tinha meu like!!!")

                        self.counting += 1
                else:
                    print("Botão de like não está visível.")

        except Exception as e:
            print(f"Algo deu errado: {str(e)}")

# Cria uma instância da classe devslike.
test = devslike()

# Chama o método home para iniciar o script.
test.home()
