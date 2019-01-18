class SearchResultsPage(object):

    def __init__(self, browser):
        self.driver = browser

    def get_element(self, locator):
        return self.driver.find_element_by_class_name(locator)

    def get_page_title(self):
        return self.driver.title

    def find_search_results(self):
        return self.get_element('heading-counter').text
