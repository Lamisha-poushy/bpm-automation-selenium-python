import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import json

# options = Options()
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-dev-shm-usage')

# all variable
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the existing JSON file for loading into a variable
def all_data()->dict:
   with open('./json/pts.json') as json_data:
     alldata = json.load(json_data)
   return alldata

# Open google browser , search Hasina and friends on google.com
@pytest.mark.order(1)
def test_searchkeywards():
    # open google  browser
    driver.maximize_window()
    driver.get('http://www.google.com')

    # search in google.com
    SearchKey = all_data().get("SearchKey")
    search = driver.find_element(by=By.NAME, value="q")
    search.send_keys(SearchKey)
    search.send_keys(Keys.RETURN)
    sleep(1)

# click on Hasina and Friends url on google search result
@pytest.mark.order(2)
def test_gotowebsite():
    siteUrl = all_data()["webSiteUrl"]
    webSiteUrl = driver.find_element(by=By.XPATH, value=siteUrl)
    webSiteUrl.click()
    sleep(2)

# click on pts sidebar
@pytest.mark.order(3)
def test_sidebar():
    PTSbar = all_data()["ptsBar"]
    click_sidebar = driver.find_element(by=By.XPATH, value=PTSbar)
    click_sidebar.click()
    sleep(2)

# click on quiz editor
@pytest.mark.order(4)
def test_quizeditor():
    Editor = all_data()["quizeditor"]
    click_QuizEditor = driver.find_element(by=By.XPATH, value=Editor)
    driver.execute_script("arguments[0].scrollIntoView();",click_QuizEditor)
    sleep(2)
    click_QuizEditor.click()
    sleep(2)

# click on quiz editor
@pytest.mark.order(4)
def test_quizeditor():
    Editor = all_data()["quizeditor"]
    click_QuizEditor = driver.find_element(by=By.XPATH, value=Editor)
    driver.execute_script("arguments[0].scrollIntoView();",click_QuizEditor)
    sleep(2)
    click_QuizEditor.click()
    sleep(2)

# click on sign up link 
@pytest.mark.order(5)
def test_clicksignup():
    Signup = all_data()["signup"]
    click_signup = driver.find_element(by=By.XPATH, value=Signup)
    click_signup.click()
    sleep(2)

#fill up sign in form
@pytest.mark.order(6)
def test_fillupform():
#first name
  FirstName = all_data().get("firstname")
  firstname = driver.find_element(by=By.NAME, value="firstName")
  firstname.send_keys(FirstName)
  firstname.send_keys(Keys.RETURN)
  sleep(1)

#last name
  LastName = all_data().get("lastname")
  lastname = driver.find_element(by=By.NAME, value="lastName")
  lastname.send_keys(LastName)
  lastname.send_keys(Keys.RETURN)
  sleep(1)

#email
  Email = all_data().get("email")
  email = driver.find_element(by=By.NAME, value="email")
  email.send_keys(Email)
  email.send_keys(Keys.RETURN)
  sleep(1)

#password
  Password = all_data().get("password")
  password = driver.find_element(by=By.NAME, value="password_1")
  password.send_keys(Password)
  password.send_keys(Keys.RETURN)
  sleep(1)

#confirm password
  ConfirmPassword = all_data().get("confirmPassword")
  confirmpassword = driver.find_element(by=By.NAME, value="password_2")
  confirmpassword.send_keys(ConfirmPassword)
  confirmpassword.send_keys(Keys.RETURN)
  sleep(1)

#next button
  NextButton = all_data()["nextbutton"]
  click_nextbutton = driver.find_element(by=By.XPATH, value=NextButton)
  click_nextbutton.click()