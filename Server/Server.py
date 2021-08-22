import socket


class server:
    
    PORT = 8000

    def __init__(self, HOST):
        self.HOST = HOST
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

    def chat_server(self):
        self.s.listen(99999)
        self.s.bind((self.HOST, self.PORT))

        conn, addr = self.s.accept()

        text_1 = bytes(text, 'utf-8')

        self.data = conn.recv(1024)

    def chat_client(self, text):
        text_1 = bytes(text, 'utf-8')

        try:
            self.s.connect((self.HOST, self.PORT)) # tiến hành kết nối đến server
        except:
            return False

        self.s.sendall(text_1) # Gửi dữ liệu lên server
    def connect(self):
        try:
            self.s.connect((self.HOST, self.PORT)) # tiến hành kết nối đến server
        except:
            return False
    def close(self):
        self.s.close()