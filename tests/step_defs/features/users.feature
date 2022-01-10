Feature: Users endpoint methods 

    As an application developer
    I want to be able to create, update, delete
    and read Users data.

Scenario: Get list of users
  Given hit the endpoint to get list of users 
  Then the response code should be "200"
  Then the response body contains list of users

Scenario: Get single user
  Given get a user by id "2"
  Then the response code should be "200"
  Then the response body should retured the id "2"

Scenario: Get non-existing user
Given get non-existing user by id "23"
Then the response code should be "404"

Scenario: Create new user
Given create new user with name "Ghosoun" and job "leader"
Then the response code is "201"
Then the response body has name "Ghosoun" and job "leader"

