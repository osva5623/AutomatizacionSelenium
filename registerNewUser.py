import unittest
from selenium import webdriver


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="./chromedriver")
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()        
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver=self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()
        
        create_account_button=driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_button.is_displayed()and create_account_button.is_enabled())
        create_account_button.click()
        self.assertEqual('Create New Customer Account', driver.title)
        first_name=driver.find_element_by_id('firstname')
        middle_name=driver.find_element_by_id('middlename')
        last_name=driver.find_element_by_id('lastname')
        email=driver.find_element_by_id('email_address')
        password=driver.find_element_by_id('password')
        confirm_password=driver.find_element_by_id('confirmation')
        submit_button=driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button')
        
        self.assertTrue(first_name.is_enabled()
            and middle_name.is_enabled()
            and last_name.is_enabled()
            and email.is_enabled()
            and password.is_enabled()
            and confirm_password.is_enabled()
            and submit_button.is_enabled()
        )

        first_name.send_keys('oswaldo')
        middle_name.send_keys('perez')
        last_name.send_keys('rosas')
        email.send_keys('oswaldo.rosas@gmail.com')
        password.send_keys('123456789')
        confirm_password.send_keys('123456789')
        driver.implicitly_wait(1)
        submit_button.click()



    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)