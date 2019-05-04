#### open python.org site and search text

            from selenium import webdriver
            # keyboard input
            from selenium.webdriver.common.keys import Keys
            driver = webdriver.Firefox()  # driver = webdriver.Chrome() # use firefox or chrome
            driver.get("http://www.python.org")
            assert "Python" in driver.title
            # goto search textbox
            elem = driver.find_element_by_name("q")
            # clear old text if there is any
            elem.clear()
            # write text 'pycon' in search field, keys refer to keyboard
            elem.send_keys("pycon")
            # using Keys.ENTER or Keys.RETURN to submit search text
            elem.send_keys(Keys.RETURN)
            # confirm it has results
            # page source : html
            assert "No results found." not in driver.page_source
            import time
            time.sleep(5)
            driver.close()




#### using unittest

            import unittest
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys

            class PythonOrgSearch(unittest.TestCase):
                def setUp(self):
                    self.driver = webdriver.Firefox()

                def test_search_in_python_org(self):
                    driver = self.driver
                    driver.get("http://www.python.org")
                    self.assertIn("Python",driver.title)
                    elem = driver.find_element_by_name('q')
                    elem.send_keys('pycon')
                    elem.send_keys(Keys.RETURN)
                    assert "No results found." not in driver.page_source

                def tearDown(self):
                    import time
                    time.sleep(5) #wait for 5 seconds before close
                    self.driver.close()

            if __name__ == '__main__':
                unittest.main()


            # output : 
            # ----------------------------------------------------------------------
            # Ran 1 test in 13.799s
            # 
            # OK
