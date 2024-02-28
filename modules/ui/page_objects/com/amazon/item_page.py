from modules.ui.page_objects.com.amazon.base_page import BasePage
from modules.common.com.amazon.price import Price
from modules.ui.driver.wait_utils import WaitUtils
from selenium.webdriver.common.by import By

class ItemPage(BasePage):
    ADD_TO_CART_BUTTON =  "add-to-cart-button"
    FINAL_PRICE = "#apex_desktop .priceToPay"

    def __init__(self) -> None:
        super().__init__()

    def add_to_cart(self):
        WaitUtils.wait_for_element_visibility((By.ID, ItemPage.ADD_TO_CART_BUTTON)).click()

    def get_final_price(self):
       locale_price = WaitUtils.wait_for_element_visibility((By.CSS_SELECTOR, ItemPage.FINAL_PRICE)).text
       
       return Price(locale_price)