class UserConfig:
    """Change values according to your preferences
    """

    def __init__(self):
        self.profile_name = 'profile'
        self.username = ''
        self.password = ''
        self.driver_path = None  # if None, then in the same file with Controller
        self.blue_energy_cap = 5
        self.red_energy_cap = 5
        self.wait_for_energy_time = 20*60
