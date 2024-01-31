from pylenium import Pylenium

class Homepage:
    def __init__(self, py: Pylenium):
        self.py = py

    def visit_page(self, url):
        self.py.visit(url)

    def is_logo_present(self):
        return self.py.get('#reddit-logo').should().exist()

    def search_for_subreddit(self, subreddit_name):
        search_input = self.py.get('#search-input')
        search_input.clear()  # This is optional but worth doing as we don't control if the placeholder is fixed
        search_input.set(subreddit_name)

    def is_subreddit_list_present(self):
        return self.py.get('#reddit-typeahead-results-partial-container').should().exist()

    def select_subreddit(self, subreddit_name):
        selector = f'input[type="{subreddit_name}"]'
        select_subreddit = self.py.get(selector)
        select_subreddit.click()
