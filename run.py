from UserConfig import UserConfig
from Controler import Controller
from time import sleep

def main():
    user = UserConfig()
    control_panel = Controller(user)
    try:
        control_panel.fight_and_judge()
    except Exception:
        control_panel.quit_browser()
        sleep(user.wait_if_exception)
        main()


if __name__ == '__main__':
    main()
