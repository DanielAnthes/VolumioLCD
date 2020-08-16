import socket

PORT = 9000

client_socket = socket.socket()
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # try to avoid address in use errors when restarting the script
client_socket.bind(("localhost", PORT))
client_socket.listen(1)

print("listening on port " + str(PORT))

connection, address = client_socket.accept()

print("connected with: " + address[0] + ":" + str(address[1]))

msg = ""

while True:
	data = connection.recv(1024)
	msg += data
	if not data:
		break

print("Reveived message: " + msg)

client_socket.close()

