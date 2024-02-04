from modules.ui.page_objects.com.amazon.base_page import BasePage
from modules.ui.driver.driver_config import DriverConfig
from modules.ui.driver.wait_utils import WaitUtils 
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    URL = "https://amazon.com/s"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self, search_request):
        DriverConfig.get_driver().get(SearchPage.URL + f"/?k={search_request}")
      
    def click_first_item(self):
        WaitUtils.wait_for_element_visibility((By.XPATH, "//*[starts-with(@cel_widget_id,'MAIN-SEARCH_RESULTS')]//*[@data-component-type]/a")).click()
