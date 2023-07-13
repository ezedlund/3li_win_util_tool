import os, sys, ctypes
from colorama import Fore, Style
from pick import pick


VERSION = "v1.1"


def kill_process(process_name):
    """
    kill_process(process_name)
    use os.system to kill task provided
    """
    os.system(f"taskkill /f /im {process_name}")


def random_win_killer(skip_continue_check=False):
    """
    random_win_killer()
    * kills some dumb tasks from windows
    """
    windows_processes = [
        "CompatTelRunner.exe",
        "phoneexperiencehost.exe",
        "yourphoneserver.exe",
        "yourphone.exe",
        "mysqld.exe",
        "msedge.exe",
    ]
    xbox_processes = [
        "xboxappservices.exe",
        "gamebarpresencewriter.exe",
        "gamebarftserver.exe",
        "gamebar.exe",
        "xboxapp.exe",
        "XboxIdp.exe",
        "XboxPCApp.exe",
        "gamingservices.exe",
        "gamingservicesnet.exe",
        "gameinputsvc.exe",
        "mysqld.exe",
    ]
    try:
        # Windows
        print(Fore.GREEN + "WINDOWS PROCESSES" + Style.RESET_ALL)
        print(Fore.CYAN)  # INFO COLOR
        for process in windows_processes:
            kill_process(process)
        print(Style.RESET_ALL)  # INFO COLOR RESET
        # Xbox
        print(Fore.GREEN + "XBOX PROCESSES" + Style.RESET_ALL)
        print(Fore.CYAN)  # INFO COLOR
        for process in xbox_processes:
            kill_process(process)
        print(Style.RESET_ALL)  # INFO COLOR RESET

    except:
        print(Fore.RED + "Error occurred." + Style.RESET_ALL)

    finally:
        if not skip_continue_check:
            input(Fore.GREEN + "Press any key to continue..." + Style.RESET_ALL)


def assorted_games_killer(skip_continue_check=False):
    """
    assorted_games_killer()
    * kills random leftover tasks from games
    """
    oculus_processes = [
        "OculusClient.exe",
        "OVRRedir.exe",
        "OVRServer_x64.exe",
        "OVRServiceLauncher.exe",
    ]
    ubisoft_processes = [
        "upc.exe",
        "UplayWebCore.exe",
        "UbisoftGameLauncher.exe",
        "UbisoftGameLauncher64.exe",
    ]
    other_processes = ["Agent.exe"]
    riot_processes = ["RiotClientCrashHandler.exe", "RiotClientServices.exe"]
    try:
        # Oculus
        print(Fore.GREEN + "OCULUS PROCESSES" + Style.RESET_ALL)
        print(Fore.CYAN)  # INFO COLOR
        for process in oculus_processes:
            kill_process(process)
        print(Style.RESET_ALL)  # INFO COLOR RESET
        # Ubisoft
        print(Fore.GREEN + "UBISOFT PROCESSES" + Style.RESET_ALL)
        print(Fore.CYAN)  # INFO COLOR
        for process in ubisoft_processes:
            kill_process(process)
        print(Style.RESET_ALL)  # INFO COLOR RESET
        # Riot
        print(Fore.GREEN + "RIOT PROCESSES" + Style.RESET_ALL)
        print(Fore.CYAN)  # INFO COLOR
        for process in riot_processes:
            kill_process(process)
        print(Style.RESET_ALL)  # INFO COLOR RESET
        # Other
        print(Fore.GREEN + "OTHER PROCESSES" + Style.RESET_ALL)
        print(Fore.CYAN)  # INFO COLOR
        for process in other_processes:
            kill_process(process)
        print(Style.RESET_ALL)  # INFO COLOR RESET

    except:
        print(Fore.RED + "Error occurred." + Style.RESET_ALL)

    finally:
        if not skip_continue_check:
            input(Fore.GREEN + "Press any key to continue..." + Style.RESET_ALL)


def all_killers():
    """
    all_killers()
    * calls all killers
    """
    assorted_games_killer(skip_continue_check=True)
    random_win_killer(skip_continue_check=True)
    input(Fore.GREEN + "Press any key to continue..." + Style.RESET_ALL)


def see_tasks():
    """
    see_tasks()
    * view current tasks and info
    """
    try:
        print(Fore.CYAN)  # INFO COLOR
        tasks = os.popen("tasklist").readlines()
        for task in tasks:
            print(task, end="")
        print(Style.RESET_ALL)  # INFO COLOR RESET
    except:
        print(Fore.RED + "Error occurred." + Style.RESET_ALL)
    finally:
        input(Fore.GREEN + "Press any key to continue..." + Style.RESET_ALL)


def pid_killer():
    """
    pid_killer()
    * kill specific task via pid
    """
    try:
        PID = int(input("Enter PID: "))
        os.system(f"taskkill /f /im {PID}")
    except:
        print(Fore.RED + "Error occurred." + Style.RESET_ALL)
    finally:
        input(Fore.GREEN + "Press any key to continue..." + Style.RESET_ALL)


def commands_menu():
    """
    commands_menu()
    * sub menu for commandss
    """
    while True:
        os.system("cls")
        menu_title = "Useful Commands"
        options = ["Open old control panel", "IP config", "System infos", "Back"]
        _, index = pick(options=options, title=menu_title, indicator=">")
        if index == 0:
            os.system("control panel")
        elif index == 1:
            os.system("ipconfig")
            input(Fore.GREEN + "Press any key to continue..." + Style.RESET_ALL)
        elif index == 2:
            os.system("systeminfo")
            input(Fore.GREEN + "Press any key to continue..." + Style.RESET_ALL)
        elif index == 3:
            break


if __name__ == "__main__":
    # Attempt to install requirements
    os.system("pip install -r requirements.txt")
    # Check admin
    if ctypes.windll.shell32.IsUserAnAdmin():
        while True:
            os.system("cls")
            # Menu setup
            menu_title = (
                "|  3li's Win Util Tool "
                + VERSION
                + "    |\n      |   Welcome "
                + str(os.getlogin())
                + "   |"
                + "\n____________________________________"
            )
            options = [
                "All Cleaners",
                "Assorted Games Cleaner",
                "Windows Cleaner",
                "See Tasks",
                "Custom PID Cleaner",
                "Useful Commands",
                "Quit",
            ]
            _, index = pick(options=options, title=menu_title, indicator=">")
            # All
            if index == 0:
                all_killers()
            # Games
            elif index == 1:
                assorted_games_killer()
            # Windows
            elif index == 2:
                random_win_killer()
            # Tasks
            elif index == 3:
                see_tasks()
            # PID Cleaner
            elif index == 4:
                pid_killer()
            # Commands
            elif index == 5:
                commands_menu()
            # Quit
            elif index == 6:
                break

    else:
        # re-launch as admin
        input(
            Fore.CYAN
            + "ADMIN_ERROR: Press any key to re-launch as admin..."
            + Style.RESET_ALL
        )
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
