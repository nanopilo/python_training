from lettuce import before, world, after
from selenium import webdriver
from features.pages.home import HomePage
from features.pages.search_results import SearchResultsPage


@before.all
def open_shop():
    open_drivers()
    prepare_pages(world.driver)


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


def prepare_pages(driver):
    world.home = HomePage(driver)
    world.search = SearchResultsPage(driver)


def close_drivers():
    if world.driver:
        world.driver.quit()
