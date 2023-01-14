import pyfiglet
import socket
import threading
from colorama import Fore
from datetime import datetime
import subprocess

print(Fore.GREEN+'''
 ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
|  _ \ / _ \|  _ \_   _| / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
| |_) | | | | |_) || |   \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
|  __/| |_| |  _ < | |    ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
|_|    \___/|_| \_\|_|   |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\\
''')
print("-"*70)

print(Fore.YELLOW+"""
     ,-~~-.___.      
    / |  x     \ 
    (  )        0       
    \_/-, ,----'  ____  
        ====      ||   \_ 
       /  \-'~;   ||     |                v.1.0.0
      /  __/~| ...||__/|-"            PORT SCANNER TOOL
    =(  _____||________|                ~thebibekdas~
   
   https://github.com/thebibekdas/Port-Scanner
    
""")

print(Fore.BLUE+"-"* 70)
print(Fore.BLUE+"-"* 70)

host=socket.gethostbyname(input("[+] Enter target domain: ",))
start_port=int(input("[+] Enter start port: "))
end_port=int(input("[+] Enter end port: "))

print("-" * 50)
print("Scanning Target: " + host)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

def scan(port):
    s=socket.socket()
    s.settimeout(3)
    result=s.connect_ex((host,port,))
    if result ==0:
        print("Port {} is open".format(port,))
    s.close()

for i in range(start_port,end_port+1):
    t=threading.Thread(target=scan,args=(i,))
    t.start()


