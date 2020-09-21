import socket

class Client:
    Host = '127.0.0.1'
    Port = 65432

    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
    
    def connection(self):
        self.s.connect((Client.Host,Client.Port))
        self.s.sendall(b'Hello')
        data = self.s.recv(1024)
        print(data.decode("utf-8"))
        print(f'Received {repr(data)}')

    

    


c =Client()
c.connection()

    
