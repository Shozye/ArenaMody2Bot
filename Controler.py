import os
from selenium import webdriver
from Bots.WorkerBot import WorkerBot
from logger import config_logging
from time import sleep
import logging


class Controller:
    """
    Using one of methods in this class should be enough to run bot
    Names of the methods should clearly state what actions bot is going to take
    They should be run at run.py
    """

    def __init__(self, user):
        config_logging()
        self.user = user
        self.driver_path = user.driver_path if user.driver_path else os.path.join(os.getcwd(), 'chromedriver.exe')

        self.logger = logging.getLogger('main')
        self.logger.info('Bot has started, user profile is ' + self.user.profile_name)

        self.browser = webdriver.Chrome(self.driver_path)
        self.browser.maximize_window()
        self.browser.implicitly_wait(0.5)

    def fight(self):
        try:
            self.logger.info('fight method executed')
            bot = WorkerBot(self.browser, self.user)
            bot.login()
            while True:
                bot.update_status()
                if bot.red_energy > self.user.red_energy_cap:
                    bot.duel_fight()
                elif bot.blue_energy > self.user.blue_energy_cap:
                    bot.judge()
                else:
                    wait_time = self.user.wait_for_energy_time
                    sleep(wait_time)
        except Exception:
            self.logger.critical('fight thrown exception', exc_info=True)
            raise

    def test_update_status(self):
        try:
            self.logger.info('test_update_status method executed')
            bot = WorkerBot(self.browser, self.user)
            bot.login()
            bot.update_status()
            while True:
                bot.update_status()
        except Exception:
            self.logger.critical('test_update_status thrown exception', exc_info=True)
            raise
