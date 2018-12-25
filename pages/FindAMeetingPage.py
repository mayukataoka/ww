from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.Locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class FindMeeting:

    def __init__(self, driver):
        self.driver = driver

    def find_a_meeting(self, search_word):

        self.driver.find_element_by_id(Locators.enter_location_textfield_id).send_keys(search_word)
        self.driver.find_element_by_name(Locators.search_form_name).submit()

    def print_first_location(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, Locators.location_name_link_class)))
        print(self.driver.find_element_by_class_name(Locators.location_name_link_class).text + "\n")

    def print_first_distance(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, Locators.location_distance_class)))
        print(self.driver.find_element_by_class_name(Locators.location_distance_class).text+ "\n")

    def click_first_location(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, Locators.meeting_location_top_class)))
        self.driver.find_element_by_class_name(Locators.meeting_location_top_class).click()
