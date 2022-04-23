from config.Config import TestData
import pytest


@pytest.fixture(params=TestData.BROWSERS, scope="class")
def init_driver(request):
    if request.param == "chrome":
        from selenium.webdriver.chrome.service import Service as ChromeService
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver import Chrome
        service = ChromeService(ChromeDriverManager(log_level=0).install())
        driver = Chrome(service=service)

    elif request.param == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager
        from selenium.webdriver import Firefox
        service = FirefoxService(GeckoDriverManager(log_level=0).install())
        driver = Firefox(service=service)

    else:
        raise AttributeError("There is no driver such exists.")

    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.delete_all_cookies()
    driver.close()
    driver.quit()
