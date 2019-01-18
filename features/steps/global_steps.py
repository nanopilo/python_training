from lettuce import step, world
from nose.tools import assert_equal


@step('Given I navigate to the Automation Practice Home page')
def step_i_navigate_to_the_home_page(step):
    world.driver.get('http://automationpractice.com/index.php')
    assert_equal(world.driver.title, 'My Store')


@step('When I get the phone number section')
def step_when_i_get_the_phone_number_section(step):
    phone_number_container = \
        world.driver.find_element_by_class_name('shop-phone')
    world.phone_number = phone_number_container.\
        find_element_by_tag_name('strong').text


@step('I can see the phone number text "([^"]*)"')
def step_i_can_see_the_phone_number_text(step, phone_number):
    assert_equal('0123-456-789', phone_number)


@step('When I get the social section')
def step_when_i_get_the_social_section(step):
    world.social_elements = world.driver.find_elements_by_xpath(
        '//section[@id="social_block"]/ul/li')


@step('I can count (\d+) social items')
def step_i_can_count_four_social_items(step, social_elements):
    assert_equal(4, len(world.social_elements))
