try:
    import warnings
    warnings.filterwarnings("ignore")
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    opction = Options()
    opction.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    # opction.add_argument('--headless')
    # opction.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=opction, executable_path=r'D:\CSE_4\webdriver\chromedriver.exe')
    driver.get('https://www.cse.lk/pages/trade-summary/trade-summary.component.html')

except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")

else:
   print ("Written content in the file successfully")
