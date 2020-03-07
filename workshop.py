import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UsingUnittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path = "./geckodriver")
        
    def test_hello_world(self):
        driver = self.driver
        driver.get("https://www.python.org")

        about_button = driver.find_element_by_link_text("About")
        sleep(1)
        about_button.click()

        
        search_bar = driver.find_element_by_id("id-search-field")
        sleep(1)
        search_bar.click()
        sleep(1)
        search_bar.send_keys("documentation")
        sleep(1)
        search_bar.send_keys(Keys.ENTER)

    
    def tearDown(self):
        print('Browser is about to close..')
        sleep(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
