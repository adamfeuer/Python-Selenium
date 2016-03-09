#!/usr/bin/env python

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
# This is the only code you need to edit in your existing scripts.
# The command_executor tells the test to run on Sauce, while the desired_capabilities
# parameter tells us which browsers and OS to spin up.
desired_cap = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "31",
}

sauce_labs_username = os.environ.get('SAUCELABS_USERNAME')
sauce_labs_access_key = os.environ.get('SAUCELABS_ACCESS_KEY')
driver = webdriver.Remote(
   command_executor='http://{}:{}@ondemand.saucelabs.com:80/wd/hub'.format(sauce_labs_username, sauce_labs_access_key),
   desired_capabilities=desired_cap)
 
# This is your test logic. You can add multiple tests here.
driver.implicitly_wait(10)
driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("Sauce Labs")
elem.submit()
print driver.title
 
# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes.
driver.quit()
