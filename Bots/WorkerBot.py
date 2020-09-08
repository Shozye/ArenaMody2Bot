from Bots.BaseBot import BaseBot
from Pages.GamePage import GamePage
from Pages.RedArenaPage import RedArenaPage
from Pages.BlueArenaPage import BlueArenaPage
import logging
import time


class WorkerBot(BaseBot):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def duel_fight(self):
        red_arena_page = RedArenaPage(self.browser, self.user)
        red_arena_page.go_to()
        red_arena_page.challenge()

    def judge(self):
        blue_arena_page = BlueArenaPage(self.browser, self.user)
        blue_arena_page.go_to()
        blue_arena_page.choose_judge()
        blue_arena_page.decide_winner()
        pass

