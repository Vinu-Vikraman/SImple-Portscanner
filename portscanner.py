#!/python3

import socket #importing socket module

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #these two are for connecting to ip4 address

host = input("[+]Enter the IP to connect: ")  #prompt the user for ip address    
port = int(input("[+]Enter the Port to connect: "))  #prompt the user port 
  

def portscanner(port):  #defining port scanner function
    if sock.connect_ex((host,port)): #tuple as parameter
      print("Port %d is closed"%(port))  #display if port is opened
    else:
      print("Port %d is opened"%(port))  #display if port is opened

portscanner(port)
