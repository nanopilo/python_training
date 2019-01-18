from lettuce import step, world
from nose.tools import assert_equal, assert_in


@step('Given I navigate to the Automation Practice Home page')
def step_i_navigate_to_the_home_page(step):
    world.driver.get('http://automationpractice.com/index.php')
    assert_equal(world.driver.title, 'My Store')


@step('When I search for "([^"]*)"')
def step_when_i_search_for(step, search_term):
    world.driver.find_element_by_class_name(
        'search_query'
    ).send_keys(search_term)
    world.driver.find_element_by_name('submit_search').click()


@step('Then I am taken to the Automation Practice Search Results page')
def step_i_am_taken_to_the_homepage(step):
    assert_equal(world.driver.title, 'Search - My Store')


@step('And I see the text "([^"]*)"')
def step_i_see_the_text(step, search_result):
    text_found = world.driver.find_element_by_class_name(
        'heading-counter'
    ).text
    assert_in(search_result, text_found)
