Feature: Api Search Functionality

    As an application developer,
    I want to get answer for search for university via REST API,
    So that I can search using filters.

Scenario: Search for universities by name
  Given search for specific "Campion College"
  Then the response status code is "200"
  And the response contains results for "Campion College"

Scenario: Search for universities by part of name
  Given search for university using part of university name "Saint"
  Then the response status code is "200"
  And all the returned universities have "Saint" in their names

Scenario: Search for university by country and part of university name
  Given search for university using specific country name "Canada" and "Brand" university
  Then the response has status code "200"
  And all the result has country name "Canada"
  And all the returned universities contain "Brand" in their names

Scenario: List of univeristis display
  Given searching for university without using the filters
  Then the response status code "200"
  And the result length is greater than "0"

Scenario: Search using invalid country
  Given search using invalid <country> name
  # When using numbers as a <country> name
  # And using non-existing <country> name
  # And using Arabic <country> name
  # And using part of <country> name
  # And using part of <country> name
  # And using valid <country> name but non-existing <university> name
  # And using valid <university> name but non-existing <country> name
  Then the response body should be empty

Examples:
    | country |
    | 123     |
    | test    | 
    | الاردن   |  
    | United  |  

Scenario: Search using invalid params
Given Search using valid country "Canada" but non-existing university name "test"
And using valid university "Campion College" but non-existing country name "QA test"
Then the response body is empty
