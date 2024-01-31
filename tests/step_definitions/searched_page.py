from behave import given, then
from pylenium import Pylenium
from searched_page.searched_page import SearchedPage 

# Initialize Pylenium
py = Pylenium()
searched_page = SearchedPage(py)

@then('the title element at index "{index}" should have text "{expected_text}"')
def step_then_i_print_a_list_of_top_titles(context, index, expected_text):
    title_elements = searched_page.get_title_elements()
    # Ensure there is at least one title element
    assert title_elements.should().exist(), "No title elements found"
    # Get the text content of the title element using dynamic index to be reused
    index_element_text = title_elements.eq(int(index)).text()
    # Assert the title text
    assert index_element_text == expected_text, f"Actual title text: {index_element_text}"

@when('I select the second downvote')
def step_when_i_select_the_second_downvote(context):
    searched_page.select_downvote()

@then('the title element at index "{index}" should have text "{expected_text}"')
def step_then_the_downvote_is_selected(context, index, expected_text):
    searched_page.get_downvote_button_css()

@when('I select the top results')
def step_when_i_select_the_second_downvote(context):
    searched_page.select_top_results()