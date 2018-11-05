from selenium.webdriver.common.by import By
from page_objects.page import Page
from page_objects.page import Element
from page_objects.page_fragments import SidebarMenu
from page_objects.page_fragments import WalletNavMenu

class Wallet(Page):
    def __init__(self, driver, name):
        super().__init__(driver)

        self.name = name

        self.sidebar_menu = SidebarMenu(self.driver)
        self.wallet_menu = WalletNavMenu(self.driver)

    def open_wallet(self):
        self.sidebar_menu.get_wallet_by_name(self.name).click()

    def go_to(self, wallet_function):
        self.open_wallet()
        self.wallet_menu.get_wallet_nav_item(wallet_function).click()

        if wallet_function == WalletFunctions.Settings:
            return WalletSettingsPage(self.driver)

        raise Exception("Wallet function not supported: " + wallet_function)

    def delete_wallet(self):
        self.go_to("Settings").delete_wallet(self.name)

class WalletFunctions(object):
    Summary       = "Summary"
    Send          = "Send"
    Receive       = "Receive"
    Transactions  = "Transactions"
    Settings      = "Settings"


class WalletSettingsPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

        self.sidebar_menu = SidebarMenu(self.driver)
        self.wallet_menu = WalletNavMenu(self.driver)
        self.delete_wallet_button = Element(self.driver, By.CSS_SELECTOR, ".DeleteWalletButton_button")


    def delete_wallet(self, name):
        self.delete_wallet_button.click()
        delete_modal = DeleteWalletModal(self.driver)
        delete_modal.delete_wallet(name)


class DeleteWalletModal(Page):

    def __init__(self, driver):
        super().__init__(driver)

        self.confirm_checkbox = Element(self.driver, By.CSS_SELECTOR, "[type='checkbox']")
        self.wallet_name_input = Element(self.driver, By.XPATH, "//input[@class='SimpleInput_input' and @label='Enter the name of the wallet to confirm deletion:']")
        self.delete_button = Element(self.driver, By.XPATH, "//button[@label='Delete']")

    def delete_wallet(self, name):
        self.confirm_checkbox.click()
        self.wallet_name_input.type(name)
        self.delete_button.click()