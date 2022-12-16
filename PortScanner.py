import pyfiglet
import socket
import threading
from datetime import datetime
import subprocess

output=subprocess.Popen("title portscanner",shell=True)
#output=subprocess.Popen("color 0a",shell=True)
print(output)
#input()

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
print("-"*70)

print("""
     ,-~~-.___.      
    / |  x     \ 
    (  )        0       
    \_/-, ,----'  ____  
        ====      ||   \_ 
       /  \-'~;   ||     |                v.1.0.0
      /  __/~| ...||__/|-"            PORT SCANNER TOOL
    =(  _____||________|                ~thebibekdas~
""")


'''print("""
 __      __             ___                                           
/\ \  __/\ \           /\_ \                                          
\ \ \/\ \ \ \     __   \//\ \      ___     ___     ___ ___       __   
 \ \ \ \ \ \ \  /'__`\   \ \ \    /'___\  / __`\ /' __` __`\   /'__`\ 
  \ \ \_/ \_\ \/\  __/    \_\ \_ /\ \__/ /\ \L\ \/\ \/\ \/\ \ /\  __/ 
   \ `\___x___/\ \____\   /\____\\ \____\\ \____/\ \_\ \_\ \_\\ \____\
    '\/__//__/  \/____/   \/____/ \/____/ \/___/  \/_/\/_/\/_/ \/____/ """)
'''


print("-"* 70)
print("-"* 70)

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


