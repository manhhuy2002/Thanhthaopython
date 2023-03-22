import socket

# Tao socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lay ten local machine 
host = socket.gethostname()

port = 9999

# Ket noi toi server
clientsocket.connect((host, port))

while True:
    # Gui tin nhan toi server
    message = input("Enter a message: ")
    if not message:
	#neu tin nhan trong thi ngat ket noi
        break
    clientsocket.send(message.encode())

    # Nhan tin nhan tu server
    data = clientsocket.recv(1024).decode()

    print("Received from server: " + data)

# Dong socket
clientsocket.close()
