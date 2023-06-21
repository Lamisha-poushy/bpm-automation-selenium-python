import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import  datetime
import json
import sys
import os
from twocaptcha import TwoCaptcha

# options = Options()
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--disable-dev-shm-usage')

# all variable
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Open the existing JSON file for loading into a variable
def all_data()->dict:
   with open('register_user.json') as json_data:
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

# Avatar select on landing page 
@pytest.mark.order(3)
def test_selectavatar():
    SelectedAvatar = all_data()["SelectedAvatar"]
    avatar = driver.find_element(by=By.XPATH, value=SelectedAvatar)
    avatar.click()
    sleep(2)

# input avatar name
@pytest.mark.order(4)
def test_inputavatarname():
    SelectedAvatarInput = all_data()["SelectedAvatarInput"]
    avatar_name = all_data()["Name"]
    avatar_name_input = driver.find_element(by=By.XPATH, value=SelectedAvatarInput)
    avatar_name_input.send_keys(avatar_name)
    sleep(2)

# Click on start button
@pytest.mark.order(5)
def test_startbutton():
    StartButton = all_data()["StartButton"]
    startbutton = driver.find_element(by=By.XPATH, value=StartButton)
    startbutton.click()
    sleep(2)

#click circle avatar
@pytest.mark.order(6)
def test_circleavatar():
    CircleAvatar = all_data()["CircleAvatar"]
    circleavatar = driver.find_element(by=By.XPATH, value=CircleAvatar)
    circleavatar.click()
    sleep(2)

#click on my profile
@pytest.mark.order(7)
def test_myprofile():
    MyProfile = all_data()["MyProfile"]
    myprofile = driver.find_element(by=By.XPATH, value=MyProfile)
    myprofile.click()
    sleep(2)

#Input Email Id
@pytest.mark.order(8)
def test_inputemail():
    EmailInput = all_data()["InputEmail"]
    email = all_data()["email"]
    email_input = driver.find_element(by=By.XPATH, value=EmailInput)
    email_input.send_keys(email)
    sleep(2)

#click date field
@pytest.mark.order(9)
def test_date():
    DateInput = all_data()["dateField"]
    date = driver.find_element(by=By.XPATH, value=DateInput)
    date.click()
    sleep(2)

#select current date 
@pytest.mark.order(10)
def test_date():  
    # Getting today's date
    now = datetime.datetime.now()
    tday = now.strftime("%m-%d-%Y")
    current_date = driver.find_element(by=By.NAME, value="dob")
    current_date.send_keys(tday)
    sleep(2)

#disable captcha 

#click checkbox
@pytest.mark.order(11)
def test_checkboxfield():
    checkbox = all_data()["checkbox"]
    click_checkbox = driver.find_element(by=By.XPATH, value=checkbox)
    click_checkbox.click()
    sleep(2)

#remove captcha
@pytest.mark.order(12)
def test_checkbox():
    api_key = os.getenv('APIKEY_2CAPTCHA', '0eeeb444cbf03281f9e7dc6b8888a242')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.hcaptcha(
            sitekey='f7de0da3-3303-44e8-ab48-fa32ff8ccc7b',
            url=all_data()["webSiteUrl"],
        )

    except Exception as e:
        sys.exit(e)

    else:
        sys.exit('solved: ' + str(result))
    
