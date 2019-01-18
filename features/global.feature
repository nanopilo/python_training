Feature: Global

  Scenario: Phone Number Automation Practice
    Given I navigate to the Automation Practice Home page
    When I get the phone number section
    Then I can see the phone number text "0123-456-789"

  Scenario: Social Footer Automation Practice
    Given I navigate to the Automation Practice Home page
    When I get the social section
    Then I can count 4 social items 
