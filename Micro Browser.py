import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80)) # Connect to the server
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() # Send a request to the server
mysock.send(cmd) # Send the request to the server

while True:
    data = mysock.recv(512) # Receive the data from the server
    if len(data) < 1:
        break   
    print(data.decode(),end='')
mysock.close() # Close the connection