from UserConfig import UserConfig
from Controler import Controller


def main():
    user = UserConfig()
    control_panel = Controller(user)
    # control_panel.fight()
    control_panel.test_update_status()

if __name__ == '__main__':
    main()
