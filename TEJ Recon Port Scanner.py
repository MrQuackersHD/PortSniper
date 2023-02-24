
#Version 1.1 "CITADEL"


### Importing ###
import pyfiglet
import tkinter as TK
import sys
import socket
from datetime import datetime
import colorama
import threading
from colorama import Fore
import concurrent.futures
colorama.init()


print_lock = threading.Lock()

ascii_banner = pyfiglet.figlet_format (" PORT SNIPER ")
with print_lock:
    print(Fore.RED + ascii_banner)


print("WARNING: This tool is not made to be used for malicious intent. It is a tool created for finding and identifying open ports that could be used for malicious intent by third parties. This tool is not a game, or toy.\n")

target = input(str("Target IP/ADDRESS:"))


print("_" * 50, "\n")
print("SNIPING TARGET IP NOW: " + target)
print("IP address: " + target + " has been targeted on " + str(datetime.now()))
print("_" * 50, "\n")

try:

    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)

        result = s.connect_ex((target,port))
        if result == 0:
            with print_lock:
                print(Fore.WHITE + f"[{port}]" + Fore.GREEN + "OPEN")
            list_elm = {port}
            
        s.close()

except KeyboardInterrupt:
    print("\n Exiting :( ")
    sys.exit()

except socket.error:
    print("The Target Host is Not Responding :(\nTerminating Sniper, Now! ")


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range (1,65535):
        executor.submit( target, port + 1)



ascii_banner = pyfiglet.figlet_format (" SNIPE COMPLETED:\n ALL PORTS SCANNED SUCCESSFULLY ")
if result == 0:
        with print_lock:
            print(Fore.GREEN+ ascii_banner)

if result == 0:
            with print_lock:
                print(Fore.WHITE + result)

