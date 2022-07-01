from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import random

__version__ = "0.0.1"


class likeiro:
    """ Classe inicializadora do likeiro. """

    def __init__(self):
        """ Inicializa o likeiro. """
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--lang=pt-BR")
