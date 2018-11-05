from selenium.webdriver.common.by import By
from page_objects.page import Page
from page_objects.page import Element
from page_objects.page_fragments import SidebarMenu


class AddWalletPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

        self.sidebar_menu = SidebarMenu(self.driver)
        self.create_wallet_button = Element(self.driver, By.CSS_SELECTOR, ".createWalletButton")
        self.restore_wallet_button = Element(self.driver, By.CSS_SELECTOR, ".restoreWalletButton")
        self.wallet_name_input = Element(self.driver, By.XPATH, "//input[@name='walletName']")




    def create_wallet(self, name, passw):
        self.sidebar_menu.add_wallet_button.click()
        self.create_wallet_button.click()

        wallet_modal = CreateWalletModal(self.driver)
        wallet_modal.wallet_name_input.type(name)
        wallet_modal.password_input.type(passw)
        wallet_modal.password_repeat_input.type(passw)
        wallet_modal.create_wallet_button.click()

        recovery_modal = RecoveryPhraseModal(self.driver)
        recovery_modal.recovery_phrase_checkbox.click()
        recovery_modal.continue_button.click()
        mnemonics = recovery_modal.recovery_phrase_mnemonics.get_text().split()
        recovery_modal.yes_confirm_button.click()

        for word in mnemonics:
            recovery_modal.get_mnemonic(word).click()

        recovery_modal.final_recovery_checkbox1.click()
        recovery_modal.final_recovery_checkbox2.click()
        recovery_modal.confirm_button.click()



class CreateWalletModal(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.wallet_name_input = Element(self.driver, By.XPATH, "//input[@name='walletName']")
        self.password_switch_on = Element(self.driver, By.XPATH, "")
        self.password_switch_off = Element(self.driver, By.XPATH, "")
        self.password_input = Element(self.driver, By.XPATH, "//input[@name='spendingPassword']")
        self.password_repeat_input = Element(self.driver, By.XPATH, "//input[@name='repeatPassword']")
        self.create_wallet_button = Element(self.driver, By.XPATH, "//button[@label='Create personal wallet']")


class RecoveryPhraseModal(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.recovery_phrase_checkbox = Element(self.driver, By.CSS_SELECTOR, ".SimpleCheckbox_check")
        self.continue_button = Element(self.driver, By.XPATH, "//button[@label='Continue']")
        self.recovery_phrase_mnemonics = Element(self.driver, By.CSS_SELECTOR, ".WalletRecoveryPhraseMnemonic_component")
        self.yes_confirm_button = Element(self.driver, By.XPATH, "//button[@label='Yes, I have written it down.']")
        self.final_recovery_checkbox1 = Element(self.driver, By.XPATH, "//div[@class='WalletRecoveryPhraseEntryDialog_checkbox'][1]/div/input")
        self.final_recovery_checkbox2 = Element(self.driver, By.XPATH, "//div[@class='WalletRecoveryPhraseEntryDialog_checkbox'][2]/div/input")
        self.confirm_button = Element(self.driver, By.XPATH, "//button[@label='Confirm']")

    def get_mnemonic(self, word):
        return Element(self.driver, By.XPATH, "//button[text()='" + word + "']")