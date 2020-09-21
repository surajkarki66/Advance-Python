import socket

Host = '127.0.0.1'
Port = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:  # .AF_INET(ipv4) -> address family , Sock_stream -> TCP
    s.bind((Host,Port))       # associate the socket with a specific network interface and port number
    s.listen()    # It enables a server to accept connections
    conn , addr = s.accept()

    with conn:
        print("Connected by ",addr)
        while True:
            data = conn.recv(1024)    #read data send by clients
            if not data:
                break
            conn.sendall(data)   # echos back all data send by client
            conn.send(bytes("Welcome to the server","utf-8"))
            