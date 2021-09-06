"""""""""
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Pitagorasz-tétel app-ot az https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel az alábbi funkcionalitásokat a Pitagorasz-tétel appban:

Az ellenőrzésekhez használj pytest keretrendszert. A tesztjeidben használj assert összehasonlításokat használj!

    Helyesen jelenik meg az applikáció betöltéskor:
        a: <üres>
        b: <üres>
        c: <nem látszik>

    Számítás helyes, megfelelő bemenettel
        a: 2
        b: 3
        c: 10

    Üres kitöltés:
        a: <üres>
        b: <üres>
        c: NaN
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
    driver.get("http://localhost:9999/randomajax.html")
    return driver


driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html")
time.sleep(1)

a = 2
b = 3
c = 10

a_num = driver.find_element_by_id("a")
b_num = driver.find_element_by_id("b")
calculation = driver.find_element_by_id("submit")
result = driver.find_element_by_id("result")

# TC1
assert result.is_displayed() == 0

#TC2
#calculation by site valid datas
a_num.send_keys(a)
b_num.send_keys(b)
calculation.click()
assert result.text == '10'

# TC3
# calculation by site empty fields
a_num.clear()
b_num.clear()
calculation.click()
assert result.text == 'NaN'

