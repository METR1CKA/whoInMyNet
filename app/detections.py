import nmap

class detections:

    def __init__(self, ip):
        self.ip = ip
        self.scanner = nmap.PortScanner()

    def checkNets(self):
        self.scanner.scan(self.ip)

        ips = self.scanner.all_hosts()

        return ips
