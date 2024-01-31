from behave import given, then
from pylenium import Pylenium
from homepage.homepage import Homepage 

# Initialize Pylenium
py = Pylenium()
homepage = Homepage(py)

@given('I am on the Reddit homepage')
def step_given_i_am_on_the_reddit_homepage(context):
    homepage.visit_page('https://www.reddit.com/')

@then('I should see the Reddit logo')
def step_then_i_should_see_the_reddit_logo(context):
    assert homepage.is_logo_present(), "The Reddit logo is not present on the page."

@when('I Search for the following Subreddit "{subreddit_name}"')
def step_when_i_search_for_a_subreddit(context, subreddit_name):
    homepage.search_for_subreddit(subreddit_name)

@then('I should see the Subreddit results list')
def step_then_i_see_a_list_of_results(context):
    homepage.is_subreddit_list_present()

@when('I select the Subreddit "{subreddit_name}"')
def step_when_i_select_a_subreddit(context, subreddit_name):
    homepage.select_subreddit(subreddit_name)
