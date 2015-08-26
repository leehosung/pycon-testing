import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PyconUserTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_log_in_pycon_2015(self):
        driver = self.driver
        driver.get("http://www.pycon.kr/2015/login")

        # US1 : 사용자는 Pycon Korea 2015 페이지 제목을 볼 수 있습니다.
        self.assertIn("PyCon Korea 2015", driver.title)

        # US2 : 사용자는 로그인을 할 수 있습니다.
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("lee.ho.sung@gmail.com")
        elem.send_keys(Keys.RETURN)
        self.assertIn("One-time login token url was sent to your mail",
                      driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(warnings='ignore')
