import socket
from datetime import datetime

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return True
        else:
            return False
    except Exception as e:
        return False
    finally:
        sock.close()

def main():
    target = input("Enter the IP address or domain name to scan: ")
    print(f"Starting scan on {target}")
    
    # Record the start time
    start_time = datetime.now()
    
    # Scan ports 1 to 1024
    for port in range(1, 1025):
        if scan_port(target, port):
            print(f"Port {port} is open")
    
    # Record the end time
    end_time = datetime.now()
    total_time = end_time - start_time
    
    print(f"Scan completed in {total_time}")

if __name__ == "__main__":
    main()

