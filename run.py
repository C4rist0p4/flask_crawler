from flask import Flask, render_template, jsonify
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import json

app = Flask(__name__)

test_json = {
    'id': 1,
    'name': u'test',
    'preis': 55
}

@app.route('/', methods=['GET'])
def hello():

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

    for item in items:
        title = item.find_element_by_xpath(".//h2[contains(@class, 'a-size-medium') and contains(@class, 's-inline')"
                                           "and contains(@class, 's-access-title') and contains(@class, 'a-text-normal')]")

        prices = item.find_elements_by_xpath(".//span[contains(@class, 'sx-price-whole')]")
        prices_fractional = item.find_elements_by_xpath(".//sup[contains(@class, 'sx-price-fractional')]")
        items_infos = item.find_elements_by_xpath(".//h3[contains(@data-attribute, '4K')"
                                                  "or contains(@data-attribute, 'Blu-ray')"
                                                  "or contains(@data-attribute, 'DVD')]")

    json_string = ''

    for price, price_fractional, item_info in zip(prices, prices_fractional, items_infos):
        json_string += json.dumps({
            'Title':  u''+title.get_attribute('data-attribute'),
            'Formart': u''+item_info.get_attribute('data-attribute'),
            'Preis': price.text + "," + price_fractional.text + "$"
        })

    return jsonify(json_string)

    driver.quit()