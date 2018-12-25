from pages.Locators import Locators


class Header:

    def __init__(self, driver):
        self.driver = driver

    def find_studio(self):
        header = self.driver.find_element_by_id(Locators.header_id)
        header.find_element_by_class_name(Locators.find_studio_link_class).click()

