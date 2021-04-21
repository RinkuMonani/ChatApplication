import time, socket, sys 

# get parameters
shost = socket.gethostname() 
ip = socket.gethostbyname(shost) 
print(shost, '({})'.format(ip)) 

# get information to connect with the server 
server_host = input('Enter server\'s IP address:') 
name = input('Enter Your Name: ') 
port = 1234 
print('Trying to connect to the server: {}, ({})'.format(server_host, port)) 
time.sleep(1) 

# get socket parameters
soc = socket.socket() 
soc.connect((server_host, port)) 
print("Connected...\n") 

# estabilish connection
soc.send(name.encode()) 
server_name = soc.recv(1024) 
server_name = server_name.decode() 
print('{} has joined...'.format(server_name)) 
print('Enter [bye] to exit.')

# listen/send messages while connection is not disrrupted
while True: 
    message = soc.recv(1024) 
    message = message.decode() 
    print(server_name, " says, ", message) 
    message = input(str("You say, ")) 
    if message == "[bye]": 
        message = "Leaving the Chat room"
        soc.send(message.encode()) 
        print("\n") 
        break 

    soc.send(message.encode()) 



