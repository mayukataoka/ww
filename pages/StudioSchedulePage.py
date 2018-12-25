from pages.Locators import Locators


class StudioSchedule:

    def __init__(self, driver):
        self.driver = driver
        self.name_count_dictionary = {}

    def get_day_index(self, day):

        if day == 'sun':
            return 0
        elif day == 'mon':
            return 1
        elif day == 'tue':
            return 2
        elif day == 'wed':
            return 3
        elif day == 'thu':
            return 4
        elif day == 'fri':
            return 5
        elif day == 'sat':
            return 6

    def get_column_element(self, day):

        day_column = self.driver.find_elements_by_class_name(Locators.schedule_detailed_day_meetings_class)
        index = self.get_day_index(day)
        return day_column[index]

    def construct_name_count_hash(self, day):
        self.name_count_dictionary = {}
        column = self.get_column_element(day)
        names = column.find_elements_by_class_name(Locators.schedule_detailed_day_meetings_item_leader_class)

        for name in names:
            instructor_name = name.text
            if instructor_name not in self.name_count_dictionary:
                self.name_count_dictionary[instructor_name] = 1
            else:
                self.name_count_dictionary[instructor_name] = self.name_count_dictionary[instructor_name] + 1
        return self.name_count_dictionary

    def print_instructor_names_and_class_count(self):
        for i in self.name_count_dictionary:
            print("Name:" + i, " Total: " + str(self.name_count_dictionary[i]) + " times")

    def get_schedule_summary(self, day):
        day = day.lower()
        self.construct_name_count_hash(day)
        print("On " + day)
        self.print_instructor_names_and_class_count()





