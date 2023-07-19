try:
    import os, sys, ctypes
    import colorama as color
    from tkinter import *
    from tkinter.ttk import *
except:
    path = os.getcwd() + "\\requirements.txt"
    os.system(f"pip install -r {path}")


VERSION = "v2b1"


class MainGui(Tk):
    """
    MainGui(Tk)
    Main GUI class for 3liWindowsUtilTool
    """

    def __init__(self):
        # init
        Tk.__init__(self)
        self.geometry("320x320")
        self.title("3li's Windows Util Tool")
        self.root = Frame(self)
        self.root.pack()
        # Style
        style = Style()
        style.configure("TButton", font=("Hobo Std", 9, "bold"), foreground="black")
        style.configure("TLabel", font=("Hobo Std", 15, "bold"), foreground="black")
        # objects
        self.title = Label(
            self.root,
            text=f"3li's Windows Util Tool {VERSION}",
        )
        self.welcome = Label(
            self.root,
            text=f"Welcome, {str(os.getlogin())}",
        )
        self.status = Label(self.root, text="ready...")
        self.all_button = Button(
            self.root, text="All cleaners", command=lambda: self.all_killers()
        )
        self.windows_button = Button(
            self.root,
            text="Windows and Xbox cleaner",
            command=lambda: self.random_win_killer(),
        )
        self.games_button = Button(
            self.root,
            text="Games cleaner",
            command=lambda: self.assorted_games_killer(),
        )
        self.quit_button = Button(
            self.root,
            text="Quit",
            command=lambda: exit(),
        )
        # pack
        self.title.pack(pady=8, padx=8)
        self.welcome.pack(pady=8, padx=8)
        self.all_button.pack(pady=8, padx=8)
        self.windows_button.pack(pady=8, padx=8)
        self.games_button.pack(pady=8, padx=8)
        self.quit_button.pack(pady=8, padx=16)
        self.status.configure(font=("Hobo Std", 10, "bold"))
        self.status.pack(pady=8, padx=50)

    def kill_process(self, process_name):
        """
        kill_process(process_name)
        use os.system to kill task provided
        """
        os.system(f"taskkill /f /im {process_name}")

    def random_win_killer(self, skip_continue_check=False):
        """
        random_win_killer()
        * kills some dumb tasks from windows
        """
        windows_processes = [
            "CompatTelRunner.exe",
            "PhoneExperienceHost.exe",
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
            print(color.Fore.GREEN + "WINDOWS PROCESSES" + color.Style.RESET_ALL)
            print(color.Fore.CYAN)  # INFO COLOR
            for process in windows_processes:
                self.kill_process(process)
            print(color.Style.RESET_ALL)  # INFO COLOR RESET
            # Xbox
            print(color.Fore.GREEN + "XBOX PROCESSES" + color.Style.RESET_ALL)
            print(color.Fore.CYAN)  # INFO COLOR
            for process in xbox_processes:
                self.kill_process(process)
            print(color.Style.RESET_ALL)  # INFO COLOR RESET

        except Exception as e:
            print(
                color.Fore.RED
                + "Error occurred: "
                + str(e)
                + color.Style.RESET_ALL
                + "\n"
            )

        finally:
            print(color.Fore.GREEN + "Done!" + color.Style.RESET_ALL)
            self.status.config(text="finished cleaning windows...")

    def assorted_games_killer(self, skip_continue_check=False):
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
        other_processes = [
            "Agent.exe",
            "Battle.net.exe",
            "EpicWebHelper.exe",
            "EpicGamesLauncher.exe",
        ]
        riot_processes = ["RiotClientCrashHandler.exe", "RiotClientServices.exe"]
        try:
            # Oculus
            print(color.Fore.GREEN + "OCULUS PROCESSES" + color.Style.RESET_ALL)
            print(color.Fore.CYAN)  # INFO COLOR
            for process in oculus_processes:
                self.kill_process(process)
            print(color.Style.RESET_ALL)  # INFO COLOR RESET
            # Ubisoft
            print(color.Fore.GREEN + "UBISOFT PROCESSES" + color.Style.RESET_ALL)
            print(color.Fore.CYAN)  # INFO COLOR
            for process in ubisoft_processes:
                self.kill_process(process)
            print(color.Style.RESET_ALL)  # INFO COLOR RESET
            # Riot
            print(color.Fore.GREEN + "RIOT PROCESSES" + color.Style.RESET_ALL)
            print(color.Fore.CYAN)  # INFO COLOR
            for process in riot_processes:
                self.kill_process(process)
            print(color.Style.RESET_ALL)  # INFO COLOR RESET
            # Other
            print(color.Fore.GREEN + "OTHER PROCESSES" + color.Style.RESET_ALL)
            print(color.Fore.CYAN)  # INFO COLOR
            for process in other_processes:
                self.kill_process(process)
            print(color.Style.RESET_ALL)  # INFO COLOR RESET

        except Exception as e:
            print(color.Fore.RED + "Error occurred: " + str(e) + color.Style.RESET_ALL)

        finally:
            print(color.Fore.GREEN + "Done!" + color.Style.RESET_ALL + "\n")
            self.status.config(text="finished cleaning games...")

    def all_killers(self):
        """
        all_killers()
        * calls all killers
        """
        self.assorted_games_killer(skip_continue_check=True)
        self.random_win_killer(skip_continue_check=True)
        self.status.config(text="finished cleaning all...")


if __name__ == "__main__":
    # Check admin
    if ctypes.windll.shell32.IsUserAnAdmin():
        app = MainGui()
        app.mainloop()
    else:
        # re-launch as admin
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
