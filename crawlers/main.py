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

for element in wallet:
    try:
        elem_funds = driver.find_element_by_name("fii")
        elem_funds.clear()
        elem_funds.send_keys(element)
        driver.find_element_by_xpath(f'//*[@id="item-{element}"]/a/span').click()
        time.sleep(3)

        date = datetime.today().strftime("%d-%m-%Y %H:%M")

        cod = driver.find_element_by_xpath(
            "/html/body/section/section/div/div/div/div[2]/h1"
        ).text

        price = driver.find_element_by_xpath(
            "/html/body/section/section/div/div/div/div[3]/div/span[1]"
        ).text

        variation = driver.find_element_by_xpath(
            "/html/body/section/section/div/div/div/div[3]/div/span[2]"
        ).text

        liquidez = driver.find_element_by_xpath(
            "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[1]/span[2]"
        ).text

        last_income = driver.find_element_by_xpath(
            "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[2]/span[2]"
        ).text

        dividend_yield = driver.find_element_by_xpath(
            "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[3]/span[2]"
        ).text

        patrimony = driver.find_element_by_xpath(
            "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[4]/span[2]"
        ).text

        equity_value = driver.find_element_by_xpath(
            "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[5]/span[2]"
        ).text

        profitability_month = driver.find_element_by_xpath(
            "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[6]/span[2]"
        ).text

        p_vp = driver.find_element_by_xpath(
            "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[7]/span[2]"
        ).text

        data.append(
            (
                date,
                cod,
                price,
                liquidez,
                last_income,
                variation,
                dividend_yield,
                patrimony,
                equity_value,
                profitability_month,
                p_vp,
            )
        )

        driver.execute_script("window.history.go(-1)")
        time.sleep(2)
    except Exception as e:
        print(f"Os dados não foram coletados: {e}")

driver.close()

# ==============================================
#    DataFrame with collected information
# ==============================================

df = pd.DataFrame(
    data,
    columns=[
        "Data",
        "Codigo",
        "Preco",
        "Liquidez",
        "Ultimo_Rendimento",
        "Variacao",
        "Dividend_Yield",
        "Patrimonio_Liquido",
        "Valor_Patrimonial",
        "Rentabilidade_mes",
        "P/VP",
    ],
)

df.to_csv("funds.csv", sep=";", index=False)
