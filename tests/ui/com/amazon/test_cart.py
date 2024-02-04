from modules.ui.page_objects.com.amazon.search_page import SearchPage
from modules.ui.page_objects.com.amazon.cart_page import CartPage
from modules.ui.page_objects.com.amazon.item_page import ItemPage
from modules.ui.page_objects.com.amazon.smart_wagon_page import SmartWagonPage
import pytest

search_request = "iphone 15"

@pytest.mark.amazonui
def test_add_single_item_to_cart():
    search_page = SearchPage()
    search_page.go_to(search_request)
    search_page.click_first_item()
    item_page = ItemPage()
    expected_price = item_page.get_final_price().to_float()
    item_page.add_to_cart()
    smart_wagon_page = SmartWagonPage()
    smart_wagon_page.go_to_cart()
    cart_page = CartPage()
    assert cart_page.get_subtotal().to_float() == expected_price
    assert cart_page.get_items_count() == 1
    cart_page.close()
    
@pytest.mark.amazonui
def test_add_several_items_to_cart():
    search_page = SearchPage()
    search_page.go_to(search_request)
    search_page.click_first_item()
    item_page = ItemPage()
    expected_price = item_page.get_final_price().to_float()
    item_page.add_to_cart()
    smart_wagon_page = SmartWagonPage()
    smart_wagon_page.search("iphone 15 pro case")
    search_page.click_first_item()
    expected_price += item_page.get_final_price().to_float()
    item_page.add_to_cart()
    smart_wagon_page.go_to_cart()
    cart_page = CartPage()
    assert cart_page.get_subtotal().to_float() == expected_price
    assert cart_page.get_items_count() == 2
    cart_page.close()

@pytest.mark.amazonui
def test_remove_item_from_cart():
    search_page = SearchPage()
    search_page.go_to(search_request)
    search_page.click_first_item()
    item_page = ItemPage()
    item_page.add_to_cart()
    smart_wagon_page = SmartWagonPage()
    smart_wagon_page.go_to_cart()
    cart_page = CartPage()
    cart_page.delete_item(1)
    assert cart_page.get_subtotal().to_float() == 0
    assert cart_page.get_items_count() == 0
    cart_page.close()

@pytest.mark.amazonui
def test_quantity_increment():
    expected_quantity = 2
    search_page = SearchPage()
    search_page.go_to(search_request)
    search_page.click_first_item()
    item_page = ItemPage()
    expected_price = item_page.get_final_price().to_float()
    item_page.add_to_cart()
    smart_wagon_page = SmartWagonPage()
    smart_wagon_page.go_to_cart()
    cart_page = CartPage()
    cart_page.set_quantity(1, expected_quantity)
    assert cart_page.get_subtotal().to_float() == expected_price * expected_quantity
    cart_page.close()