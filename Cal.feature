# Created by USER at 25-08-2022
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Additions using given data table
    Given User is on calculator
    When user enter following values
    |number1|number2|operator|
    |234    |2      |+       |
    When user verify total