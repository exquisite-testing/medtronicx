from behave import given, then
from pylenium import Pylenium
from authentication_page.authentication_page import AuthenticationPage 

# Initialize Pylenium
py = Pylenium()
authentication_page = AuthenticationPage(py)

@when('I login to a user')
def step_when_i_login(context):
    #Normally this will be hidden within 1password to in CI
    authentication_page.enter_username("National-Hearing6288")
    #Normally this will be hidden within 1password to in CI
    authentication_page.enter_password("Testing123")
    authentication_page.select_login()

@then('I should see the Subreddit results list')
def step_then_i_see_a_list_of_results(context):
    homepage.is_subreddit_list_present()

@when('I select the Subreddit "{subreddit_name}"')
def step_when_i_select_a_subreddit(context, subreddit_name):
    homepage.select_subreddit(subreddit_name)