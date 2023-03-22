import socket

# Tao 1 socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lay dia chi ip local
host = socket.gethostname()

port = 9999

# Mo lien ket voi 1 cong
serversocket.bind((host, port))

# Lắng nghe các kết nối đến
serversocket.listen(1)

print("Server listening on port: %s" % str(port))

# Cho ket noi
connection, address = serversocket.accept()

print("Connection from: " + str(address))

while True:
    # Nhan du lieu den
    data = connection.recv(1024).decode()

    if not data:
	#neu du lieu nhan duoc ma rong thi dong ket noi
        break

    print("Received data: " + data)

    # Gui du lieu di
    response = input("Enter a response: ")
    connection.send(("ACK: " + response).encode())

# Dong ket noi
connection.close()
