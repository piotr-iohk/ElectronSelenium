from selenium import webdriver
from helpers.env import Env

class ElectronDriver:

    def __init__(self, env = Env.STAGING):
        ports = {
            Env.MAINNET : "9223",
            Env.STAGING: "9223",
            Env.TESTNET: "9223",
        }

        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:" + ports[env]
        self.instance = webdriver.Chrome(chrome_options=opt)



