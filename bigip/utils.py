import getpass
import time
import subprocess
from pathlib import Path

get_abs_path = lambda rel_path: str((Path(__file__).resolve().parent / rel_path).resolve())

sleep = lambda x=5: time.sleep(x)

class UserAuth:
    def __init__(self):
        # Automatically fetch the current system username
        self._username = getpass.getuser()
        self._password = None  # Password starts as None

    # Getter for username
    @property
    def username(self):
        return self._username

    # Getter for password
    @property
    def password(self):
        return self._password

    def get_password(self):
        self._password = getpass.getpass("Enter password: ")

user = UserAuth()



class MacOSApplicationManager:
    def __init__(self, app_name):
        """
        Initializes the application manager with the application name.
        
        Parameters:
        - app_name (str): The name of the application to manage.
        """
        self.app_name = app_name
        self.close_application()  # Ensures any existing instance of the app is closed before reopening it.

    def __enter__(self):
        """
        Opens the application when entering the context.
        """
        return self.open()

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes the application when exiting the context.
        """
        self.close_application()

    def open(self):
        try:
            subprocess.run(['open', '-a', self.app_name], check=True)
            print(f"Opened {self.app_name}.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to open {self.app_name}. Error: {e}")
        return self
    
    def close_application(self):
        """
        Closes the application by using 'pkill' with the process path if provided.
        """
        try:
            subprocess.run(['pkill', '-f', self.app_name], check=False)
            print(f"Closed {self.app_name}.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to close {self.app_name}. Error: {e}")





