from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import reverse_geocoder as rg
import pprint
from iso3166 import countries
import ast


import time

def getLocation():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Firefox()
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    l1=(latitude,longitude)
    #return (latitude,longitude)
    return (l1)
#print(getLocation())
def reverseGeocode(coordinates):
    result = rg.search(coordinates)
    #pprint.pprint(result)
    return result

def refresh_location():
    coor = getLocation()
    l1 = (coor[0], coor[1])
    # print(l1)
    cloc = reverseGeocode(l1)[0]
    # print(cloc)
    Contt = countries.get(cloc.get('cc'))
    # print(countries.get(cloc.get('cc')))
    deta = str(l1) + "\n" + str(cloc) + "\n" + (Contt[0])
    open("%%tem_data%%", 'w').write(deta)
    print(deta)
    print('Refresh Location RUN')

def loc_info():
    raw_data = open('%%tem_data%%', 'r').read()
    raw_data = raw_data.split('\n')
    coordinates=eval(raw_data[0])
    location=ast.literal_eval(raw_data[1])
    address='\n'+raw_data[2]+'\n'+location.get('admin1')+'\n'+location.get('name')+'\n'
    data={'coordinates':coordinates,'location':location,'country':raw_data[2],'state':location.get('admin1'),'city':location.get('name'),'addr':address}
    return data

#location=loc_info()
#print(location.get('country'))
#refresh_location()