from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_for_visibility_of_element_located(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_presence_of_all_elements_located(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_visibility_of(self, element):
        return self.wait.until(EC.visibility_of(element))

    def wait_for_clickable(self, locator_or_element):
        return self.wait.until(EC.element_to_be_clickable(locator_or_element))

    def fill_input(self, locator, value):
        element = self.wait_for_visibility_of_element_located(locator)
        element.send_keys(value)

    def click_after_wait(self, locator_or_element):
        self.wait_for_clickable(locator_or_element).click()

    def click_with_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def choose_from_dropdown(self, dropdown_locator, items_locator, index):
        self.click_after_wait(dropdown_locator)
        items = self.wait_for_presence_of_all_elements_located(items_locator)
        item = items[index]
        item.click()

    def find_element_by_index(self, locator, index):
        elements = self.driver.find_elements(*locator)
        return elements[index]

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_current_url(self):
        return self.driver.current_url