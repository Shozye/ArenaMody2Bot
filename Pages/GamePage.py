from Pages.BasePage import BasePage
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


class GamePage(BasePage):
    """ Page Object to operate navigation bar
    """

    def __init__(self, browser, user):
        super().__init__(browser, user)
        self.player_info = self.get_player_info()

    def turn_off_cookies_notification(self):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(self.Locator.cookies_button)
            )
            self.retry_click(self.Locator.cookies_button)
        except selenium.common.exceptions.TimeoutException:
            self.logger.debug('Cookies notification didn\'t show up')
            pass

    def is_at(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.Locator.chat_button))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False

    def get_player_info(self):
        by, value = self.Locator.info_dict
        script = self.browser.find_elements(by, value)[1].get_attribute('innerHTML')
        return json.loads(script.split('.setLadyStats(')[1].split('})')[0] + "}")

    def my_money(self):
        return int(self.player_info['dollars'])

    def my_blue_energy(self):
        return int(self.player_info['energyPageant']['ladyEnergy'])

    def my_red_energy(self):
        return int(self.player_info['energyArena']['ladyEnergy'])

    def my_emeralds(self):
        return int(self.player_info['emeralds'])
