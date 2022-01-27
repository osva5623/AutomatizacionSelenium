import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class hello_world(unittest.TestCase):

    @classmethod
    def  setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="./chromedriver")

    def test_hello_world(self):
        driver=self.driver
        driver.get('https://platzi.com/')
    def test_wikiedia(self):
        self.driver.get('https://es.wikipedia.org/')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='hello-world'))