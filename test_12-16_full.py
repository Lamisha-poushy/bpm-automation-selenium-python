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
   with open('./json/12-16.json') as json_data:
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

# Avatar select on landing page for age 12 to 16
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

# Click on environment theme
@pytest.mark.order(6)
def test_environmenttheme():
    Environment = all_data()["EnvironmentTheme"]
    environmenttheme = driver.find_element(by=By.XPATH, value=Environment)
    environmenttheme.click()
    sleep(2)

#Maya has a Secret
@pytest.mark.order(7)
def test_maya ():
    Maya = all_data()["maya"]
    story_maya = driver.find_element(by=By.XPATH, value=Maya)
    story_maya.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = all_data()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = all_data()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

#Rafid Loves Photography
@pytest.mark.order(8)
def test_rafid ():
    Environment = all_data()["EnvironmentTheme"]
    environmenttheme = driver.find_element(by=By.XPATH, value=Environment)
    environmenttheme.click()
    sleep(2)

    Rafid = all_data()["rafid"]
    story_rafid = driver.find_element(by=By.XPATH, value=Rafid)
    story_rafid.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = all_data()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = all_data()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

#Redwan's Experiments with the Sun
@pytest.mark.order(9)
def test_redwan ():
    Environment = all_data()["EnvironmentTheme"]
    environmenttheme = driver.find_element(by=By.XPATH, value=Environment)
    environmenttheme.click()
    sleep(2)

    Redwan = all_data()["redwan"]
    story_redwan = driver.find_element(by=By.XPATH, value=Redwan)
    story_redwan.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = all_data()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = all_data()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

# Click on health theme
@pytest.mark.order(10)
def test_healththeme():
    Health = all_data()["HealthTheme"]
    healththeme = driver.find_element(by=By.XPATH, value=Health)
    healththeme.click()
    sleep(2)

#Vegetables in our Backyard
@pytest.mark.order(11)
def test_vegetables ():
    Vegetables = all_data()["vegetables"]
    story_vegetables = driver.find_element(by=By.XPATH, value=Vegetables)
    story_vegetables.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = all_data()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = all_data()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

#The Cricket Diaries
@pytest.mark.order(12)
def test_cricket ():
    Health = all_data()["HealthTheme"]
    healththeme = driver.find_element(by=By.XPATH, value=Health)
    healththeme.click()
    sleep(2)

    Cricket = all_data()["cricket"]
    story_cricket = driver.find_element(by=By.XPATH, value=Cricket)
    story_cricket.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = all_data()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = all_data()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

#The Girl Who Stopped Smiling
@pytest.mark.order(13)
def test_girl ():
    Health = all_data()["HealthTheme"]
    healththeme = driver.find_element(by=By.XPATH, value=Health)
    healththeme.click()
    sleep(2)

    Girl = all_data()["girl"]
    story_girl = driver.find_element(by=By.XPATH, value=Girl)
    story_girl.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = all_data()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = all_data()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

# Click on education theme
@pytest.mark.order(14)
def test_educationtheme():
    Education = all_data()["EducationTheme"]
    educationtheme = driver.find_element(by=By.XPATH, value=Education)
    educationtheme.click()
    sleep(2)

#Its the Time to Celebrate
@pytest.mark.order(15)
def test_celebrate ():
    Celebrate = all_data()["celebrate"]
    story_celebrate = driver.find_element(by=By.XPATH, value=Celebrate)
    story_celebrate.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = all_data()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = all_data()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

#Orin's Skills Are Electrical
@pytest.mark.order(16)
def test_orin ():
    Education = all_data()["EducationTheme"]
    educationtheme = driver.find_element(by=By.XPATH, value=Education)
    educationtheme.click()
    sleep(2)

    Orin = all_data()["orin"]
    story_orin = driver.find_element(by=By.XPATH, value=Orin)
    story_orin.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = all_data()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = all_data()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

#Brishti is a Brat
@pytest.mark.order(17)
def test_brishti ():
    Education = all_data()["EducationTheme"]
    educationtheme = driver.find_element(by=By.XPATH, value=Education)
    educationtheme.click()
    sleep(2)

    Brishti = all_data()["brishti"]
    story_brishti = driver.find_element(by=By.XPATH, value=Brishti)
    story_brishti.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = all_data()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = all_data()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

# Click on connectivity theme
@pytest.mark.order(18)
def test_connectivitytheme():
    Connectivity = all_data()["ConnectivityTheme"]
    connectivitytheme = driver.find_element(by=By.XPATH, value=Connectivity)
    connectivitytheme.click()
    sleep(2)

#Can I Help You Abbu
@pytest.mark.order(19)
def test_abbu ():
    Abbu = all_data()["abbu"]
    story_abbu = driver.find_element(by=By.XPATH, value=Abbu)
    story_abbu.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = all_data()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = all_data()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

#Faisal Wants to Sing
@pytest.mark.order(20)
def test_faisal ():
    Connectivity = all_data()["ConnectivityTheme"]
    connectivitytheme = driver.find_element(by=By.XPATH, value=Connectivity)
    connectivitytheme.click()
    sleep(2)

    Faisal = all_data()["faisal"]
    story_faisal = driver.find_element(by=By.XPATH, value=Faisal)
    story_faisal.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = all_data()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = all_data()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

#Radyna vs Enigmus the Alien
@pytest.mark.order(21)
def test_alien ():
    Connectivity = all_data()["ConnectivityTheme"]
    connectivitytheme = driver.find_element(by=By.XPATH, value=Connectivity)
    connectivitytheme.click()
    sleep(2)

    Alien = all_data()["alien"]
    story_alien = driver.find_element(by=By.XPATH, value=Alien)
    story_alien.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = all_data()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = all_data()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)