from selenium.webdriver.common.by import By
from page_objects.page import Element


class SidebarMenu:

    def __init__(self, driver):
        self.driver = driver

        self.add_wallet_button = Element(self.driver, By.XPATH, "//button[contains(@class,'SidebarWalletsMenu_addWalletButton')]")
        self.show_wallets_button = Element(self.driver, By.XPATH, "//button[@class='SidebarCategory_component SidebarCategory_active']")

    def get_wallet_by_name(self, name):
        return Element(self.driver, By.XPATH, "//span[@class='SidebarWalletMenuItem_title' and text()='"+name+"']")


class WalletNavMenu:

    def __init__(self, driver):
        self.driver = driver


    def get_wallet_nav_item(self, name):
        nav_items = {
            "Summary"      : "[1]",
            "Send"         : "[2]",
            "Receive"      : "[3]",
            "Transactions" : "[4]",
            "Settings"     : "[5]",
        }

        return Element(self.driver, By.XPATH, "//div[@class='WalletNavigation_navItem']" + nav_items[name])

