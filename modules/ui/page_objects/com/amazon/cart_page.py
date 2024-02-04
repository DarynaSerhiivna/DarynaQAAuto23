from modules.ui.page_objects.com.amazon.base_page import BasePage
from modules.common.com.amazon.price import Price
from modules.ui.driver.driver_config import DriverConfig
from modules.ui.driver.wait_utils import WaitUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

class CartPage(BasePage):

    def __init__(self) -> None:
        super().__init__()

    def get_subtotal(self):
        locale_price =  WaitUtils.wait_for_element_visibility((By.CLASS_NAME, "sc-price")).text

        return Price(locale_price)
    
    def get_items_count(self):
        return len(self.get_items())
    
    def delete_item(self, position):
        items = self.get_items()
        items[position - 1].find_element(By.XPATH,".//input[@value='Delete']").click()

    def get_items(self):
        return DriverConfig.get_driver().find_elements(By.CLASS_NAME,"sc-list-item-content")
    
    def set_quantity(self, position, quantity):
        initial_quantity = self.get_subtotal_quantity()
        dropdowns = WaitUtils.wait_for_all_elements_visibility((By.ID,"quantity"))
        Select(dropdowns[position - 1]).select_by_index(quantity)
        self.wait_for_subtotal_quantity_change(initial_quantity)
                      
    def wait_for_subtotal_quantity_change(self, initial_quantity):
        attempts = 10
        while attempts > 0:
            if self.get_subtotal_quantity() != initial_quantity:
                break
            time.sleep(1)
            attempts -= 1 

    def get_subtotal_quantity(self):
        subtotal_quantity =  DriverConfig.get_driver().find_element(By.ID, "sc-buy-box")\
            .get_attribute("data-quantity")
        
        return int(subtotal_quantity)