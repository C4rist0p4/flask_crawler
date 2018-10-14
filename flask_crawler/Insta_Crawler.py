from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class InstaCrawler:

    def __init__(self, search_object):

        self.url = "https://www.instagram.com/explore/tags/" + search_object
        options = Options()
        options.add_argument("--headless")

        self.driver = Chrome(os.path.dirname(__file__) + '/chromedriver', chrome_options = options)
        self.wait = WebDriverWait(self.driver, 3)

    def crawl(self):

        try:
            self.driver.get(self.url)

            most_popular_posts = self.driver.find_elements_by_class_name('v1Nh3')

            hover = ActionChains(self.driver)
            hover.move_to_element(most_popular_posts[0]).perform()

            try:
                element_click = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_6S0lP')))
            except TimeoutException:
                hover.move_to_element(most_popular_posts[0]).perform()
                element_click = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_6S0lP')))

            element_click.click()

            users_names = []

            cou = 0
            page_arrow_old = ''

            for i in range(len(most_popular_posts)):

                page_arrow = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'coreSpriteRightPaginationArrow')))

                while page_arrow.get_attribute('href') == page_arrow_old:
                    page_arrow = self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow')

                element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'FPmhX')))
                users_names.append(element.text)

                page_arrow_old = page_arrow.get_attribute('href')

                page_arrow.click()

                cou += 1
                if cou == 3:
                    break
            j = self.to_json(users_names)

            return j

        finally:
            self.driver.close()

    def to_json(self, users_names):

        json = []

        for user_name in users_names:

            self.driver.get('https://www.instagram.com/' + user_name)
            user_json = {'name': user_name, 'data': {}}

            user_data = self.driver.find_elements_by_class_name('-nal3')

            for info in user_data:
                data, description = info.text.split(' ')
                user_json['data'].update({description: data})

            json.append(user_json)

        return json
