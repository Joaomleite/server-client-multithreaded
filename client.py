import socket
import logging


class Client:
    def executeClient(self):
        ip = socket.gethostbyname(socket.gethostname())
        port = 5566
        addr = (ip, port)

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(addr)

        logging.info(f"[CONNECTED]: Connected to server {ip}:{port}")
        self.handleMessagesToClient()
        
    def handleMessagesToClient(self):
        connected = True

        if connected:
            message = "Pode me prestar um serviço?"
            self.client.send(message.encode('utf-8'))
            message = self.client.recv(1024).decode('utf-8')
            logging.info(f"[SERVER]: {message}")

        while connected:
            message = input("Digite a requisição: ")
            self.client.send(message.encode('utf-8'))

            if message == 'disconnect':
                connected = False
            else:
                message = self.client.recv(1024).decode('utf-8')
                logging.info(f"[SERVER]: {message}")

    def __init__(self):
        logging.basicConfig(format="%(message)s ", level=logging.INFO)

if __name__ == "__main__":
   client = Client()
   client.executeClient()