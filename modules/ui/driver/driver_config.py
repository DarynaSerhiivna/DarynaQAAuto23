from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverConfig:

    driver = None

    def get_driver():
        if DriverConfig.driver is None:
            DriverConfig.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        return DriverConfig.driver
    
    def close():
        if DriverConfig.driver is not None:
            DriverConfig.driver.close()
            DriverConfig.driver = None