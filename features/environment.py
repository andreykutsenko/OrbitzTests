import os
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.ui import WebDriverWait

from app.application import Application
from app.logger import *

bs_user = 'andreykutsenko1'
bs_pw = 'KwWTFPpdaewrqzqtSGQR'

# def get_browser():
#     if os.environ['browser'] == 'chrome':
#         return webdriver.Chrome()
#     elif os.environ['browser'] == 'ff':
#         return webdriver.Firefox()
#     else:
#         raise ValueError('Browser was not provided!')


def browser_init(context, name):
    # context.driver = get_browser()

    # context.driver = webdriver.Chrome()
    # context.driver = webdriver.Chrome(executable_path='/Users/kutsenko/GitHub/OrbitzTests/drivers/mac64/chromedriver')
    # context.driver = webdriver.Firefox()

    # EventFiringWebDriver - log file
    context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())

    # for BrowserStack #
    # desired_cap = {
    #     'os': 'OS X',
    #     'os_version': 'Big Sur',
    #     'browser': 'Chrome',
    #     'browser_version': '92.0',
    #     'name': name,
    #     'browserstack.networkLogs': True
    # }
    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)
    context.wait = WebDriverWait(context.driver, 15)


def before_scenario(context, scenario):
    logger.info(f'\nStarted scenario: {scenario.name}')
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'\nStarted step: {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.info(f'\nStep failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
