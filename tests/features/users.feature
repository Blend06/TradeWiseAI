Feature: User Management
  As an admin user
  I want to create, update, delete, and view users
  So that I can manage user accounts efficiently

  Background:
    Given I am logged in as admin for users
    And I am on the Users list page

Scenario: Add new user
  When I navigate to the new user form
  And I fill in username "testuser", email "testuser@example.com", password "J7hyuititi"
  And I submit the user form
  Then I should see the new user with username "testuser" in the list

Scenario: Update existing user
  Given a user with username "testuser" exists
  When I navigate to edit the user with username "testuser"
  And I change the email to "updated@example.com"
  And I change the password to "NewPass123"
  And I submit the user form
  Then I should see the user with username "testuser" and email "updated@example.com" in the list


  Scenario: Delete a user
    Given a user with username "testuser" exists
    When I delete the user with username "testuser"
    Then I should not see the user with username "testuser" in the list

  Scenario: View user list
    Then I should see a list of users displayed