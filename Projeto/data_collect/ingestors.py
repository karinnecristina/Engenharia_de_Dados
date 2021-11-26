# ==============================================
#                 Libraries
# ==============================================
import csv
import os
import pandas as pd
import time
import warnings

from selenium import webdriver
from datetime import datetime
from abc import ABC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


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


class FundsExplorer(ABC):
    def __init__(self, wallet: list[str]) -> None:
        self.wallet = wallet
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(
            os.path.join(DRIVERS_DIR, "chromedriver"), options=self.chrome_options
        )
        self.driver.get("https://www.fundsexplorer.com.br/")

    def _access_website(self) -> None:
        """[Access the interest page]"""
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="quick-access"]/div[2]/div[1]/div[1]'
            ).click()
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, '//*[@id="popup-close-button"]')
                    )
                ).click()
            except:
                pass
        except:
            self.driver.close()

    def extraction_by_xpath(self, xpath: str) -> str:
        """[Extracts text elements from a web page]

        Args:
            xpath (str): [Element path]

        Returns:
            String: [Elements that contain specific text on the page]
        """
        return self.driver.find_element_by_xpath(xpath).text

    def get_data(self) -> list:
        """[Extracts the data of interest]

        Returns:
            List: [List with collected data]
        """
        self._access_website()
        data = []

        for element in self.wallet:
            try:
                elem_funds = self.driver.find_element_by_name("fii")
                elem_funds.clear()
                elem_funds.send_keys(element)
                self.driver.find_element_by_xpath(
                    f'//*[@id="item-{element}"]/a/span'
                ).click()
                time.sleep(5)

                info = {
                    "Data": datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M"),
                    "Codigo": self.extraction_by_xpath(
                        '//*[@id="head"]/div/div/div/div[2]/h1'
                    ),
                    "Preco": self.extraction_by_xpath('//*[@id="stock-price"]/span[1]'),
                    "Variacao": self.extraction_by_xpath(
                        '//*[@id="stock-price"]/span[2]'
                    ),
                    "Liquidez": self.extraction_by_xpath(
                        '//*[@id="main-indicators-carousel"]/div/div/div[1]/span[2]'
                    ),
                    "Ultimo_Rendimento": self.extraction_by_xpath(
                        '//*[@id="main-indicators-carousel"]/div/div/div[2]/span[2]'
                    ),
                    "Dividend_Yield": self.extraction_by_xpath(
                        '//*[@id="main-indicators-carousel"]/div/div/div[3]/span[2]'
                    ),
                    "Patrimonio_Liquido": self.extraction_by_xpath(
                        '//*[@id="main-indicators-carousel"]/div/div/div[4]/span[2]'
                    ),
                    "Valor_Patrimonial": self.extraction_by_xpath(
                        '//*[@id="main-indicators-carousel"]/div/div/div[5]/span[2]'
                    ),
                    "Rentabilidade_Mes": self.extraction_by_xpath(
                        '//*[@id="main-indicators-carousel"]/div/div/div[6]/span[2]'
                    ),
                    "P_VP": self.extraction_by_xpath(
                        '//*[@id="main-indicators-carousel"]/div/div/div[7]/span[2]'
                    ),
                }

                data.append(info)
                self.driver.execute_script("window.history.go(-1)")
                time.sleep(2)

            except Exception as error:
                print(error)
                self.driver.close()

        return data

    def save_data(self, filename: str) -> csv:
        """[Saves the data in a file with a .csv extension]

        Args:
            filename (str): [File name]

        Returns:
            CSV: [File with collected data]
        """
        data = self.get_data()
        self.driver.close()

        with open(os.path.join(DATA_DIR, filename), "a") as csv_file:
            df = pd.DataFrame(data)
            df.to_csv(csv_file, sep=";", header=csv_file.tell() == 0, index=False)
            print("Os dados foram salvos com sucesso!")
        return df
