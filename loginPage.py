class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = "username"
        self.password_textbox_password = "password"



    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_text_name).clear()         #clear sterge valorile tastate din username tab pe pg de logare
        self.driver.find_element_by_name(self.enter_username_textbox_name).send_keys(username)      #trimite mai departe username-ul

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_password).clear()
        self.driver.find_element_by_name(self.password_textbox_password).send_keys()