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
   with open('./json/9-12.json') as json_data:
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

# Avatar select on landing page for age 6 to 9
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

#Omar and the Sundarbans
@pytest.mark.order(7)
def test_omar ():
    Omar = all_data()["omar"]
    story_omar = driver.find_element(by=By.XPATH, value=Omar)
    story_omar.click()
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

#Jui is a Bit Odd
@pytest.mark.order(8)
def test_jui ():
    Environment = all_data()["EnvironmentTheme"]
    environmenttheme = driver.find_element(by=By.XPATH, value=Environment)
    environmenttheme.click()
    sleep(2)

    Jui = all_data()["jui"]
    story_jui = driver.find_element(by=By.XPATH, value=Jui)
    story_jui.click()
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

#Build A Better World- Brick By Brick
@pytest.mark.order(9)
def test_brick ():
    Environment = all_data()["EnvironmentTheme"]
    environmenttheme = driver.find_element(by=By.XPATH, value=Environment)
    environmenttheme.click()
    sleep(2)

    Brick = all_data()["brick"]
    story_brick = driver.find_element(by=By.XPATH, value=Brick)
    story_brick.click()
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

#Ruba doesn't like Vegetables
@pytest.mark.order(11)
def test_ruba ():
    Ruba = all_data()["ruba"]
    story_ruba = driver.find_element(by=By.XPATH, value=Ruba)
    story_ruba.click()
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

#Fahim's Secret World
@pytest.mark.order(12)
def test_fahim ():
    Health = all_data()["HealthTheme"]
    healththeme = driver.find_element(by=By.XPATH, value=Health)
    healththeme.click()
    sleep(2)

    Fahim = all_data()["fahim"]
    story_fahim = driver.find_element(by=By.XPATH, value=Fahim)
    story_fahim.click()
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

#The Boy Who Never Made a Mistake
@pytest.mark.order(13)
def test_mistake ():
    Health = all_data()["HealthTheme"]
    healththeme = driver.find_element(by=By.XPATH, value=Health)
    healththeme.click()
    sleep(2)

    Mistake = all_data()["mistake"]
    story_mistake = driver.find_element(by=By.XPATH, value=Mistake)
    story_mistake.click()
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

#Nazia saves the day
@pytest.mark.order(15)
def test_nazia ():
    Nazia = all_data()["nazia"]
    story_nazia = driver.find_element(by=By.XPATH, value=Nazia)
    story_nazia.click()
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

#How will Rana play?
@pytest.mark.order(16)
def test_rana ():
    Education = all_data()["EducationTheme"]
    educationtheme = driver.find_element(by=By.XPATH, value=Education)
    educationtheme.click()
    sleep(2)

    Rana = all_data()["rana"]
    story_rana = driver.find_element(by=By.XPATH, value=Rana)
    story_rana.click()
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

#A Gift for Grandma
@pytest.mark.order(17)
def test_grandma ():
    Education = all_data()["EducationTheme"]
    educationtheme = driver.find_element(by=By.XPATH, value=Education)
    educationtheme.click()
    sleep(2)

    Grandma = all_data()["grandma"]
    story_grandma = driver.find_element(by=By.XPATH, value=Grandma)
    story_grandma.click()
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

#Let's Find Ammu's Friend
@pytest.mark.order(19)
def test_ammu ():
    Ammu = all_data()["ammu"]
    story_ammu = driver.find_element(by=By.XPATH, value=Ammu)
    story_ammu.click()
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

#Who is the Best Player
@pytest.mark.order(20)
def test_player ():
    Connectivity = all_data()["ConnectivityTheme"]
    connectivitytheme = driver.find_element(by=By.XPATH, value=Connectivity)
    connectivitytheme.click()
    sleep(2)

    Player = all_data()["player"]
    story_player = driver.find_element(by=By.XPATH, value=Player)
    story_player.click()
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

#The Cyclone Adventure
@pytest.mark.order(21)
def test_cyclone ():
    Connectivity = all_data()["ConnectivityTheme"]
    connectivitytheme = driver.find_element(by=By.XPATH, value=Connectivity)
    connectivitytheme.click()
    sleep(2)

    Cyclone = all_data()["cyclone"]
    story_cyclone = driver.find_element(by=By.XPATH, value=Cyclone)
    story_cyclone.click()
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