from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)