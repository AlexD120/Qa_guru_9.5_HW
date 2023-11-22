from selene import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_config():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'

    yield

    browser.quit()