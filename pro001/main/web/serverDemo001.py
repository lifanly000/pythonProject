#coding=utf-8

import socket

# listen_socket = socket.socket()
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = "127.0.0.1"
port = 8888
listen_socket.bind((host,port))
listen_socket.listen(1)

while True:
    client_conn,client_addr = listen_socket.accept()
    request = client_conn.recv(1024)
    print request
    print client_addr

    http_response = """
    HTTP/1.1 200 OK

    Hello World !
    """
    client_conn.send("Hello World!")
    # client_conn.sendall(http_response)
    client_conn.close()
