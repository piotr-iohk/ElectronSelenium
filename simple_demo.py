from selenium import webdriver
from selenium.webdriver.common.by import By

#attach to daedalus
opt = webdriver.ChromeOptions();
opt.debugger_address = "127.0.0.1:9223"
driver = webdriver.Chrome(chrome_options=opt)

# start creating wallet
driver.find_element(By.XPATH, "//button[contains(@class,'SidebarWalletsMenu_addWalletButton')]").click()
driver.find_element(By.CSS_SELECTOR, ".createWalletButton").click()
driver.find_element(By.XPATH, "//input[@name='walletName']").send_keys("Test wallet")

#detach from deadelus
driver.quit()