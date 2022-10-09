from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

browser = webdriver.Chrome('/Users/mohammedsoubaneh/Downloads/chromedriver')
browser.get('http://localhost:8000')
time.sleep(5)

# She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a textbox(Edith's hobby is tying fly fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly"(Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will rememeber her list. Then she sees
# that the site has generated a unique URL for her -- there is some explanatory
# text to that effect

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep

browser.quit()