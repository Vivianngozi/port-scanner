import socket
import threading
import re
from queue import Queue
import subprocess
import platform

# Lock for thread-safe printing
print_lock = threading.Lock()

def port_scan(target_ip, port):
    """Scans a single port on the target IP."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                with print_lock:
                    try:
                        service = socket.getservbyport(port)
                    except:
                        service = "Unknown Service"
                    print(f"[+] Port {port} is OPEN ({service})")
    except Exception as e:
        with print_lock:
            print(f"[-] Error scanning port {port}: {e}")

def threader(target_ip, q):
    while True:
        worker = q.get()
        port_scan(target_ip, worker)
        q.task_done()

def validate_ip(ip):
    """Validates both IPv4 and IPv6 addresses."""
    ipv4_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    ipv6_pattern = re.compile(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$")

    if ipv4_pattern.match(ip):
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False
    elif ipv6_pattern.match(ip):
        return True
    else:
        return False

def check_host_reachable(ip):
    """Pings the target IP to check if it is reachable."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", ip]
    try:
        subprocess.check_output(command, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("Basic Port Scanner\n--------------------")
    
    target_ip = input("Enter target IP address: ").strip()
    if not validate_ip(target_ip):
        print("[-] Invalid IP address format. Please enter a valid IPv4 or IPv6 address.")
        return

    if not check_host_reachable(target_ip):
        print(f"[-] The IP address {target_ip} is not reachable or does not exist.")
        return

    print(f"[+] Scanning Target IP: {target_ip}")

    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        print("[-] Invalid port range. Please enter ports between 0-65535.")
        return

    q = Queue()
    
    # Starting threads
    for _ in range(100):  # 100 threads for faster scanning
        t = threading.Thread(target=threader, args=(target_ip, q))
        t.daemon = True
        t.start()

    # Queuing ports
    for port in range(start_port, end_port + 1):
        q.put(port)

    q.join()
    print("\n[+] Scanning completed.")

if __name__ == '__main__':
    main()


