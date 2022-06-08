from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
my_port = 5050
my_host = 'localhost'
serverSocket.bind((my_host,my_port))
serverSocket.listen()

print("Ready To Serve ...")

while True:
    # Establish the connection
    connectionSocket, addr = serverSocket.accept()
    MAX_PACKET = 32768 
    try:
        message = connectionSocket.recv(MAX_PACKET)
        print("\nMessage:\n", message)
        filename = message.split()[1]
        print("\nFilename:\n", filename)
        f = open(filename[1:])
        outputdata =f.readlines()
        print("\nFile Length:\n", len(outputdata))
        connectionSocket.send(bytes('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode()))
        for i in range(0, len(outputdata)):
            connectionSocket.send(bytearray(outputdata[i].encode()))
        connectionSocket.close()
    except :
        connectionSocket.send(bytes('HTTP/1.1 404 OK\nContent-Type: text/html\n\n'.encode()))
        connectionSocket.send(bytes('<html><head></head><body><h1>Error</h1></body></html>'.encode()))
        connectionSocket.close()
serverSocket.close()