from selenium.webdriver.common.by import By


class Constant:
    """That Class is used to easier introduce changes to code
    It also helps in readability of code.
    """
    def __init__(self):
        self.Locator = self.Locator()
        self.Url = self.Url()
        self.Script = self.Script()

    class Locator:
        def __init__(self):
            # BasePage
            # ChallengePage

            # GamePage
            self.info_dict = (By.CSS_SELECTOR, "div script[type='text/javascript']")
            self.chat_button = (By.ID, 'js-chat-toggle-button')
            self.dollars = (By.ID, 'player-dollars')
            self.emeralds = (By.ID, 'player-emeralds')
            self.level = (By.ID, 'currentLevel')
            self.red_energy = (By.CSS_SELECTOR, 'span.player-energy-value span.energy-arena-value')
            self.blue_energy = (By.CSS_SELECTOR, 'span.player-energy-value span.energy-bp-value')
            # RankPage
            # StartPage
            self.login_button = (By.ID, 'login-btn')
            self.cookies_button = (By.CSS_SELECTOR, 'div>a.cc_btn.cc_btn_accept_all')
            self.user_field = (By.NAME, 'login_user')
            self.pass_field = (By.NAME, 'login_pass')
            self.submit_login = (By.ID, 'loginSubmit')
            # WorkPage

    class Url:
        def __init__(self):
            self.start_page = 'https://arenamody.pl'
            self.blue_energy_arena = 'https://g.arenamody.pl/beauty_pageant.php'
            self.red_energy_arena = 'https://g.arenamody.pl/duels.php'

    class Script:
        def __init__(self):
            pass