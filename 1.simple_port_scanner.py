import socket
import time

#Defines the target IP (localhost for safety):
target_ip= "127.0.0.1"

#list of common ports to scan:
ports_to_scan = [22, 80, 443, 8000]

#print a welcome message:
print("Starting port scanner for", target_ip)

#Loop through each port
for port in ports_to_scan:

    #create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Set a timeout to avoid hanging
    sock.settimeout(1)

    #Try connecting to the IP and port
    result = sock.connect_ex((target_ip, port))

    #check if port is open (result == 0 means success)
    if result == 0:
        print(f"port {port} is OPEN")
    else:
        print(f"port {port} is CLOSED")

    #Close the socket
    sock.close() 

    #small delapy to avoid overwhelming the system
    time.sleep(0.5)

print("Scan complete!")    


