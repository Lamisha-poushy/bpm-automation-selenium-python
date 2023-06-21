from common import *
from gsconnector import gsconnect

# Open google browser , search Hasina and friends on google.com
@pytest.mark.order(1)
def test_searchkeywards():
    # open google  browser
    driver.maximize_window()
    driver.get('http://www.google.com')

    # search in google.com
    SearchKey = gsconnect().get("SearchKey")
    search = driver.find_element(by=By.NAME, value="q")
    search.send_keys(SearchKey)
    search.send_keys(Keys.RETURN)
    sleep(1)

# click on Hasina and Friends url on google search result
@pytest.mark.order(2)
def test_gotowebsite():
    siteUrl = gsconnect()["webSiteUrl"]
    webSiteUrl = driver.find_element(by=By.XPATH, value=siteUrl)
    webSiteUrl.click()
    sleep(2)

# Avatar select on landing page for age 6 to 9
@pytest.mark.order(3)
def test_selectavatar():
    SelectedAvatar = gsconnect()["SelectedAvatar"]
    avatar = driver.find_element(by=By.XPATH, value=SelectedAvatar)
    avatar.click()
    sleep(2)

# input avatar name
@pytest.mark.order(4)
def test_inputavatarname():
    SelectedAvatarInput = gsconnect()["SelectedAvatarInput"]
    avatar_name = gsconnect()["Name"]
    avatar_name_input = driver.find_element(by=By.XPATH, value=SelectedAvatarInput)
    avatar_name_input.send_keys(avatar_name)
    sleep(2)

# Click on start button
@pytest.mark.order(5)
def test_startbutton():
    StartButton = gsconnect()["StartButton"]
    startbutton = driver.find_element(by=By.XPATH, value=StartButton)
    startbutton.click()
    sleep(2)

# Click on environment theme
@pytest.mark.order(6)
def test_environmenttheme():
    Environment = gsconnect()["EnvironmentTheme"]
    environmenttheme = driver.find_element(by=By.XPATH, value=Environment)
    environmenttheme.click()
    sleep(2)

#the king search of his queen
@pytest.mark.order(7)
def test_hilsa ():
    Hilsa = gsconnect()["hilsa"]
    story_hilsa = driver.find_element(by=By.XPATH, value=Hilsa)
    story_hilsa.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = gsconnect()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = gsconnect()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

#Miss Sonali and Mr. Plastic
@pytest.mark.order(8)
def test_sonali ():
    Environment = gsconnect()["EnvironmentTheme"]
    environmenttheme = driver.find_element(by=By.XPATH, value=Environment)
    environmenttheme.click()
    sleep(2)

    Sonali = gsconnect()["sonali"]
    story_sonali = driver.find_element(by=By.XPATH, value=Sonali)
    story_sonali.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = gsconnect()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = gsconnect()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

# Click on health theme
@pytest.mark.order(9)
def test_healththeme():
    Health = gsconnect()["HealthTheme"]
    healththeme = driver.find_element(by=By.XPATH, value=Health)
    healththeme.click()
    sleep(2)

#The Secret Garden
@pytest.mark.order(10)
def test_garden ():
    Garden = gsconnect()["garden"]
    story_garden = driver.find_element(by=By.XPATH, value=Garden)
    story_garden.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = gsconnect()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = gsconnect()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

#Who will Take Care of Heera
@pytest.mark.order(11)
def test_heera ():
    Health = gsconnect()["HealthTheme"]
    healththeme = driver.find_element(by=By.XPATH, value=Health)
    healththeme.click()
    sleep(2)

    Heera = gsconnect()["heera"]
    story_heera = driver.find_element(by=By.XPATH, value=Heera)
    story_heera.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = gsconnect()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = gsconnect()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

# Click on education theme
@pytest.mark.order(12)
def test_educationtheme():
    Education = gsconnect()["EducationTheme"]
    educationtheme = driver.find_element(by=By.XPATH, value=Education)
    educationtheme.click()
    sleep(2)

#The New Doctor In Town
@pytest.mark.order(13)
def test_doctor ():
    Doctor = gsconnect()["doctor"]
    story_doctor = driver.find_element(by=By.XPATH, value=Doctor)
    story_doctor.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = gsconnect()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = gsconnect()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

#The Window at Meghna’s Room
@pytest.mark.order(14)
def test_heera ():
    Education = gsconnect()["EducationTheme"]
    educationtheme = driver.find_element(by=By.XPATH, value=Education)
    educationtheme.click()
    sleep(2)

    Meghna = gsconnect()["meghna"]
    story_meghna = driver.find_element(by=By.XPATH, value=Meghna)
    story_meghna.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = gsconnect()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = gsconnect()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

# Click on connectivity theme
@pytest.mark.order(15)
def test_connectivitytheme():
    Connectivity = gsconnect()["ConnectivityTheme"]
    connectivitytheme = driver.find_element(by=By.XPATH, value=Connectivity)
    connectivitytheme.click()
    sleep(2)

#There is a New Guest
@pytest.mark.order(16)
def test_guest ():
    Guest = gsconnect()["guest"]
    story_guest = driver.find_element(by=By.XPATH, value=Guest)
    story_guest.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = gsconnect()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = gsconnect()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)

#When Chom Chom Went Missing
@pytest.mark.order(17)
def test_missing ():
    Connectivity = gsconnect()["ConnectivityTheme"]
    connectivitytheme = driver.find_element(by=By.XPATH, value=Connectivity)
    connectivitytheme.click()
    sleep(2)

    Missing = gsconnect()["missing"]
    story_missing = driver.find_element(by=By.XPATH, value=Missing)
    story_missing.click()
    sleep(10)

    #click on bpm logo and back to home page
    BPM = gsconnect()["BPMlogo"]
    bpm_logo = driver.find_element(by=By.XPATH, value=BPM)
    bpm_logo.click()
    sleep(2)

    HomeButton = gsconnect()["Homebutton"]
    home_button = driver.find_element(by=By.XPATH, value=HomeButton)
    home_button.click()
    sleep(2)