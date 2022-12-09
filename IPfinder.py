import socket
import re
import subprocess
import time

def get_ip_addresses():
    ip_pattern = re.compile(r'192\.(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){2}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
    output = subprocess.check_output('arp -a', shell=True)
    ip_addresses = re.findall(ip_pattern, output.decode('utf-8'))

    return ip_addresses

print(get_ip_addresses())

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break