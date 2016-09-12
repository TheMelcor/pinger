import os
from sys import platform




class Pinger():

    def __init__(self):
        self.host_names = []
        self.host_ip = []
        self.responses = []

        self.command = self.getCmd()
        self.setup()

    def getCmd(self):
        if platform == "linux" or platform == "linux2":
            return "ping -c 1 "
        elif platform == "darwin":
            return "ping -c 1 "
        elif platform == "win32":
            return "ping -n 1 "
        else:
            return "ping "

    def setup(self):
        with open('hostList') as f:
            host_list = f.readlines()

        for l in host_list:
            temp = l.split(":")
            self.host_names.append(temp[0])
            self.host_ip.append(temp[1])

    def checkIp(self):
        del self.responses[:]
        for i in self.host_ip:
            response = os.system(self.command + i)
            if response == 0:
                self.responses.append(1)
            else:
                self.responses.append(0)

    def checkSingleIp(self, ip):
        response = os.system(self.command + self.host_ip[ip])
        if response == 0:
            return True
        else:
            return False

    def getResponses(self):
        return self.responses

    def getHostNames(self):
        return self.host_names

    def getHostIp(self):
        return self.host_ip

