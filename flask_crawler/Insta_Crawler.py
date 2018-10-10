from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class Insta_Crawler():

    def crawl(self):
        url = "https://www.amazon.com"

        options = Options()
        options.add_argument("--headless")

        driver = webdriver.Firefox(firefox_options=options)
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)

        driver.get(url)

        search_bar = driver.find_element_by_id('twotabsearchtextbox')

        search_bar.send_keys('blueray movies 2018')

        search_bar.submit()

        items = driver.find_elements_by_xpath("//li[contains(@id, 'result_')]")

        item_list = []

        for item in items:
            title = item.find_element_by_xpath(
                ".//h2[contains(@class, 'a-size-medium') and contains(@class, 's-inline')"
                "and contains(@class, 's-access-title') and contains(@class, 'a-text-normal')]")

            prices = item.find_elements_by_xpath(".//span[contains(@class, 'sx-price-whole')]")
            prices_fractional = item.find_elements_by_xpath(".//sup[contains(@class, 'sx-price-fractional')]")
            items_info = item.find_elements_by_xpath(".//h3[contains(@data-attribute, '4K')"
                                                      "or contains(@data-attribute, 'Blu-ray')"
                                                      "or contains(@data-attribute, 'DVD')]")

            for price, price_fractional, item_in in zip(prices, prices_fractional, items_info):
                item_list.append({
                    'title': title.get_attribute('data-attribute'),
                    'attribute':  item_in.get_attribute('data-attribute'),
                    'price':  price.text + ',' + price_fractional.text + '$'})

        driver.quit()

        return item_list


