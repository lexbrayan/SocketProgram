#Get socket function
import socket
import sys 

# The start function is called if all connections and binding was successful
# After all successful communications and procols have been established , an infite loop is called
# to constantly listen for an message that might be recieved from the Client (in this case an htlm page) 
def start():
    while True:
	print('The server is ready to receive from {}'.format(SERVER))

	# wait for a new connection to the server
	conn, addr = serverSocket.accept()

	try:
		# gets message from the client and then decodes the message, 
		# 2048 represents the max byte size of the message to be decoded from the index.html file i created
		msg = conn.recv(5000).decode()
		
		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]
		filename = msg.split()[1]
		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 
		f = open(filename[1:])
		
		#Send one HTTP header line into socket
		data = f.read()
		
		#send 200 ok header line
		conn.send("HTTP/1.1 200 OK\r\n\r\n".encode()) 
 
		#Send the content of the requested file to the client
		for i in range(0, (len(data)+1)):  
			conn.send(data[i].encode())
		conn.send("\r\n".encode()) 
		
		# This closes the connection if the message has successfully ended.
		conn.close()

	except IOError:
			#This is the response that will be sent if the file was not found
			conn.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
			conn.send("<html><head></head><body><h1>404 File Not Found</h1></body></html>\r\n".encode())

			#Close client socket
			conn.close()


#creates TCP server socket 
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Defines the port that would be used
serverPort = 1991

#This will bind the port to an address
serverSocket.bind(("", serverPort))
#Gets the name of the host and displays it to the User's screen.
SERVER= socket.gethostname()
#Tells the socket to listen for requests
serverSocket.listen(5)

#if all connections and protocols are established the start function will be called.
start()

#closes the server socket
serverSocket.close()  

#Exit or terminate the program *
