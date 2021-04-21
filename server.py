
import time, socket, sys 

time.sleep(1) 

# get parameters
host_name = socket.gethostname() 
ip = socket.gethostbyname(host_name) 
port = 1234 

# setting up parameters for socket
soc = socket.socket() 
soc.bind((host_name, port)) 
print(host_name, '({})'.format(ip)) 

# get client name
name = input('Enter Your name: ') 

#Try to locate using socket 
soc.listen(1) 
print('Waiting for incoming connections...') 

# accept and estabilish connection
connection, addr = soc.accept() 
print("Received connection from ", addr[0], "(", addr[1], ")\n") 
print("Connection Established")
print("Connected From: {}, ({})".format(addr[0], addr[0]))
client_name = connection.recv(1024) 
client_name = client_name.decode() 
print(client_name + ' has connected.') 
print('Press [bye] to leave the chat room') 
connection.send(name.encode()) 

# route messages while connection is not disrupted
while True: 
    message = input('You say, ') 
    if message == '[bye]': 
        message = 'Good Night...' 
        connection.send(message.encode()) 
        print("\n") 
        break 
    connection.send(message.encode()) 
    message = connection.recv(1024) 
    message = message.decode() 
    print(client_name, ' said, ', message) 
