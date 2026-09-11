from appium import webdriver

from config.capabilities import get_capabilities


def create_driver():
    options = get_capabilities()

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    return driver