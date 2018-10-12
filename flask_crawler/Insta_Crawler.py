from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

class Insta_Crawler():

    def crawl(self):
        url = "https://www.instagram.com/explore/tags/sport/"

        options = Options()
        options.add_argument("--headless")

        driver = webdriver.Firefox(firefox_options=options)
        driver.implicitly_wait(5)

        try:

            driver.get(url)

            most_popular_posts = driver.find_elements_by_class_name('v1Nh3')

            users_names = []

            cou = 0
            for i in most_popular_posts:

                driver.execute_script("arguments[0].scrollIntoView();", i)

                hover = ActionChains(driver).move_to_element(i)
                hover.click().perform()

                users_names.append(driver.find_element_by_class_name('FPmhX').text)

                driver.find_element_by_class_name('ckWGn').click()

                cou += 1
                if cou == 3:
                    cou = 0
                    break

            for user_name in users_names:

                driver.get('https://www.instagram.com/' + user_name)

                user_data = driver.find_elements_by_class_name('-nal3')

                print('Name: ' + user_name)

                for info in user_data:
                    print(info.text)

                cou += 1
                if cou == 3:
                    break


            return users_names

        finally:
            driver.quit()
