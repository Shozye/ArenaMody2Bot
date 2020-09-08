from Pages.BasePage import BasePage
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from time import sleep

class BlueArenaPage(BasePage):
    """ Page Object to operate navigation bar
    """

    def __init__(self, browser, user):
        super().__init__(browser, user)

    def go_to(self):
        if self.browser.current_url != self.Url.blue_energy_arena:
            self.logger.debug('Entering blue_energy_arena Page')
            self.browser.get(self.Url.blue_energy_arena)

    def choose_judge(self):
        self.logger.debug('Clicking to judge button')
        self.retry_click(self.Locator.judge_button)

    def decide_winner(self):
        wait = WebDriverWait(self.browser, 60)
        wait.until(EC.element_to_be_clickable(self.Locator.versus_string))
        self.logger.debug('Clicking winner image')
        wait.until(EC.element_to_be_clickable(self.Locator.winner_img_parent))
        self.retry_click(self.Locator.winner_img_parent)
        # self.retry_click(self.Locator.winner)
