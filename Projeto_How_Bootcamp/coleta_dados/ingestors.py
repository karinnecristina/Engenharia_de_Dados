# ==============================================
#                 Libraries
# ==============================================
import csv
import os
import pandas as pd
import time
import warnings
from selenium import webdriver

warnings.filterwarnings("ignore")

# ==============================================
#           Folders and Subfolders
# ==============================================

BASE_DIR = os.path.join(os.path.abspath("."))
DATA_DIR = os.path.join(BASE_DIR, "./data")
DRIVERS_DIR = os.path.join(BASE_DIR, "./drivers")


# ==============================================
#           Accessing the website
# ==============================================


driver = webdriver.Chrome(os.path.join(DRIVERS_DIR, "chromedriver"))
time.sleep(5)

driver.get("https://www.fundsexplorer.com.br/")


def extraction_by_xpath(xpath: str, driver=driver) -> str:
    return driver.find_element_by_xpath(xpath).text


def save_data(filename: str, file: list) -> csv:
    with open(os.path.join(DATA_DIR, filename), "a") as csv_file:
        df = pd.DataFrame.from_dict(file)
        df.to_csv(csv_file, sep=";", header=csv_file.tell() == 0, index=False)
    return df
