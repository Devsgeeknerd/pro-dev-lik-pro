from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import random
import getpass
import time

# Versão
__version__ = "0.0.1"

class likeiro:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--lang=pt-BR")
        chrome_options.add_argument("--disable-notification")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome()
