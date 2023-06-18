import undetected_chromedriver as uc
import time
from selenium.webdriver.common.keys import Keys


chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("user-data-dir=E:/selenium/session/")
browser = uc.Chrome(options=chrome_options)
browser.delete_all_cookies()

# Getting url
browser.get('https://terabox.com/webmasterSharefile')
time.sleep(12)
Tperiod = browser.find_element(by='class name', value='u-input__inner').click()
time.sleep(1)
Tperiod.send_keys(Keys.ARROW_DOWN)
Tperiod.send_keys(Keys.ARROW_DOWN)
Tperiod.send_keys(Keys.ARROW_DOWN)
Tperiod.send_keys(Keys.ARROW_DOWN)
Tperiod.send_keys(Keys.ENTER)

Tperiod = browser.find_element(by='class name', value='.add-button').click()

time.sleep(1000)