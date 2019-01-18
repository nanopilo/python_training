class HomePage(object):

    def __init__(self, browser):
        self.driver = browser

    def fill(self, locator, text):
        self.driver.find_element_by_class_name(locator).send_keys(text)

    def click_element(self, locator):
        self.driver.find_element_by_name(locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        self.fill('search_query', search_term)
        self.click_element('submit_search')
