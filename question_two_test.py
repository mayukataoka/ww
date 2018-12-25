from selenium import webdriver
import pytest
from pages.HeaderPage import Header

from pages.FindAMeetingPage import FindMeeting
from pages.StudioSchedulePage import StudioSchedule


@pytest.fixture()
def env_setup():
    global driver
    DRIVER_PATH = '/Users/mayukataoka/Downloads/chromedriver'
    URL = 'https://www.weightwatchers.com/us/'
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(URL)
    yield
    driver.close()
    driver.quit()


def test_get_schedule_summary(env_setup):

    assert 'WW (Weight Watchers): Weight Loss & Wellness Help' in driver.title
    page_header = Header(driver)

    page_header.find_studio()
    assert 'Find a Studio & Meeting Near You | WW USA' in driver.title

    page_meeting_search = FindMeeting(driver)
    page_meeting_search.find_a_meeting("10011")
    assert 'Weight Loss Meeting Locations; 10011 | WW USA' in driver.title

    page_meeting_search.print_first_location()
    page_meeting_search.print_first_distance()

    page_meeting_search.click_first_location()

    schedule = StudioSchedule(driver)
    schedule.get_schedule_summary('Mon')
    schedule.get_schedule_summary('Tue')
    schedule.get_schedule_summary('Wed')

