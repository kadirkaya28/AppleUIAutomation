from config.Config import TestData
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def navigate_to_url(self, url=TestData.BASE_URL) -> None:
        self.driver.get(url)

    def find_element(self, locator) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))

    def find_elements(self, locator) -> list[WebElement]:
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_all_elements_located(locator))

    @staticmethod
    def find_element_under_specified_element(element: WebElement, locator) -> WebElement:
        return element.find_element(*locator)

    @staticmethod
    def find_elements_under_specified_element(element: WebElement, locator) -> list[WebElement]:
        return element.find_elements(*locator)

    def click_visibility(self, mark) -> None:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(mark))
        element.click()
        time.sleep(1)

    def click_presence(self, mark) -> None:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(mark))
        element.click()
        time.sleep(1)

    def click(self, mark) -> None:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = WebDriverWait(self.driver, self.timeout).until(ec.element_to_be_clickable(mark))
        element.click()
        time.sleep(1)

    def highlight(self, mark, color: str, effect_time=1, thickness=2, radius=10, background=False) -> None:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = self.find_element(mark)
        self.driver = element.parent
        original_style = element.get_attribute('style')

        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        if background:
            apply_style(f"background-color: {color};")
        else:
            apply_style(f"border: {thickness}px solid {color}; border-radius: {radius}px;")

        # allure.attach(self.driver.get_screenshot_as_png(),
        #               name=ctime(time.time()).replace(":", "_"),
        #               attachment_type=AttachmentType.PNG)
        time.sleep(effect_time)
        apply_style(original_style)

    def is_visible(self, mark) -> bool:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(mark))
        return bool(element)

    def is_enabled(self, mark) -> bool:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(mark))
        return element.is_enabled()

    def is_clickable(self, mark) -> bool:
        try:
            return bool(WebDriverWait(self.driver, 1).until(ec.element_to_be_clickable(mark)))
        except TimeoutException:
            return False

    def get_element_text(self, mark) -> str:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = self.find_element(mark)
        return element.text

