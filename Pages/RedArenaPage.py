from Pages.BasePage import BasePage
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


class RedArenaPage(BasePage):
    """ Page Object to operate navigation bar
    """

    def __init__(self, browser, user):
        super().__init__(browser, user)

    def challenge(self):
        self.logger.debug('challenge at red arena')
        self.retry_click(self.Locator.red_arena_challenge)

    def go_to(self):
        if self.browser.current_url != self.Url.red_energy_arena:
            self.browser.get(self.Url.red_energy_arena)