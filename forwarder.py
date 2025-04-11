import netifaces
import sys

try:
    iface = sys.argv[1]
except IndexError:
    print("specify iface")
    exit()

interfaces = netifaces.interfaces()
if iface in interfaces:
    addresses = netifaces.ifaddresses(iface)
    ip = addresses[netifaces.AF_INET][0]['addr']
    ip_parts = ip.split('.')
    ip_parts[2] = '0'
    subnet = '.'.join(ip_parts[:3]) + '.0/32'
else:
    print("invalid iface")