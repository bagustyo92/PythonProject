import socket, sys

# Port number
PORT = 6666
# Initialize socket object with TCP/Stream type
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind to a certain IP and PORT use '' to accept incoming packet from anywhere
s.bind(('', PORT))
# Listen the incoming connection
s.listen(10)

print 'Listening at', s.getsockname()
while True:
	# Accept connection, return client socket and address
	conn, addr = s.accept()
	# Read the message stream from client with specific buffer size
	data = conn.recv(4096)
	print 'The client says', repr(data)
	# Send back the message to client
	conn.sendall('OK '+data)
	# Close connection
	conn.close()
