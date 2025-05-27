Feature: User Feedback Management
  As a user or admin
  I want to create, update, delete, and view user feedbacks
  So that I can manage feedback efficiently

  Background:
    Given I am logged in as admin for feedbacks
    And I am on the User Feedback list page

  Scenario: Add new feedback
    When I navigate to the new feedback form
    And I fill in user "3", message "This is a test feedback", feedback type "suggestion"
    And I submit the feedback form
    Then I should see the new feedback with message "This is a test feedback" in the list

  Scenario: Update existing feedback
    Given a feedback with message "This is a test feedback" exists
    When I navigate to edit the feedback with message "This is a test feedback"
    And I change the message to "Updated feedback message"
    And I submit the feedback form
    Then I should see the feedback with message "Updated feedback message" in the list

  Scenario: Delete a feedback
    Given a feedback with message "Updated feedback message" exists
    When I delete the feedback with message "Updated feedback message"
    Then I should not see the feedback with message "Updated feedback message" in the list

  Scenario: View feedback list
    Then I should see a list of feedbacks displayed
