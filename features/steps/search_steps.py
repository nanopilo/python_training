from lettuce import step, world
from nose.tools import assert_equal, assert_in


@step('Given I navigate to the Automation Practice Home page')
def step_i_navigate_to_the_home_page(step):
    world.home.navigate('http://automationpractice.com/index.php')
    assert_equal(world.home.get_page_title(), 'My Store')


@step('When I search for "([^"]*)"')
def step_when_i_search_for(step, search_term):
    world.home.search(search_term)


@step('Then I am taken to the Automation Practice Search Results page')
def step_i_am_taken_to_the_search_results_page(step):
    assert_equal(world.search.get_page_title(), 'Search - My Store')


@step('And I see the text "([^"]*)"')
def step_i_see_the_text(step, search_result):
    text_found = world.search.find_search_results()
    assert_in(search_result, text_found)
