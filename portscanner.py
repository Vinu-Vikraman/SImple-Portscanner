import socket #importing socket module

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #for connecting to ip4 address

host = input("IP Address: ")                #give your host here
port = int(input("Port: "))          #pre-determined port

def portscanner(host,port):     #definying a function     
  if sock.connect(host,port):   
    print("Port %d is open"%(port))
  else:
    print("Port %d is closed"%(port))
   
portscanner(port)
