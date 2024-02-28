from modules.ui.page_objects.com.amazon.search_page import SearchPage
from modules.ui.page_objects.com.amazon.cart_page import CartPage
from modules.ui.page_objects.com.amazon.item_page import ItemPage
from modules.ui.page_objects.com.amazon.smart_wagon_page import SmartWagonPage
import pytest

SEARCH_REQUEST = "iphone 15"

@pytest.mark.amazonui
def test_add_single_item_to_cart():

    # do search on the page
    search_page = SearchPage()
    search_page.go_to(SEARCH_REQUEST)

    # select first item
    search_page.click_first_item()
    item_page = ItemPage()
    
    # save item price
    expected_price = item_page.get_final_price().to_float()
    
    # add item to cart
    item_page.add_to_cart()
    
    # go to cart
    smart_wagon_page = SmartWagonPage()
    smart_wagon_page.go_to_cart()
    
    # check total price is correct
    cart_page = CartPage()
    assert cart_page.get_subtotal().to_float() == expected_price
    
    # check items count is correct
    assert cart_page.get_items_count() == 1
    
    # close current page
    cart_page.close()
    
@pytest.mark.amazonui
def test_add_several_items_to_cart():

    # do search on the page
    search_page = SearchPage()
    search_page.go_to(SEARCH_REQUEST)

    # select first item
    search_page.click_first_item()
    item_page = ItemPage()
    
    # save item price
    expected_price = item_page.get_final_price().to_float()

    # add item to cart
    item_page.add_to_cart()
    
    # do search on the page
    smart_wagon_page = SmartWagonPage()
    smart_wagon_page.search("iphone 15 pro case")

    # select first item
    search_page.click_first_item()
    
    # add item price to previously saved
    expected_price += item_page.get_final_price().to_float()
    
    # add item to cart
    item_page.add_to_cart()
    
    # go to cart
    smart_wagon_page.go_to_cart()
    cart_page = CartPage()
    
    # check total price is correct
    assert cart_page.get_subtotal().to_float() == expected_price
    
    # check items count is correct
    assert cart_page.get_items_count() == 2
    
    # close current page
    cart_page.close()

@pytest.mark.amazonui
def test_remove_item_from_cart():

    # do search on the page
    search_page = SearchPage()
    search_page.go_to(SEARCH_REQUEST)
    
    # select first item
    search_page.click_first_item()
    item_page = ItemPage()
    
    # add item to cart
    item_page.add_to_cart()
    smart_wagon_page = SmartWagonPage()
    
    # go to cart
    smart_wagon_page.go_to_cart()
    cart_page = CartPage()
    
    # delete item from cart
    cart_page.delete_item(1)
    
    # check total price is zero
    assert cart_page.get_subtotal().to_float() == 0
    
    # check items count is zero
    assert cart_page.get_items_count() == 0
    
    # close current page
    cart_page.close()

@pytest.mark.amazonui
def test_quantity_increment():
    expected_quantity = 2

    # do search on the page
    search_page = SearchPage()
    search_page.go_to(SEARCH_REQUEST)
    
    # select first item
    search_page.click_first_item()
    item_page = ItemPage()
    
    # save item price
    expected_price = item_page.get_final_price().to_float()
    
    # add item to cart
    item_page.add_to_cart()
    smart_wagon_page = SmartWagonPage()
    
    # go to cart
    smart_wagon_page.go_to_cart()
    cart_page = CartPage()
    
    # set first item quantity
    cart_page.set_quantity(1, expected_quantity)
    
    # check total amount
    assert cart_page.get_subtotal().to_float() == expected_price * expected_quantity
    
    # close current page
    cart_page.close()