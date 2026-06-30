
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--ports', required=True, help = 'Target ports')
parser.add_argument('-t', '--target', required=True, help = 'Target')
args = parser.parse_args()



def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    res = sock.connect_ex((target,port))
    if res == 0:
        print(f'Port {port} is open')
    
    sock.close()
        
try:
    target = args.target
    start, end = args.ports.split('-')
    parts = range(int(start), int(end) + int(1))
    with ThreadPoolExecutor(max_workers=100) as executor:
       executor.map(scan_port, parts)
        
except ValueError:
    print('Incorrect value(-p,-t)')
except KeyboardInterrupt:
    print('Stop scanning')
finally:
    print('End of scanning')   
    
