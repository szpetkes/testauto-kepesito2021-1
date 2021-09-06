"""""""""
Készíts egy Python python applikációt (egy darab python file) ami selenium-ot használ.

A program töltse be a Alfanumerikus mezőapp-ot az https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a Alfanumerikus mező app tesztelését.

Az ellenőrzésekhez használj pytest keretrendszert. A tesztjeidben használj assert összehasonlításokat használj!

A cél a mező validáció tesztelése:

    Helyes kitöltés esete:
        title: abcd1234
        Nincs validációs hibazüzenet

    Illegális karakterek esete:
        title: teszt233@
        Only a-z and 0-9 characters allewed.

    Tul rövid bemenet esete:
        title: abcd
        Title should be at least 8 characters; you entered 4.
"""

import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html")
time.sleep(1)

# elements
title1 = 'abcd1234'
title2 = 'teszt233@'
title3 = 'abcd'

text = driver.find_element_by_id("title")
error = driver.find_element_by_xpath('/html/body/form/span')


# TC1
# valid data
def test_tc1():
    text.send_keys(title1)
    assert error.is_enabled()


# TC2
# invalid data
def test_tc2():
    text.clear()
    text.send_keys(title2)
    assert error.text == 'Only a-z and 0-9 characters allewed'


# TC3
# short data
def test_tc3():
    text.clear()
    text.send_keys(title3)
    assert error.text == 'Title should be at least 8 characters; you entered 4.'


driver.close()
