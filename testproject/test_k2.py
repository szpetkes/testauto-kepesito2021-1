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

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html")
    return driver


driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html")
time.sleep(1)
