"""""""""
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Bingo app-ot az https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Bingoapp tesztelését.

Az applikáció indulo bingo táblája minden frissítésnél véletlenszerűen változik!

Az ellenőrzésekhez használj pytest keretrendszert. A tesztjeidben használj assert összehasonlításokat használj!

A feladatod az alábbi tesztesetek lefejlesztése:

    Az applikáció helyesen megjelenik:
        A bingo tábla 25 darab cellát tartalmaz
        A számlista 75 számot tartalmaz

    Bingo számok ellenőzrzése:
        Addig nyomjuk a play gobot amíg az első bingo felirat meg nem jelenik
        Ellenőrizzük, hogy a bingo sorában vagy oszlopában lévő számok a szelvényről tényleg a már kihúzott számok közül kerültek-e ki

    Új játékot tudunk indítani
        az init gomb megnyomásával a felület visszatér a kiindulási értékekhez
        új bingo szelvényt kapunk más számokkal.

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

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html")
time.sleep(1)

# elements
bingos = driver.find_elements_by_xpath('//*[@id="bingo-body"]//input')
numbers = driver.find_elements_by_xpath('//*[@id="numbers-list"]//input')
play_btn = driver.find_element_by_id("spin")
init_btn = driver.find_element_by_id("init")
test_data = [25, 75]

# TC1
# page showed up 25/75
def test_tc1():
bingo_list = []
for bingo in bingos:
    bingo_list.append(bingo.text)

assert len(bingo_list) == test_data[0]

num_list = []
for num in numbers:
    num_list.append(num.text)

assert len(num_list) == test_data[1]

# Tc2
# datas shown up on the page
play_btn.click()
