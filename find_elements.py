import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="./chromedriver")
        driver=self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

    def test_search(self):
        search_file= self.driver.find_element_by_id('search')

    def test_search_field_by_name(self):
        search_file_name= self.driver.find_element_by_name('q')

    def test_search_field_by_class_name(self):
        search_file_name= self.driver.find_elements_by_class_name('button')
    
    def test_vip_promo(self):
        vip_promo=self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    def test_selector_css(self):
        css_selector=self.driver.find_elements_by_css_selector('div.header-minicart span.icon')

    def test_count_images_promo(self):
        banner_list=self.driver.find_element_by_class_name('promos')
        banners=banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3,len(banners))

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)

