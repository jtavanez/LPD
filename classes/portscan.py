import socket
import subprocess
import sys
import time
from datetime import datetime

class portscan: 
    
    def portscan(self):
        rmip = input("\t Insira o ip que pretende fazer scan: ")
        r1 = int(input("\t Insira o porto de inicio: \t"))
        r2 = int(input("\t Insira o porto final: \t"))
        print("\n A fazer o portscan... ", rmip)
        t1 = datetime.now()
        i = 0
        try:
            for port in range(r1, r2):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((rmip, port))
                if result == 0:
                    i = i + 1
                    print("Porto Aberto:-->\t", port)
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

        print("Tem estes portos abertos: ", i)
        t2 = datetime.now()
        total = t2 - t1
        print("Tempo que demorei a fazer isto: ", total)
        time.sleep(5)
