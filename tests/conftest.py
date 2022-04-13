import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    service = ChromeService(ChromeDriverManager(log_level=0).install())
    driver = Chrome(service=service)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
