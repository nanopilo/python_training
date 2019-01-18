from lettuce import before, world, after
from selenium import webdriver


@before.all
def open_shop():
    open_drivers()


@after.all
def close_shop(total):
    close_drivers()


def open_drivers():
    world.driver = get_chrome()
    world.driver.set_page_load_timeout(10)
    world.driver.implicitly_wait(10)
    world.driver.maximize_window()


def get_chrome():
    return webdriver.Chrome('./chromedriver')


def close_drivers():
    if world.driver:
        world.driver.quit()
