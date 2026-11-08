import socket

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        s.close()
        if result == 0:
            return True
        return False
    except:
        return False

def main():
    print("--- Network Port Scanner ---")
    ip = input("Enter IP address (e.g., 127.0.0.1): ")
    ports = [21, 22, 23, 80, 443, 3389]
    
    print(f"\nScanning {ip}...")
    for port in ports:
        if scan_port(ip, port):
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is closed")

if __name == "__main__":
    main()
