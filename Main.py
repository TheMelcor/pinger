import Tkinter
import time

from pinger import Pinger


class PingerGui(Tkinter.Tk):

    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.p = Pinger()
        self.host_names = self.p.getHostNames()
        self.host_ips = self.p.getHostIp()
        self.stime = 60000

        self.labelsN = []
        self.labelsI = []
        self.responses = []
        self.initialize()

    def initialize(self):
        self.grid()
        x = 0
        for i in self.host_names:
            self.labelsN.append(Tkinter.Label(self, anchor="w", fg="black", text=i))
            self.labelsN[x].grid(column=0, row=x, columnspan=2, sticky="nsew")
            x += 1

        x = 0
        for i in self.host_ips:
            self.labelsI.append(Tkinter.Label(self, anchor="w", fg="black", bg="white", text=i))
            self.labelsI[x].grid(column=2, row=x, columnspan=2, sticky="nsew")
            x += 1

        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(2,weight=3)
        self.start()

    def setRed(self, target):
        target.configure(bg="red")

    def setGreen(self, target):
        target.configure(bg="green")

    def setYellow(self, target):
        target.configure(bg="yellow")

    def start(self):
        x=0
        for i in self.host_ips:
            self.setYellow(self.labelsI[x])
            self.setYellow(self.labelsN[x])
            self.update()
            if(self.p.checkSingleIp(x)):
                self.setGreen(self.labelsI[x])
                self.setGreen(self.labelsN[x])
            else:
                self.setRed(self.labelsI[x])
                self.setRed(self.labelsN[x])
            x+=1
        self.after(self.stime, self.start)



app = PingerGui(None)
app.title('Pinging')
app.mainloop()
