"""""""""
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Színes reakció app-ot az https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Színes reakció app tesztelését.

Az ellenőrzésekhez használj pytest keretrendszert. A tesztjeidben használj assert összehasonlításokat használj!

Az alábbi teszteseteket kell lefedned:

    Helyesen jelenik meg az applikáció betöltéskor: Alapból egy random kiválasztott szín jelenik meg az == bal 
    oldalanán. A jobb oldalon csak a [ ] szimbólum látszik. <szín neve> [ ] == [ ] 

    El lehet indítani a játékot a start gommbal.
        Ha elindult a játék akkor a stop gombbal le lehet állítani.

    Eltaláltam, vagy nem találtam el. Ha leállítom a játékot két helyes működés van, ha akkor állítom épp le amikor a 
    bal és a jobb oldal ugyan azt a színt tartalmazza akkor a Correct! felirat jelenik meg. ha akkor amikor eltérő 
    szín van a jobb és bal oldalon akkor az Incorrect! felirat kell megjelenjen. "" """

import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html")
time.sleep(1)

# elements
color = driver.find_element_by_id("randomColor")
test_color = driver.find_element_by_id("testColor")
start = driver.find_element_by_id("start")
stop = driver.find_element_by_id("stop")
result = driver.find_element_by_id("result")
random_color = driver.find_element_by_id("randomColorName")

all_colors = driver.find_element_by_id("allcolors").text
color_list = all_colors.replace('"', "").split(", ")


# TC1
# color check
def test_tc1():
    random_col_in = []
    for color in color_list:
        if random_color.text == color:
            random_col_in.append(color)
        assert random_col_in == random_color.text


# TC2
def test_tc2():
    test_list = []
    for i in color_list:
        start.click()
        test_list.append(i)

    assert len(test_list) != 0

    test_list1 = []
    for i in color_list:
        start.click()
        test_list1.append(i)
        stop.click()
        break

    assert len(test_list) > len(test_list1)


# TC3
def test_tc3():


    if random_color.text == test_color.text:
        assert result.text == "Correct!"
    else:
        assert result.text == "Incorrect!"
