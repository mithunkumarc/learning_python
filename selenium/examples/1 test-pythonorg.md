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
