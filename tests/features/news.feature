Feature: News Management
  As an admin user
  I want to create, update, delete, and view news articles
  So that I can manage news content efficiently

  Background:
    Given I am logged in as admin for news
    And I am on the News list page

  Scenario: Add new news article
    When I navigate to the new news article form
    And I fill in title "Breaking News", content "Some breaking news content", and upload image "test-image.jpg"
    And I submit the news form
    Then I should see the new news article with title "Breaking News" in the list

  Scenario: Update existing news article
    Given a news article with title "Breaking News" exists
    When I navigate to edit the news article with title "Breaking News"
    And I change the title to "Updated News Title"
    And I change the content to "Updated content"
    And I submit the news form
    Then I should see the news article with title "Updated News Title" in the list

  Scenario: Delete a news article
    Given a news article with title "Updated News Title" exists
    When I delete the news article with title "Updated News Title"
    Then I should not see the news article with title "Updated News Title" in the list

  Scenario: View news article list
    Then I should see a list of news articles displayed