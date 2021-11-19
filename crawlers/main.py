# ==============================================
#                 Libraries
# ==============================================

import pandas as pd
import time
import warnings
from datetime import datetime
from selenium import webdriver

warnings.filterwarnings("ignore")

# ==============================================
#                   Driver
# ==============================================
driver = webdriver.Chrome("./src/chromedriver")
time.sleep(5)

# ==============================================
#           Accessing the website
# ==============================================
driver.get("https://www.fundsexplorer.com.br/")
elem_funds = driver.find_element_by_xpath(
    '//*[@id="quick-access"]/div[2]/div[1]/div[1]'
).click()

# ==============================================
#    Extracting real estate fund information
# ==============================================

wallet = [
    "HGCR11",
    "XPLG11",
    "KNRI11",
    "HGRU11",
    "TORD11",
    "VINO11",
    "IRDM11",
    "MXRF11",
    "MGFF11",
]

data = []


def extraction_by_xpath(xpath: str, driver=driver) -> str:
    return driver.find_element_by_xpath(xpath).text


def save_data(filename):
    with open(filename, "a") as csv_file:
        df.to_csv(csv_file, sep=";", header=csv_file.tell() == 0, index=False)
    return df


if __name__ == "__main__":
    for element in wallet:
        try:
            elem_funds = driver.find_element_by_name("fii")
            elem_funds.clear()
            elem_funds.send_keys(element)
            driver.find_element_by_xpath(f'//*[@id="item-{element}"]/a/span').click()
            time.sleep(5)

            info = {
                "Data": datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M"),
                "Codigo": extraction_by_xpath(
                    "/html/body/section/section/div/div/div/div[2]/h1"
                ),
                "Preco": extraction_by_xpath(
                    "/html/body/section/section/div/div/div/div[3]/div/span[1]"
                ),
                "Variacao": extraction_by_xpath(
                    "/html/body/section/section/div/div/div/div[3]/div/span[2]"
                ),
                "Liquidez": extraction_by_xpath(
                    "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[1]/span[2]"
                ),
                "Ultimo_Rendimento": extraction_by_xpath(
                    "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[2]/span[2]"
                ),
                "Dividend_Yield": extraction_by_xpath(
                    "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[3]/span[2]"
                ),
                "Patrimonio_Liquido": extraction_by_xpath(
                    "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[4]/span[2]"
                ),
                "Valor_Patrimonial": extraction_by_xpath(
                    "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[5]/span[2]"
                ),
                "Rentabilidade_Mes": extraction_by_xpath(
                    "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[6]/span[2]"
                ),
                "P/VP": extraction_by_xpath(
                    "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[7]/span[2]"
                ),
            }
            data.append(info)
            df = pd.DataFrame.from_dict(data)

            driver.execute_script("window.history.go(-1)")
            time.sleep(2)
        except Exception as e:
            print(f"Os dados não foram coletados: {e}")

    driver.close()

# ==============================================
#    csv file with collected information
# ==============================================

save_data(filename="fundos.csv")
