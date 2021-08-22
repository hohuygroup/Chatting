import socket

HOST = '127.0.0.1'    # Cấu hình address server
PORT = 8000              # Cấu hình Port sử dụng       

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)

client, addr = s.accept()

data = client.recv(1024)
str_data = data.decode("utf8")
print("Client: " + str_data)
