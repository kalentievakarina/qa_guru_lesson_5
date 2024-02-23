import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_open():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 5.0
    browser.config.window_height = 1100
    browser.config.window_width = 1200

    yield

    browser.quit()