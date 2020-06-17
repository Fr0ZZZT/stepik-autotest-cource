import unittest
from selenium import webdriver

browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")

class TestRegistration1(unittest.TestCase):
    def test_input1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Constantine")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Fr0ZT")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("newkosss@gmail.com")
        input4 = browser.find_element_by_css_selector('.second_block .first')
        input4.send_keys("102")
        input4 = browser.find_element_by_css_selector('.second_block .second')
        input4.send_keys("Odessa")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, welcome_text_elt.text, "Congrats text should be equal")


if __name__ == "__main__":
    unittest.main()