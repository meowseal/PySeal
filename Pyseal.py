#8 888888888o  `8.`8888.      ,8' d888888o.   8 8888888888            .8.          8 8888         
#8 8888    `88. `8.`8888.    ,8'.`8888:' `88. 8 8888                 .888.         8 8888         
#8 8888     `88  `8.`8888.  ,8' 8.`8888.   Y8 8 8888                :88888.        8 8888         
#8 8888     ,88   `8.`8888.,8'  `8.`8888.     8 8888               . `88888.       8 8888         
#8 8888.   ,88'    `8.`88888'    `8.`8888.    8 888888888888      .8. `88888.      8 8888         
#8 888888888P'      `8. 8888      `8.`8888.   8 8888             .8`8. `88888.     8 8888         
#8 8888              `8 8888       `8.`8888.  8 8888            .8' `8. `88888.    8 8888         
#8 8888               8 8888   8b   `8.`8888. 8 8888           .8'   `8. `88888.   8 8888         
#8 8888               8 8888   `8b.  ;8.`8888 8 8888          .888888888. `88888.  8 8888         
#8 8888               8 8888    `Y8888P ,88P' 8 888888888888 .8'       `8. `88888. 8 888888888888 


# Modules
import sys
import subprocess
import os

# install module through subprocess
def install(module):
    # load in a module
    package_to_install = module
    try:
        result = subprocess.run(
            # Talk to the system to install a package through pip
            [sys.executable, "-m", "pip", "install", package_to_install],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"Successfully installed {package_to_install}.")
        print("STDOUT:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_to_install}:")
        print("STDERR:", e.stderr)
    except FileNotFoundError:
        print(f"Error: Python executable not found at {sys.executable}")



# Load in Colorama
print("Initializing Modules...")
try:
    from colorama import Fore, Back, Style
    import keyboard
except ModuleNotFoundError:
    install("colorama")
    install("keyboard")
    from colorama import Fore, Back, Style
    import keyboard
# Initialize First frame
os.system("clear")
print(Style.BRIGHT + Fore.BLACK + Back.WHITE + "                                                         Pyseal                                                             ")
print(Style.BRIGHT + Fore.BLACK + Back.WHITE + "                                                Text based Operating System built from Python                               ")
print(Style.BRIGHT + Back.WHITE + "                                                    " + Back.WHITE + "                                                                        ")
print(Style.BRIGHT + Back.CYAN + "                        MENU                        " + Back.WHITE + "                                                                        ")
print(Style.BRIGHT + Back.CYAN + "____________________________________________________" + Back.WHITE + "                                                                        ")
print(Style.BRIGHT + Back.YELLOW+" [ Help ]    [ Commands ]    [ About ]    [ Apps ]  " + Back.WHITE + "                                                                        ")
print(Style.BRIGHT + Back.YELLOW+" [ Files ]    [ Quit ]                              " + Back.WHITE + "                                                                        ")
while True:
    1 + 1