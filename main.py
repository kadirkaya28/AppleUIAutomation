import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.apple.com/"
LANG_CODES = {
    "Turkey": "tr/",
    "United Kingdom": "uk/",
    "Deutschland": "de/",
    "Italy": "it/",
    "France": "fr/",
    "Spain": "es/"
}

IPHONE = (By.CLASS_NAME, "ac-gn-iphone")
XIII_PRO = (By.CSS_SELECTOR, ".chapternav-item-iphone-13-pro a")
BUY_BUTTON = (By.CLASS_NAME, "ac-ln-button")
PRO_OR_MAX = (By.NAME, "dimensionScreensize")  # 0: Pro 1: Max
COLORS = (By.NAME, "dimensionColor")  # 0: Green 1: Silver 2: Gold 3: Graphite 4: Blue
CAPACITY = (By.NAME, "dimensionCapacity")  # 0:128 1:256 2:512 3:1TB
CARRIERS = (By.NAME, "carrierModel")  # click index 4
NO_TRADE = (By.ID, "noTradeIn")
PAYMENT_OPTIONS = (By.NAME, "purchase_option")  # click index 1
APPLE_CARE = (By.ID, "applecareplus_59_noapplecare")
ADD_BUTTON = (By.NAME, "add-to-cart")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get(BASE_URL)

"""
const x = document.querySelectorAll(".rc-dimension-selector-group")  --> en dıştaki elementleri buluyor 7 tane
x[1].querySelectorAll("div")[0].setAttribute("style", 'border: 4px solid red')  --> içteki elementleri çizdiriyoruz
x[0].querySelectorAll("div")[1].setAttribute("style", 'border: 4px solid red')
"""


def highlight(element, color: str, effect_time=1, thickness=2) -> None:
    dr = element.parent
    original_style = element.get_attribute('style')

    def apply_style(s):
        dr.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

    apply_style(f"border: {thickness}px solid {color};")

    time.sleep(effect_time)
    apply_style(original_style)


def click(locator, index=0):
    element = driver.find_elements(*locator)[index]
    highlight(element, "red")
    element.click()
    time.sleep(2)


click(IPHONE)
click(XIII_PRO)
click(BUY_BUTTON)
click(PRO_OR_MAX, 1)
click(COLORS)
click(CAPACITY, 3)
click(CARRIERS, 4)
click(NO_TRADE)
click(PAYMENT_OPTIONS, 1)
click(APPLE_CARE)
click(ADD_BUTTON)

time.sleep(5)

driver.close()
driver.quit()
