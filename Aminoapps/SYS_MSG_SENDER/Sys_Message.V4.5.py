
# Built In Imports
import os
import sys
import subprocess
import requests
from time import sleep
from sys import exit

# Dependencies
Dependencies = input("Update & Install Dependencies? Y/N \> ").lower()
if Dependencies == "y":
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'art'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'lolpython'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'amino.py'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'amino.py', '--upgrade'])
else:
    pass


if os.path.exists("device.json"):
      os.remove("device.json")
else:
    print("did not find")
    pass


# PYPI Imports
import colorama
import lolpython
import art
import amino
from colorama import Fore, Style, Back
from  lolpython import lol_py as lolpy
from amino.lib.util.exceptions import *
from art import *

colorama.init(autoreset=True)

# Updates Amino.py
#os.system("python3 pip -m install amino.py --upgrade")

# Handles Device ID For Remote Updates Without needing To Modify Script Directly.
Git_deviceId = requests.get("https://raw.githubusercontent.com/ODYSSE3US/Stand_Alone_Build_Data/main/Aminoapps/SYS_MSG_SENDER/deviceId.txt")
Git_deviceId_text = Git_deviceId.text
deviceId = str(Git_deviceId_text.rstrip("\n"))

#deviceId = "428320C1CBC8CB809BE9C4246907ED0598CC5023E777BC3E5EF3F4DE41626A4B443AB7A58183D424CD"

# Random Comment // Announcement banner | Not Yet Implimented.
Git_banner = requests.get("https://raw.githubusercontent.com/ODYSSE3US/Stand_Alone_Build_Data/main/Aminoapps/SYS_MSG_SENDER/Banner.txt")
Git_OTA_Banner = Git_deviceId.text


# Colour Shortcuts
White_TXT = Fore.WHITE + Style.BRIGHT
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
CYAN = Fore.CYAN
Reset = Fore.RESET + Style.RESET_ALL


# Confirm Dialogue But Repetitive.
def Redo():
    try:
        RMSG = input(White_TXT + 'Type Message Here: ')
        subclient.send_message(chatId,message=RMSG, messageType="109")
    except ValueError:
        print(RED + "Message Failed, Please Try again..")
        Redo()

    print(White_TXT + f"Type Y for Yes And N for No.")
    print(White_TXT + "Type 'a' For Advanced Mode To Get Rid Of This Annoying Reminder.")
    party = input(White_TXT + "Wanna Send Another? ").lower()
    if party == "y":
        Redo()
    elif party == "n":
        exit(0)
    elif party == "a":
        skip_annoying_Reminder()
    elif party == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        Redo()
    else:
        print(f'Make sure you either said Y or N, Type "clear" To Clear Screen.')


# This Skips That Annoying Reminder And Enables More Possible Functions
def skip_annoying_Reminder():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTWHITE_EX + Back.RED + "Advanced Mode:")
    print("Type '!help' for help")

    ThisIsDefined = input(White_TXT + 'Type Message Here: ')

    if ThisIsDefined == "!help":
        print(help_msg)
        input("Continue? /> ")
        skip_annoying_Reminder()

    elif ThisIsDefined == "!clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        skip_annoying_Reminder()

    elif ThisIsDefined == "!exit":
        print(RED + "Exiting Script..")
        sleep(1.7)
        os.system('cls' if os.name == 'nt' else 'clear')
        exit(0)

    elif ThisIsDefined == "!gaymode":
        print("Congrats! You Just Found An Easter Egg.")
        sleep(0.6)
        os.system('cls' if os.name == 'nt' else 'clear')
        LGBT_MODE()
    else:
        subclient.send_message(chatId,message=ThisIsDefined, messageType="109")
        skip_annoying_Reminder()


# Useless But Fun Addition.... I was bored so why not?
def LGBT_MODE():
    if os.name == "nt":

        lolpy("This Is Unfortunately Not Compatible With Windows. Returning..")
        # Or More Specifically Machines that support ANSI Color Coding.
        sleep(1.5)
        skip_annoying_Reminder()

    else:
        gay_mode_ASCII = """
 ██████   █████  ██    ██     ███    ███  ██████  ██████  ███████ 
██       ██   ██  ██  ██      ████  ████ ██    ██ ██   ██ ██      
██   ███ ███████   ████       ██ ████ ██ ██    ██ ██   ██ █████   
██    ██ ██   ██    ██        ██  ██  ██ ██    ██ ██   ██ ██      
 ██████  ██   ██    ██        ██      ██  ██████  ██████  ███████ 
        Dyed with 100% Genuine, Cruelty Free Unicorn Piss.                                   
    """
        os.system('cls' if os.name == 'nt' else 'clear')
        lolpy(gay_mode_ASCII)
        lolpy("This is just here purely for my amusement... 5hrs later.. lol")
        lolpy("Type '!help' for help")

        RainbowInput = input(White_TXT + 'Type Message Here: ')

        if RainbowInput == "!help":
            lolpy(help_msg)
            input("Continue? /> ")
            skip_annoying_Reminder()

        elif RainbowInput == "!clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            skip_annoying_Reminder()

        elif RainbowInput == "!exit":
            lolpy("Exiting Script..")
            sleep(1.7)
            os.system('cls' if os.name == 'nt' else 'clear')
            exit(0)

        elif RainbowInput == "!gaymode":
            lolpy("Congrats! You Just Found An Easter Egg.")
            sleep(0.6)
            os.system('cls' if os.name == 'nt' else 'clear')
            skip_annoying_Reminder()
        else:
            try:
                subclient.send_message(chatId,message=RainbowInput, messageType="109")
                LGBT_MODE()
            except ValueError:
                print(RED + "Something went wrong on amino's end. Try again in a few minutes.")
                exit(1)

            


help_msg = """

    !help       -     Displays This message
    !clear      -     Clears The Screen
    !exit       -     Exits The Script
    !gaymode    -     ????????????????
"""



# The Main Event.. The Thing That Starts On Start Up.
try:
    os.system('cls' if os.name == 'nt' else 'clear')


    client = amino.Client()
    tprint("Sys Messenger")
    U = input(White_TXT + 'Enter Your Email Here: ')
    P = input(White_TXT + 'Enter Your Password Here: ')

    client.login(email=U, password=P)
    print(f"Successfully Logged In As  {RED}'{client.profile.nickname}'")
    sleep(2)

    os.system('cls' if os.name == 'nt' else 'clear')
    clients = client.sub_clients(start=0, size=1000)

    for A, name in enumerate(clients.name, 1):
        print(f"{YELLOW}|{CYAN}{A}{YELLOW}| {GREEN}{name}")
    aminoIdent = clients.comId[int(input("Select the community: "))-1]
    subclient = amino.SubClient(comId=aminoIdent, profile=client.profile)


    os.system('cls' if os.name == 'nt' else 'clear')
    chatLink = input(White_TXT + 'Paste Chat Link Here: ')
    chatId = client.get_from_code(chatLink).objectId
    MSG = input(White_TXT + 'Type Message Here: ')
    if MSG == "!exit":
        print(White_TXT + "Exiting Script...")
        exit(0)

    else:
        subclient.send_message(chatId,message=MSG,messageType="109")
        print(RED + "Fake System Message Sent.")

        print("Type Y for Yes And N for No. **Case Sensitive**")
        party = input(White_TXT + "Wanna Send Another? ")
        if party == "Y":
            Redo()
        elif party == "y":
            Redo()
        elif party == "N":
            exit(0)
        elif party == "n":
            exit(0)
        else:
            print("Make sure you either said Y or N")

except amino.lib.util.exceptions.InvalidPassword as invalidpw:
    print(RED + "Invalid Password", "An Error Has Occurred Please Restart The Program.")
    sleep(2)
    exit(0)


except amino.lib.util.exceptions.InvalidEmail as invalidemail:
    print(RED + "Invalid Email", "An Error Has Occurred Please Restart The Program.")
    sleep(2)
    exit(0)

except ValueError:
    print(RED + "Something went wrong on amino's end. Try again in a few minutes.")
    exit(1)