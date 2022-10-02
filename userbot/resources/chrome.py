import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


async def chrome(chrome_options=None):
    if chrome_options is None:
        chrome_options = await options()
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.mkdir(Config.TMP_DOWNLOAD_DIRECTORY)
    prefs = {"download.default_directory": Config.TMP_DOWNLOAD_DIRECTORY}
    chrome_options.add_experimental_option("prefs", prefs)
    return webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )


async def options():
    chrome_options = Options()
    chrome_options.binary_location = Config.CHROME_BIN
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    return chrome_options
