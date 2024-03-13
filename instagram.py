from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time




options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)



options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Instagram:

  chrome_driver_path="/Users/uygaraydin/Downloads/chromedriver-mac-arm64/chromedriver"




  def __init__(self,username,password):
    self.username=username
    self.password=password
    self.driver=webdriver.Chrome(Instagram.chrome_driver_path,options=options)


  def signIn(self):
    
    self.driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(4)
    usernameInput=self.driver.find_element(By.NAME,"username")
    passwordInput=self.driver.find_element(By.NAME,"password")
    usernameInput.send_keys(self.username)
    passwordInput.send_keys(self.password) 
    passwordInput.send_keys(Keys.ENTER)
    time.sleep(10)
    element = self.driver.find_element(By.XPATH, "//div[contains(text(),'yedek kodlarından')]")
    element.click()
    time.sleep(4)
    security_code = input("Lütfen güvenlik kodunu girin: ")
    time.sleep(5)
    code_input = self.driver.find_element(By.NAME,"verificationCode")
    code_input.send_keys(security_code)
    time.sleep(10)
    code_input.send_keys(Keys.ENTER)
    



app=Instagram()

app.signIn()







