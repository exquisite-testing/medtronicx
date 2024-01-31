Feature: Reddit Page

    Background: Verify the Reddit homepage is loaded
        Given I am on the Reddit homepage
        Then I should see the Reddit logo

    Scenario: Search for select a Subreddit
        When I Search for the following Subreddit "Marvel"
        Then I should see the Subreddit results list
        When I select the Subreddit "r/Marvel"
        And I select the top results
        Then the title element at index "0" should have text "Expected Title Text"

    Scenario: Login and vote for Subreddit
        When I login to a user
        When I Search for the following Subreddit "Marvel"
        And I select the Subreddit "r/Marvel"
        When I select the second down vote
        Then the second down vote is selected
