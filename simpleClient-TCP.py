import socket, sys

# Server IP address
SERVER_IP = '127.0.0.1'
# Port number used by server
PORT = 6666
# Initialize socket object with TCP/Stream type
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#print 'Address before sending:', s.getsockname()
# Initiate a CONNECTION
s.connect((SERVER_IP, PORT))
# Send the message
s.sendall('This is my message')
# Read message stream from server with specific buffer size
data = s.recv(4096)
print 'The server says', repr(data)
# Close connection
s.close()