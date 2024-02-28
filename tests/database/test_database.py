import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)    


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user [0] [0] == 'Maydan Nezalezhnosti 1'
    assert user [0] [1] == 'Kyiv'
    assert user [0] [2] == '3127'
    assert user [0] [3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0] [0] == 25    


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0] [0] == 30


@pytest.mark.database  
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0  


@pytest.mark.database
def test_datailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print('замовлення', orders)
    #Check quantity of orders equal to 1
    assert len(orders) == 1

    #Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.database
def test_product_insert_where_qnt_zero():
    db = Database()
    db.insert_product(77, 'apple', 'green', 0)
    qnt = db.select_product_qnt_by_id(77)

    assert qnt[0][0] == 0


@pytest.mark.database
def test_product_insert_where_qnt_large_int():
    db = Database()
    db.insert_product(79, 'lemon', 'frozen', 1234567890)
    qnt = db.select_product_qnt_by_id(79)
    
    assert qnt[0][0] == 1234567890


@pytest.mark.database 
def test_product_cant_be_deleted_when_order_exists():
    db = Database()
    db.insert_product(78, 'apple', 'green', 1000 )
    db.insert_customer(123, 'Any', 'Any', 'Any', '0000', 'Any')
    db.insert_order(111, 123, 78, '11/22/63')
    with pytest.raises(ValueError, match='Wrong Result'):
        db.delete_product_by_id(78)


@pytest.mark.database
def test_order_cant_be_created_for_unexistng_customer():
    db = Database()
    db.insert_product(20, 'tea', 'black', 10)
    with pytest.raises(ValueError, match='User not exist'):
        db.insert_order(100, 1000, 20, '11/11/11')
     
    
@pytest.mark.database
def test_customer_cant_be_created_with_no_name():
    db = Database()
    with pytest.raises(ValueError, match='User name is None'):
        db.insert_customer(80, None, 'Any', 'Any', '1212', 'Any' )
