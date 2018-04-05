from thread import start_new_thread

def clientthread(conn):     
	#infinite loop so that function do not terminate and thread do not end.
	while True:		
		try :
			# Read the message stream from client
			data = conn.recv(4096)
			# Check if receive data is not empty
			if data :
				print 'The client says ', data
				# Send back the message to client
				conn.sendall('OK '+data)
			# Empty string means connection closed
			else :
				break			 
		except socket.error, e :
			break   
	#came out of loop
	print "Connection closed by client"
	conn.close()

print 'Listening at', sock.getsockname()
while True:
	# Accept connection, return client socket and address
	conn, addr = sock.accept()
	# Read the message stream from client with specific buffer size
	start_new_thread(clientthread ,(conn,))
