# Created by kutsenko at 8/26/21
Feature: Flight search testing

  @smoke_kts
  Scenario Outline: User can searches for flights and correct result is shown
    Given Open main page
    When Select Flights option
    And Select Roundtrip option
    Then Enter "Leaving from": <city_from>
    And Enter "Going to": <city_to>
    And Select "Departing" date to be <start_trip_week> weeks from today and "Returning" date to be <back_trip_week> weeks from today
    Then Click on Search
    Then Our search results for <city_from>, <city_to> and the date with <start_trip_week> and <back_trip_week> are displayed correctly
    When Select “Nonstop” option
    And Select the <price> flight from the list
    And Click on the <price> flight
    Then Our the flight details for <city_from>, <city_to> and the date with <start_trip_week> and <back_trip_week> are displayed correctly
    Examples:
      | city_from     | city_to       | price           | start_trip_week | back_trip_week |
      | San Francisco | New York, JFK | Price (Highest) |2                | 3              |