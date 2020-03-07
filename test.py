from selenium import webdriver

driver = webdriver.Opera(executable_path = "/usr/bin/geckodriver")
driver.get("https://www.python.org")

driver.close()
