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
   with open('./json/biographies.json') as json_data:
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

# click on PM logo 
@pytest.mark.order(3)
def test_clickpmlogo():
    PMlogo = all_data()["PMLogo"]
    click_PMLogo = driver.find_element(by=By.XPATH, value=PMlogo)
    click_PMLogo.click()
    sleep(2)

# click on FON logo 
@pytest.mark.order(4)
def test_clickfonlogo():
    FONlogo = all_data()["fonlogo"]
    click_FONlogo = driver.find_element(by=By.XPATH, value=FONlogo)
    click_FONlogo.click()
    sleep(7)

# click on Family Matters
@pytest.mark.order(5)
def test_familymatters():
    FamilyMatters = all_data()["familymatters"]
    click_familymatters = driver.find_element(by=By.XPATH, value=FamilyMatters)
    click_familymatters.click()
    sleep(4)

    #close section
    Close = all_data()["close"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)


# click on Work and Play 
@pytest.mark.order(6)
def test_workandplay():
    WorkandPlay = all_data()["workandplay"]
    click_workandplay = driver.find_element(by=By.XPATH, value=WorkandPlay)
    click_workandplay.click()
    sleep(4)

    #close section
    Close = all_data()["close"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)

# click on The Courageous Man
@pytest.mark.order(7)
def test_myfather():
    CourageousMan = all_data()["courageousman"]
    click_courageousman = driver.find_element(by=By.XPATH, value=CourageousMan)
    click_courageousman.click() 
    sleep(4)

    #close section
    Close = all_data()["close"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)

# click on A Deep Cultural Bond
@pytest.mark.order(8)
def test_education():
    Education = all_data()["education"]
    click_education = driver.find_element(by=By.XPATH, value=Education)
    click_education.click() 
    sleep(4)

    #close section
    Close = all_data()["close"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)

# click on A Friend of Bengal
@pytest.mark.order(9)
def test_minister():
    FriendofBengal = all_data()["bengal"]
    click_bengal = driver.find_element(by=By.XPATH, value=FriendofBengal)
    click_bengal.click() 
    sleep(4)

    #close section
    Close = all_data()["close"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)
  
# click on The Road to Freedom
@pytest.mark.order(10)
def test_freedom():
    Freedom = all_data()["freedom"]
    click_freedom = driver.find_element(by=By.XPATH, value=Freedom)
    click_freedom.click() 
    sleep(4)

    #close section
    Close = all_data()["close"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)

# click on Becoming Father of the Nation
@pytest.mark.order(11)
def test_ganabhaban():
    FatherofNation = all_data()["fon"]
    click_fon = driver.find_element(by=By.XPATH, value=FatherofNation)
    click_fon.click() 
    sleep(4)

    #close section
    Close = all_data()["close"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)

# click on A Tragic Loss
@pytest.mark.order(12)
def test_tragicloss():
    TragicLoss = all_data()["tragicloss"]
    click_tragicloss = driver.find_element(by=By.XPATH, value=TragicLoss)
    click_tragicloss.click() 
    sleep(4)

    #close section
    Close = all_data()["close"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)