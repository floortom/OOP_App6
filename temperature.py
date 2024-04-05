from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Temperature:
    """
    A scraper that uses an yaml file to read the xpath of a value needed from the timeanddate.com/weather webpage.
    """

    headers = {
        'pragma':                    'no-cache',
        'cache-control':             'no-cache',
        'dnt':                       '1',
        'upgrade-insecure-requests': '1',
        'user-agent':                'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept':                    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language':           'en-GB,en-US;q=0.9,en;q=0.8',
    }
    baseUrl = "https://www.timeanddate.com/weather/"
    ymlPath = "temperature.yaml"

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        """
        Builds the url string from user input \n
        :return: Url
        """
        url = self.baseUrl + self.country + "/" + self.city
        print(url)
        return url

    def _get_driver(self):
        """
        Set options to make browsing easier \n
        :return: driver object
        """
        options = webdriver.ChromeOptions()
        options.add_argument("disable-infobars")
        options.add_argument("start-minimized")
        options.add_argument("no-sandbox")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("disable-blink-features=AutomationControlled")

        driver = webdriver.Chrome(options=options)
        driver.get(self._build_url())
        return driver

    def _scrape(self):
        """
        Extracts a value \n
        :return: Temperature value
        """
        driver = self._get_driver()
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//*[@id='qlook']/div[contains(@class, 'h2')]")
        # print(element.text)
        return element.text

    def get(self):
        scrapedContent = self._scrape()
        return float(scrapedContent.replace("°C", "").strip())


if __name__ == "__main__":
    temp = Temperature("poland", "warsaw")
    print(temp.get())
