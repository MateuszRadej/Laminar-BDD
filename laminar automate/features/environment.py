from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def before_feature(context, feature):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    
def after_feature(context, feature):
    context.driver.quit()

def element_exists(selector):
    try:
        selector()
    except (NoSuchElementException, TimeoutException):
        return False
    return True