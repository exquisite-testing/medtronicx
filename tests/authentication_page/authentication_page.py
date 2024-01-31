from pylenium import Pylenium

class AuthenticationPage:
    def __init__(self, py: Pylenium):
        self.py = py

    def select_login(self):
        return self.py.get('#login-button').should().exist()

    def enter_username(self, username):
        username_input = self.py.get('[name="username"]')
        username_input.clear()  # This is optional but worth doing as we don't control if the placeholder is fixed
        username_input.set(username)

    def enter_password(self, password):
        password_input = self.py.get('[name="password"]')
        password_input.clear()  # This is optional but worth doing as we don't control if the placeholder is fixed
        password_input.set(password)

    def select_login_button(self):
        selector = 'input[type="login"]'
        select_login = self.py.get(selector)
        select_login.click()
