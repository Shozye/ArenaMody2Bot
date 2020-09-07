from Bots.BaseBot import BaseBot
from Pages.GamePage import GamePage
import logging
import time


class WorkerBot(BaseBot):
    def __init__(self, browser, user):
        super().__init__(browser, user)

    def duel_fight(self):
        pass

    def judge(self):
        pass

