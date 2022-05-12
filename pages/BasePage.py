from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from config.Config import TestData


class BasePage:
    BODY = (By.TAG_NAME, "body")

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def navigate_to_url(self, url=TestData.BASE_URL) -> None:
        self.driver.get(url)

    def find_element(self, locator) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))

    def find_elements(self, locator) -> list:
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_all_elements_located(locator))

    def get_element_text(self, mark) -> str:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = self.find_element(mark)
        WebDriverWait(element, 3).until(lambda el: el.text != "")
        return element.text

    def get_title(self) -> str:
        return self.driver.title

    def static_wait(self, timeout=3) -> None:
        try:
            WebDriverWait(self.driver, timeout).until(lambda _: False)
        except TimeoutException:
            pass

    def hover(self, mark) -> None:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = self.find_element(mark)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def click(self, mark) -> None:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(mark))
        element.click()
        self.static_wait(1)

    def is_clickable(self, locator: tuple) -> bool:
        try:
            return bool(WebDriverWait(self.driver, self.timeout / 4).until(ec.element_to_be_clickable(locator)))
        except TimeoutException:
            return False

    def highlight(self, mark, color: str, effect_time=1, thickness=2, radius=10) -> None:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = self.find_element(mark)
        self.hover(element)
        self.driver = element.parent
        original_style = element.get_attribute('style')

        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        apply_style(f"border: {thickness}px solid {color}; border-radius: {radius}px;")
        self.static_wait(effect_time)
        apply_style(original_style)
