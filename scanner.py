import socket,sys,colorama
from datetime import datetime

#----------------------------------------------------

ip_to_host = socket.gethostbyname(input(colorama.Fore.GREEN+"host : "))
p1 = True
while p1:
    start_port = input("first port : ")
    end_port = input("last_port : ")

    try:
        start_port = int(start_port)
        end_port = int(end_port)
        p1 = False
    except:
        print("port i not number ! please enter the number.")
        pass

p2 = True
while p2:
    tcp_udp = input("TCP or UDP ?: ")
    if tcp_udp[0] == "t"or"T":
        tcp_udp_1 = socket.SOCK_STREAM
        p2 = False
    elif tcp_udp[0] == "U"or"u":
        tcp_udp_1 = socket.SOCK_DGRAM
        p2 = False
    else:
        print("sorry!! I don't undrestand!")
print(colorama.Style.RESET_ALL)
#----------------------------------------------------

print("-"*60)
print(f"please wait host = {ip_to_host}")
print("-"*60)

time_1 = datetime.now()
#----------------------------------------------------
open_ports = []
try:
    for port in range(start_port,end_port+1):
        soct = socket.socket(socket.AF_INET,tcp_udp_1)
        result = soct.connect_ex((ip_to_host,port))

        if result == 0:
            print(colorama.Fore.BLACK+colorama.Back.GREEN+f"[+]   port {port}:    open")
            open_ports.append(port)
        else : 
            print(colorama.Fore.WHITE+colorama.Back.RED+f"[+]    port {port} :      close")
except KeyboardInterrupt : 
    print("have good time!!")
    sys.exit()
except socket.gaierror:
    print(f"we can't connect to {ip_to_host}")
except socket.error:
    print(f"{ip_to_host} is off")
except :
    print("something id wrong!!")

print(colorama.Style.RESET_ALL)
print("-"*60,"\n\n")
for p in open_ports:
    print(f"[{p}      opne]")


time_2 = datetime.now()

time_3 = time_2 - time_1

print(f"time : {time_3}")

input("you want close program? ")
input("are you sure? ")
