import unittest
from helpers.drivers import ElectronDriver
from page_objects.add_wallet import AddWalletPage
from page_objects.wallet import Wallet

class CreateWallet(unittest.TestCase):

    def setUp(self):
        self.driver = ElectronDriver()


    def test_create_wallet(self):
        add_wallet_screen = AddWalletPage(self.driver.instance)
        add_wallet_screen.create_wallet(name="nowy2", passw="Zaq123edc")

    def test_delete_wallet(self):
        wallet = Wallet(self.driver.instance, name="nowy2")
        wallet.delete_wallet()

    def tearDown(self):
        self.driver.instance.quit()

if __name__ == '__main__':
    unittest.main()
