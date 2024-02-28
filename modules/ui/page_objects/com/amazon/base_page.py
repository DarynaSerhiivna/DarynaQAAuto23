from modules.ui.driver.driver_config import DriverConfig
from modules.ui.driver.wait_utils import WaitUtils 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class BasePage:
    SEARCH_FIELD = "twotabsearchtextbox"

    def search(self,search_request):
         search_field = WaitUtils.wait_for_element_visibility((By.ID, BasePage.SEARCH_FIELD))
         search_field.send_keys(search_request)
         search_field.send_keys(Keys.ENTER)
 
    def close(self):
        DriverConfig.close()