import unittest
from selenium import webdriver

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver.exe")
browser.get(link)

class TestRegistration1(unittest.TestCase):
    def test_input_field1(self):
        self.assertEqual(browser.find_element_by_css_selector('.first_block .first').send_keys("Constantine"),
        f"Failed to input First name")

    def test_input_field2(self):
        self.assertEqual(browser.find_element_by_css_selector('.first_block .second').send_keys("Fr0ZT"),
        f"Failed to input Last name")

    def test_input_field3(self):
        self.assertEqual(browser.find_element_by_css_selector('.first_block .third').send_keys("newkosss@gmail.com"),
        f"Failed to input First Email")

    def test_input_field4(self):
        self.assertEqual(browser.find_element_by_css_selector('.second_block .first').send_keys("102"),
        f"Failed to input Phone")

    def test_input_field5(self):
        self.assertEqual(browser.find_element_by_css_selector('.second_block .second').send_keys("Odessa"),
        f"Failed to input Address")

    def test_input_button1(self):
        self.assertEqual(browser.find_element_by_css_selector("button.btn").click(),
        f"Failed to click on button")


if __name__ == "__main__":
    unittest.main()
