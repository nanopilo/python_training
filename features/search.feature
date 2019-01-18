Feature: Search

  Scenario: Search Automation Practice
    Given I navigate to the Automation Practice Home page
    When I search for "shoes"
    Then I am taken to the Automation Practice Search Results page
    And I see the text "results have been found"
