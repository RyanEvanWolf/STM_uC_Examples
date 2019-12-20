import socket
import time
import signal
import sys
import curses as crs #pip install windows-curses
import threading

class TCPserver:
    def __init__(self,windowRegion,address=('192.168.1.1', 999)):

        self.Address=address
        self.tcpsock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.scr=windowRegion
        self.thread= threading.Thread(name='TCPDaemon',target=self.serverRun)
        self.thread.setDaemon(True)
    def serverRun(self):
        self.scr.addstr(0,0,"Setup on "+str(self.Address))
        try:
            self.tcpsock.bind(self.Address)
            self.tcpsock.listen(5)##max clients
            self.scr.addstr(1,0,"Waiting For Connection")
            connection, client_address =self.tcpsock.accept()
            self.scr.addstr(2,0,str(time.time()) +" Connection on: "+str(client_address))
            time.sleep(3)
            self.scr.clear()
        except Exception as e:
            self.scr.addstr(4,0,str(e))
        delayTime=0.02#seconds
        msg="this is a very long message"
        while(True):
            connection.send((msg*23).encode('utf-8'))
            self.scr.addstr(3,0,"ByteSize:"+str(len(msg*23)))
            self.scr.addstr(2,0,str(time.time()))
            time.sleep(delayTime)


class TerminalStateMachine:
    def __init__(self):
        self.scr=crs.initscr()
        crs.noecho()
        crs.cbreak()
        self.scr.nodelay(True)
        #key input screen 
        #################
        ##info display screen
        self.infoScreen=crs.newwin(3,crs.LINES-1,0,0)
        self.infoScreen.addstr(1,0,"Q - Close")
        self.infoScreen.addstr(2,0,"----------------")
        self.server=TCPserver(crs.newwin(10,crs.LINES-1,3,0))
    def __del__(self):
        crs.endwin()
    def mainLoop(self):
        stop=False
        keyPress= -1
        self.server.thread.start()
        while(not stop):
            keyPress=self.scr.getch()
            self.infoScreen.addstr(0,0,str(time.time()))
            if(keyPress != -1):
                if(chr(keyPress)=='q'):
                    stop=True
            self.scr.refresh()
            self.infoScreen.refresh()
            self.server.scr.refresh()
            time.sleep(0.1)
        self.server.tcpsock.close()
    def formattedPrint(self,sensorData):
            rowNumber=2
            for j in sensorData.keys():
                self.scr.addstr(rowNumber,0,30*"")
                self.scr.addstr(rowNumber,0,j)
                self.scr.addstr(rowNumber,15,str(sensorData[j]))
                rowNumber+=1
    
    


window=TerminalStateMachine()

window.mainLoop()
print("Server Killed")






