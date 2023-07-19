import os

try:
    path = os.getcwd() + "\\requirements.txt"
    print(f"Requirements file: {path}")
    input("Press any key to instal python modules...")
    os.system(f"pip install -r {path}")
    print("\n")
    input("Success...")
except Exception as err:
    print(err)
