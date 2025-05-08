import subprocess

import pkg_resources
import sys
from flask_cors import CORS
from utils.settingsreader import propReader

# Path to your requirements.txt file


def check_and_install_requirements():
    requirements_file = 'requirements.txt'
    try:
        # Read the requirements.txt file
        with open(requirements_file, 'r') as file:
            required_packages = file.read().splitlines()

        # Get the list of installed packages
        installed_packages = {pkg.key for pkg in pkg_resources.working_set}

        # Find missing packages
        missing_packages = [pkg for pkg in required_packages if pkg and pkg.split('==')[0] not in installed_packages]

        # Install missing packages
        if missing_packages:
            print(f"Installing missing packages: {missing_packages}")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing_packages])
        else:
            print("All required packages are already installed.")
    except FileNotFoundError:
        print(f"Error: {requirements_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def init_CORS(app):
    origins_array = propReader()["cross_orgins"]
    CORS(app, origins=origins_array)
    # flask_cors.cross_origin(
    #     methods=['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT'],
    #     headers=None,
    #     supports_credentials=False,
    #     max_age=None,
    #     send_wildcard=True,
    #     always_send=True,
    #     automatic_options=False
    #     )
