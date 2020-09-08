from Pages.StartPage import StartPage
from Pages.GamePage import GamePage
from Pages.BasePage import BasePage
from math import floor
from math import ceil
import logging
import csv
import os


class BaseBot:
    def __init__(self, browser, user):
        self.browser = browser
        self.user = user
        self.stats = None
        self.money = None
        self.emeralds = None
        self.red_energy = None
        self.red_energy_regen_time = None
        self.blue_energy_regen_time = None
        self.blue_energy = None
        self.level = None
        self.logger = logging.getLogger('main')

    def login(self):
        """If WebDriver is not logged in, bot will log in to arenamody.pl with login/password from UserConfig.py
        """
        start_page = StartPage(self.browser, self.user)
        start_page.go_to()
        start_page.open_login_form()
        start_page.type_username()
        start_page.type_password()
        start_page.submit_login()
        game_page = GamePage(self.browser, self.user)
        game_page.refresh()
        # game_page.turn_off_cookies_notification()

    def is_in_game(self):
        """
        :return: True if Web driver is at logged in and at site arenamody.pl
        """
        game_page = GamePage(self.browser, self.user)
        return game_page.is_at()

    def refresh(self):
        base_page = BasePage(self.browser, self.user)
        base_page.refresh()

    def update_money(self):
        game_page = GamePage(self.browser, self.user)
        self.money = game_page.my_money()

    def update_emeralds(self):
        game_page = GamePage(self.browser, self.user)
        self.emeralds = game_page.my_emeralds()

    def update_blue_energy(self):
        game_page = GamePage(self.browser, self.user)
        self.blue_energy = game_page.my_blue_energy()

    def update_red_energy(self):
        game_page = GamePage(self.browser, self.user)
        self.red_energy = game_page.my_red_energy()

    def update_status(self):
        """Updates money, emeralds, energy, level and put them into bot attributes.
        """
        self.refresh()
        game_page = GamePage(self.browser, self.user)
        self.money = game_page.my_money()
        self.emeralds = game_page.my_emeralds()
        self.blue_energy = game_page.my_blue_energy()
        self.red_energy = game_page.my_red_energy()
        self.logger.debug('Successfully updated status')
        self.logger.debug(f'money={self.money}, emeralds={self.emeralds}, blue_energy={self.blue_energy}, red_energy={self.red_energy}')

    def quit(self):
        self.browser.quit()

