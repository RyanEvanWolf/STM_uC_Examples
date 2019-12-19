import socket

 

msgFromClient       = "A"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("192.168.1.5", 1000)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

 
while(True):
    try:
        UDPClientSocket.settimeout(1.0)
        msgFromServer = UDPClientSocket.recv(15)
        UDPClientSocket.settimeout(None)
        msg = "Message from Server {}".format(msgFromServer[0])
        print(msg)
    except Exception as e:
        print(e)
