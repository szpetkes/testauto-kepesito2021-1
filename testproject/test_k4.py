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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html")
time.sleep(2)

# !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
# Find locators:
char = driver.find_elements_by_xpath("//p[3]")
character = driver.find_element_by_id("chr")
operator = driver.find_element_by_id("op")
number = driver.find_element_by_id("num")
submit_btn = driver.find_element_by_id("submit")
result = driver.find_element_by_id("result")

test_data = [""]
reference_data = ["""!'#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""",
                  ["+", "-"]]

def test_tc1():
    assert char.text == reference_data[0]


def test_tc2():
    assert character.text in reference_data[0]
    assert operator.text == reference_data[1][0] or reference_data[1][1]
    assert number == int
    assert result.text == reference_data[1]


def test_tc3():
