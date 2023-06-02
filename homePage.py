class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.logout_link_text = "Logout"

    def click_logout(self):
        self.driver.find_element_bylink_text(self.logou_link_text).click()
