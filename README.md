# Port Scanner

A simple multithreaded port scanner that quickly scans a target host and shows which ports are open.

## Usage

```bash
python portscan.py -t <TARGET> -p <PORTS>
Arguments
-t, --target — target IP address
-p, --ports — port range to scan (e.g. 1-1000)
Example
python scanner.py -t 10.10.10.5 -p 50-100
Output:
Port 53 is open
End of scanning
Notes
Built with Python’s socket and ThreadPoolExecutor for concurrent scanning. For use in labs and authorized testing only.
