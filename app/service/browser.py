"""
Browser Service
"""
import time
import json
from typing import Any

from selenium import webdriver
from selenium.webdriver.common.by import By


class Browser():
    """Instance a Browser
    """
    def __init__(self):
        self.driver = None
        self.url = None

    def instance(self):
        self.driver = webdriver.Firefox()

    def get_local_storage(self, key: str, value: Any):
        if type(value) == dict:
            value = json.dumps(value)
        return  f"window.localStorage.setItem('{key}', '{value}');"
        # self.driver.execute_script(script)

    def go_to_kalea(self, item_label: str):
        """Driving to kalea
        """
        self.driver.get(url="https://kaleamarket.com/select-store")
        script = self.get_local_storage(
            key='store-location',
            value={"id":"pfvswBTKMD0JMgHsvEEv","name":"Valencia"}
        )
        self.driver.execute_script(script)
        script = self.get_local_storage(
            key='searchType',
            value='products'
        )
        self.driver.execute_script(script)
        self.url = f'https://kaleamarket.com/search-results?searchQuery={item_label}&searchType=products&category='
        self.driver.get(url=self.url)

    def kalea_expand_results(self, iterations: int = 3):
        xpath = '/html/body/app-root/app-full-navigation/div[1]/app-search-results/div/button'
        # element = self.driver.find_element_by_xpath(xpath)  # Deprecation
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        print(f'I got an element: {element}')
        if element:
            for _ in range(iterations):
                    element.click()

    def quit(self):
        self.driver.quit()


# b = Browser()
# b.instance()
# b.go_to_kalea(item_label='agua')
# # Debatible
# time.sleep(2.5)
# b.kalea_expand_results()
# # b.fetch()

# b.quit()
