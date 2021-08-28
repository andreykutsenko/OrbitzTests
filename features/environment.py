import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from app.application import Application

# def get_browser():
#    if os.environ['browser'] == 'chrome':
#        return webdriver.Chrome(executable_path='/Users/kutsenko/GitHub/OrbitzTests/drivers/mac64/chromedriver')
#    elif os.environ['browser'] == 'ff':
#        return webdriver.Firefox()

def browser_init(context):
    context.driver = webdriver.Chrome()
    # context.driver = webdriver.Firefox()
    # context.driver = get_browser()

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)
    context.wait = WebDriverWait(context.driver, 15)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
