# Created by kutsenko at 8/26/21
Feature: Flight search testing

  Scenario: User can searches for flights and correct result is shown
    Given Open main page
    When Select Flights option
    And Select Roundtrip option
    Then Enter "Leaving from": San Francisco
    And Enter "Going to": New York, NY
#    And Select "Departing" date to be 2 weeks from today and "Returning" date to be 3 weeks from today
#    And Click on Search
#    Then Our search results are rendered correctly