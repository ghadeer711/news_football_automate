from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


WEB_URL = "https://www.thesun.co.uk/sport/football/"

CHROME_DRIVER_PATH = (
    r"C:\Users\USER\Downloads\chromedriver-win64"
    r"\chromedriver-win64\chromedriver.exe"
)


def scrape_news():
    driver = None
    news_list = []

    try:
        service = Service(executable_path=CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=service)

        driver.get(WEB_URL)
        driver.implicitly_wait(10)

        containers = driver.find_elements(
            By.XPATH,
            "//div[@class='story__copy-container']"
        )

        for container in containers:
            title_elements = container.find_elements(
                By.XPATH,
                "./a/h3"
            )

            subtitle_elements = container.find_elements(
                By.XPATH,
                "./a/p"
            )

            link_elements = container.find_elements(
                By.XPATH,
                "./a"
            )

            title = (
                title_elements[0].text.strip()
                if title_elements
                else ""
            )

            subtitle = (
                subtitle_elements[0].text.strip()
                if subtitle_elements
                else ""
            )

            link = (
                link_elements[0].get_attribute("href")
                if link_elements
                else ""
            )

            news_list.append({
                "title": title,
                "subtitle": subtitle,
                "link": link
            })

        return news_list

    except WebDriverException as error:
        raise RuntimeError(
            f"Failed to scrape news from the website: {error}"
        ) from error

    finally:
        if driver is not None:
            driver.quit()