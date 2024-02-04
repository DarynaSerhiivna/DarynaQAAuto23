from modules.ui.driver.driver_config import DriverConfig

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class WaitUtils:

    def wait_for_element_visibility(locator, timeout = 30):
        return WebDriverWait(DriverConfig.get_driver(), timeout).until(ec.visibility_of_element_located(locator))
    
    def wait_for_all_elements_visibility(locator, timeout = 30):
        return WebDriverWait(DriverConfig.get_driver(), timeout).until(ec.visibility_of_all_elements_located(locator))
