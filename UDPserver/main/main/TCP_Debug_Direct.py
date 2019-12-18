import socket
import time
import signal
import sys
import curses as crs #pip install windows-curses



class TerminalStateMachine:
    def __init__(self):
        self.scr=crs.initscr()
        crs.noecho()
        crs.cbreak()
        self.scr.nodelay(True)
        self.scr.addstr("I STARETED")
        self.scr.refresh()
    def __del__(self):
        crs.endwin()
    def mainLoop(self):
        self.scr.addstr(0,0,str(time.time()))
        self.scr.addstr(1,0,"----------------")
        self.scr.addstr(10,0,"Q - Close")
        count=500
        stop=False
        keyPress= -1
        msgUnpackStruct={"Status":0,"Az":0,"AzRate":0,"El":0,"ElRate":0,"Range":0,"RangeRate":0,"TOF":0}
        while(not stop):
            keyPress=self.scr.getch()
            self.scr.addstr(0,0,str(time.time()))
            self.formattedPrint(msgUnpackStruct)

            if(keyPress != -1):
                if(chr(keyPress)=='q'):
                    stop=True

            self.scr.refresh()
            # if(count==0):
            #     stop=True
            count-=count
            time.sleep(0.05)
    def formattedPrint(self,sensorData):
            rowNumber=2
            for j in sensorData.keys():
                self.scr.addstr(rowNumber,0,30*"")
                self.scr.addstr(rowNumber,0,j)
                self.scr.addstr(rowNumber,15,str(sensorData[j]))
                rowNumber+=1
    
    


window=TerminalStateMachine()

window.mainLoop()


# msgUnpackStruct={"Status":0,"Az":0,"AzRate":0,"El":0,"ElRate":0,"Range":0,"RangeRate":0,"TOF":0}
# FORT_IP="192.168.112.67"
# FORT_PORT=13107


# def printFormatted(payloadStruct):
#     sys.stdout.flush()
#     for j in payloadStruct.keys():
#         sys.stdout.write(j+"\t\t"+str(payloadStruct[j]))

# global KillProgram
# KillProgram=False

# HEADER_VALIDATION="WPN:"      #  //a FORT packet has been correctly synchronized if the first token 0 contains this message,
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
# def kill_handler(sig,frame):
#     global KillProgram
#     KillProgram=True
#     print("you pressed Ctrl+C")


# # sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)
# # sock.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,True)
# # sock.connect((FORT_IP,FORT_PORT))

# # time.sleep(1)
# # print("sent")
# # sock.send("\r\nfields=0x002F\r\nflags=0x01FF\r\nregex=Rogue Data\r\n".encode("utf-8"))


# count=0
# while(not KillProgram):
#     try:
#         printFormatted(msgUnpackStruct)
#     except Exception as e:
#         sys.stdout.write('\r'+"Exception Occurred")
#         sys.stdout.write(e)
# sock.close()
# sys.exit(0)


#sock.close()

