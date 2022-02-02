import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="./chromedriver")
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()        
        driver.get('http://demo-store.seleniumacademy.com/')

    def select_language(self):
        exp_options=['English','French','German']
        act_options=[]
        select_language=Select(self.driver.find_elements_by_id('select-language'))

        for option in select_language.options:
            act_options.append(option)

        self.assertLessEqual(exp_options,act_options)
        self.assertEqual('Englis',select_language.first_selected_option.text)
        select_language.select_by_visible_text('German')
        self.assertTrue('store=german',self.driver.current_url)
        select_language.select_by_index(0)


    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)