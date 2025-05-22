import socket
import time

def scan_port(ip, port):
  try:      
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")
    sock.close()

  except Exception as e:
     print(f"Error scanning port {port}: {e}")
  finally:
     sock.close()

# Define the target IP (localhost for safety) and ports to scan.
target_ip = "127.0.0.1"
ports_to_scan = [22, 80, 443, 8000]

print("Starting port scanner for", target_ip)

#loop through each port
for port in ports_to_scan:
    scan_port(target_ip, port)
    time.sleep(0.5)

print("Scan complete!")    

