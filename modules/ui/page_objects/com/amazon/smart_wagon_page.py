from modules.ui.page_objects.com.amazon.base_page import BasePage
from modules.ui.driver.wait_utils import WaitUtils
from selenium.webdriver.common.by import By


class SmartWagonPage(BasePage):

    def __init__(self) -> None:
        super().__init__()

    def go_to_cart(self):
          WaitUtils.wait_for_element_visibility((By.CSS_SELECTOR, "#sw-gtc a")).click()
