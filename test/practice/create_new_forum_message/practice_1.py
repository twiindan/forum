__author__ = 'arobres'


#### BUILD THE JSON AND SEND A REQUEST TO THE FORUM SERVER TO CREATE A MESSAGE

# URL = http://localhost:8081/v1.0/forum

""" BODY = {'theme': <string>,
            'subject': <string>,
            'message': <string>
            }
"""

# THE RESPONSE SHOULD BE 200 WITH THE STRING REPSONSE "message created"

# THEME SHOULD BE ONE OF THE FOLLOWING: ['security', 'development', 'automation', 'testing']
# REMEMBER VERIFY THE RESPONSE STATUS CODE AND CONTENT.

#### INSERT HERE YOUR CODE  ####




import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()






