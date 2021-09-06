"""""""""
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Műveletek karakterekkel app-ot az https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html 
oldalról. 

Feladatod, hogy automatizáld selenium webdriverrel a Műveletek karakterekkel app tesztelését.

Az applikáció minden frissítésnél véletlenszerűen változik!

Az ellenőrzésekhez használj pytest keretrendszert. A tesztjeidben használj assert összehasonlításokat használj!

Az alábbi teszt eseteket kell kidolgozzad:

    Helyesen betöltődik az applikáció:
        Megjelenik az ABCs műveleti tábla, pontosan ezzel a szöveggel:
            !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~

    Megjelenik egy érvényes művelet:
        chr megző egy a fenti ABCs műveleti táblából származó karaktert tartalmaz
        op mező vagy + vagy - karaktert tartlamaz
        num mező egy egész számot tartalamaz

    Gombnyomásra helyesen végződik el a random művelet a fenti ABCs tábla alapján:
        A megjelenő chr mezőben lévő karaktert kikeresve a táblában
        Ha a + művelet jelenik meg akkor balra lépve ha a - akkor jobbra lépve
        A num mezőben megjelenő mennyiségű karaktert
        az result mező helyes karaktert fog mutatni

"""""

import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html")
    return driver


driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html")
time.sleep(1)

# elements
chr = driver.find_element_by_id('chr')
op = driver.find_element_by_id('op')
number = driver.find_element_by_id('num')
calc_button = driver.find_element_by_id('submit')
result = driver.find_element_by_id('result')
text_check = driver.find_element_by_xpath('/html/body/div/div/p[3]/text()')

# TC1
# page showed up and text is displayed
assert text_check.text == "!"  # $%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

# Tc2
# datas shown up on the page
assert chr.text
