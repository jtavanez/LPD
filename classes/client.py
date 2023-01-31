import socket
from classes.rsa import rsa

class cliente:

    def cliente(self):

        r = rsa()
        ku,kr = r.generate_keys()
        print("chave publica", ku)
        print("Chave privada", kr)  

        e = ku[0] 
        n = ku[1]
        message = 2

        criptogram = r.encrypt(message, e, n)
        print ("Mensagem encriptada: " , criptogram)  

        d= kr[0]
        print (message, e , n , d)
        message = r.decrypt(criptogram, d, n)
        print(message)


       
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = input("Introduzir o ip do servidor ")
        port = int(input("Qual o porto a usar? "))
        s.connect((host,port))
        dataFromServer = s.recv(1024)
        print(dataFromServer.decode())
        dataToServer = input("Msg a mander ao sr. Servidor: ")

        r = rsa()
        ku,kr = r.generate_keys()
        print("chave publica", ku)
        print("Chave privada", kr)  

        e = ku[0] 
        n = ku[1]
        message = int("123")

        criptogram = r.encrypt(message, e, n)
        print ("Mensagem encriptada: " , criptogram)  

        s.send(dataToServer.encode())
        s.close()