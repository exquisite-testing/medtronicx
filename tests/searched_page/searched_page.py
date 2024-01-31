from pylenium import Pylenium

class SearchedPage:
    def __init__(self, py: Pylenium):
        self.py = py

    def get_title_elements(self):
        return self.py.get('[slot="title"]')

    def select_downvote(self):
        selector = '#vote-arrows-t3_19e7fxa [data-click-id="downvote"]'
        select_downvote = self.py.get(selector)
        select_downvote.click()

    def get_downvote_button_css(self):
        downvote_button_css = f'#vote-arrows-t3_19e7fxa [data-click-id="downvote"]'
        return self.py.get(downvote_button_css).should().have.css(['color', 'rgb(113, 147, 255)'])

    def select_top_results(self):
        selector = '[href="/r/Marvel/top/"]'
        select_top = self.py.get(selector)
        select_top.click()
