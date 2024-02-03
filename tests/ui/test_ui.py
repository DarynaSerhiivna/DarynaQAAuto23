import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    #створення об"єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")

    #знаходимо поле в якому будемо вводити неправильне ім"я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field")

    #вводимо неправильне ім"я користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@istekeinemail.com")

    #знаходимо поле в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By. ID, "password")

    #вводимо неправильний пароль
    pass_elem.send_keys("Wrong password") 

    #знаходимо кнопку sign_in
    btn_elem = driver.find_element(By.NAME, "commit")

    #емулюємо клік лівою кнопкою мишки
    btn_elem.click()

    #перевіряємо що назва сторінки така яку ми очікуємо
    assert driver.title == 'Sign in to GitHub · GitHub'

    #закриваємо брузер
    driver.close()