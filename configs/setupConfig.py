
import subprocess
from utils.filehandling import create_netslocation
import pkg_resources
import sys
from utils.settingsreader import propReader
from utils.commons import StartUP_LOGO

access_json=propReader()
nested_loging = f'{access_json["file_location"]}{access_json["appname"]}/log'
def setUpingFolders(): 
    print(StartUP_LOGO)
    create_netslocation(nested_loging)

def check_and_install_requirements():
    requirements_file = 'requirements.txt'
    try:
        # Read the requirements.txt file
        install_package("setuptools")
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

def install_package(package_name):
    """Installs a Python package using pip."""
    try:
        # Use sys.executable to ensure the correct Python interpreter's pip is used
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")