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

# click on my childhood 
@pytest.mark.order(4)
def test_mychildhood():
    MyChildhood = all_data()["mychildhood"]
    click_mychildhood = driver.find_element(by=By.XPATH, value=MyChildhood)
    click_mychildhood.click()
    sleep(4)

    #close section
    Close = all_data()["closebutton"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)


# click on family matters 
@pytest.mark.order(5)
def test_mychildhood():
    FamilyMatters = all_data()["familymatters"]
    click_familymatters = driver.find_element(by=By.XPATH, value=FamilyMatters)
    driver.execute_script("arguments[0].scrollIntoView();",click_familymatters)
    click_familymatters.click()
    sleep(4)

    #close section
    Close = all_data()["closebutton"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)

# click on my father 
@pytest.mark.order(6)
def test_myfather():
    MyFather = all_data()["myfather"]
    click_myfather = driver.find_element(by=By.XPATH, value=MyFather)
    click_myfather.click() 
    sleep(4)

    #close section
    Close = all_data()["closebutton"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)

# click on importance of education 
@pytest.mark.order(7)
def test_education():
    Education = all_data()["education"]
    click_education = driver.find_element(by=By.XPATH, value=Education)
    click_education.click() 
    sleep(4)

    #close section
    Close = all_data()["closebutton"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)

# click on became prime minister
@pytest.mark.order(8)
def test_minister():
    PrimeMinister = all_data()["minister"]
    click_minister = driver.find_element(by=By.XPATH, value=PrimeMinister)
    click_minister.click() 
    sleep(4)

    #close section
    Close = all_data()["closebutton"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)
  
# click on humble appreciation
@pytest.mark.order(9)
def test_minister():
    HumbleAppreciation = all_data()["appreciation"]
    click_appreciation = driver.find_element(by=By.XPATH, value=HumbleAppreciation)
    click_appreciation.click() 
    sleep(4)

    #close section
    Close = all_data()["closebutton"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)

# click on life in gana bhaban
@pytest.mark.order(10)
def test_ganabhaban():
    GanaBhaban = all_data()["ganabhaban"]
    click_ganabhaban = driver.find_element(by=By.XPATH, value=GanaBhaban)
    click_ganabhaban.click() 
    sleep(4)

    #close section
    Close = all_data()["closebutton"]
    click_closebutton = driver.find_element(by=By.XPATH, value=Close)
    click_closebutton.click()
    sleep(2)