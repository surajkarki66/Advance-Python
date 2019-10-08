import socket

class Server:
       
    Host = '127.0.0.1'
    Port = 65432

    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.bind((Server.Host,Server.Port))       # associate the socket with a specific network interface and port number
        self.s.listen()

    def connection(self):
        conn, addr = self.s.accept()

        with conn:
            print(f'Connected by {addr}')
            while True:
                data = conn.recv(1024)    #read data send by clients
                if not data:
                    break
                conn.sendall(data)   # echos back all data send by client
                conn.send(bytes("Welcome to the server","utf-8"))
            
       

s = Server()

s.connection()