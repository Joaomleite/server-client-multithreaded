import socket
import threading
import logging

class Server:

    def executeServer(self):
        ip = socket.gethostbyname(socket.gethostname())
        port = 5566
        addr = (ip, port)


        logging.info("Starting server...")
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(addr)
        self.server.listen()
        logging.info(f"Server is listening on {ip}:{port}")
        self.createThreadByConnection()

    def createThreadByConnection(self):
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handleClientThread, args=(conn,addr))
            thread.start()
            logging.info(f"CONNECTIONS: {threading.active_count() - 1}")

    def handleClientThread(self, conn, addr):
        logging.info(f"Client Connected: {addr}")
        connect = True
        threadName = threading.current_thread().name.replace(' (handleClientThread)','')

        while connect:
            message = conn.recv(1024).decode('utf-8')
            if message == 'disconnect':
                connect = False
            print(f"[{addr}]: {message}")
            if message.lower() == "pode me prestar um serviço?":
                message = f"Serviço prestado pela thread: {threadName}:{threading.get_ident()}"
                conn.send(message.encode('utf-8'))
            else: 
                message = f"Servidor não reconhece essa mensagem"
                conn.send(message.encode('utf-8'))

        self.closeConnection(conn, addr)


    def closeConnection(self,conn, addr):
        conn.close()
        logging.info(f"Client Disconnected: {addr} ")

        
    def __init__(self):
        logging.basicConfig(format="[SERVER]: %(message)s ", level=logging.INFO)

if __name__ == "__main__":
   server = Server()
   server.executeServer()