# ==============================================
#                 Libraries
# ==============================================
import warnings
from selenium import webdriver

warnings.filterwarnings("ignore")

# ==============================================
#                   Driver
# ==============================================
driver = webdriver.Chrome("./src/chromedriver")

# ==============================================
#           Accessing the website
# ==============================================
driver.get("https://www.fundsexplorer.com.br/")
elem_funds = driver.find_element_by_xpath(
    '//*[@id="quick-access"]/div[2]/div[1]/div[1]'
).click()

# ==============================================
#          Clearing the search bar
# ==============================================
elem_funds = driver.find_element_by_name("fii")
elem_funds.clear()

# ==============================================
#        Searching a real estate fund
# ==============================================
elem_funds.send_keys("HGLG11")

# ==============================================
#    Extracting real estate fund information
# ==============================================
elem_cmb = driver.find_element_by_xpath('//*[@id="item-HGLG11"]/a/span').click()

price = driver.find_element_by_xpath(
    "/html/body/section/section/div/div/div/div[3]/div/span[1]"
).text
liquidez = driver.find_element_by_xpath(
    "/html/body/section/div[1]/section[1]/div/div/div/div/div/div[1]/span[2]"
).text

# ==============================================
#     Closing the connection to the website
# ==============================================
driver.close()

print(
    """
preço: {}
liquidez: {}""".format(
        price, liquidez
    )
)
