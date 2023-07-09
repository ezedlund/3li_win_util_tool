import os, sys, ctypes
from consolemenu import *
from consolemenu.items import *
from colorama import Fore, Style


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
    menu = ConsoleMenu(
        f"{Fore.GREEN}-> Useful windows commands{Style.RESET_ALL}",
        f"{Fore.LIGHTMAGENTA_EX}Welcome, {os.getlogin()}{Style.RESET_ALL}",
    )
    # create options
    func_control_panel = FunctionItem(
        "Open old school (and better) control panel",
        lambda: os.system("control panel"),
    )
    func_ipconfig = FunctionItem(
        "ipconfig (IP info)",
        lambda: (
            os.system("ipconfig"),
            input(Fore.GREEN + "Press any key to continue..." + Style.RESET_ALL),
        ),
    )
    func_sys_info = FunctionItem(
        "System info",
        lambda: (
            os.system("systeminfo"),
            input(Fore.GREEN + "Press any key to continue..." + Style.RESET_ALL),
        ),
    )
    # add options
    menu.append_item(func_control_panel)
    menu.append_item(func_ipconfig)
    menu.append_item(func_sys_info)
    # show menu
    menu.show()


if __name__ == "__main__":
    # Check admin
    if ctypes.windll.shell32.IsUserAnAdmin():
        # setup menu
        menu = ConsoleMenu(
            f"{Fore.GREEN}3li's Win Util Tool v0.4{Style.RESET_ALL}",
            f"{Fore.LIGHTMAGENTA_EX}Welcome, {os.getlogin()}{Style.RESET_ALL}",
        )
        # create options
        func_games_kill = FunctionItem(
            "Random Games shit killer (Oculus, Ubisoft, etc.)",
            lambda: assorted_games_killer(),
        )
        func_random_win = FunctionItem(
            "Random windows shit killer", lambda: random_win_killer()
        )
        func_all = FunctionItem("All killers", lambda: all_killers())
        func_see_tasks = FunctionItem("Check tasks", lambda: see_tasks())
        func_pid_kill = FunctionItem("Custom PID task killer", lambda: pid_killer())
        func_commands = FunctionItem("Useful commands", lambda: commands_menu())
        # add options
        menu.append_item(func_all)
        menu.append_item(func_games_kill)
        menu.append_item(func_random_win)
        menu.append_item(func_see_tasks)
        menu.append_item(func_pid_kill)
        menu.append_item(func_commands)
        # show menu
        menu.show()
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
