from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest
import time

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome('/Users/mohammedsoubaneh/Downloads/chromedriver')

    def tearDown(self):
        self.browser.quit()
    # She notices the page title and header mention to-do lists
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        time.sleep(5)
    
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
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

if __name__ == '__main__':
    unittest.main(warnings='ignore')