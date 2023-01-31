#
#     IPBEJA: ESTIG
#
#
#


from classes.udpflood import udpflood
#from classes.logview import logview
#from classes.exportfile import exportfile     
from classes.message import message
from classes.portscan import portscan
from classes.synflood import synflood



#Construcao do menu

def menu():
    print("Bemvindo ao trabalho de MESI - LPD")
    print("Escolha a opcao que pretende:")
    print("1. Analisar o nr de portos abertos num ip ou gama")
    print("2. Fazer um ataque UDP flood")
    print("3. Fazer um ataque SYN flood")
    print("4. Visualizar o log de um mikrotik")
    print("5. Troca de mensagens utilizando RSA")
    print("x para sair")
    print("")

  
    escolha = input("O que pretende fazer? ")

    if escolha == '1':
        print("PORTSCAN")
        p = portscan()
        p.portscan()
    elif escolha == '2':
        print("ATAQUE DOS")
        d = udpflood()
        d.dos()
    elif escolha == '3':
        print("ATAQUE SYN TCP")
        s = synflood()
        s.synflood()
    elif escolha == '4':
        print("LOG MIKROTIK")
        l = logview()
    elif escolha == '5':
        print("MSG RSA")
        m = message()
        m.menumessage()
    elif escolha == 'x':
        print("ADEUS")
        exit()

    else:
        print("Opção inválida.")


continuar = True
while continuar:
    menu()
    escolha = input("Deseja continuar? (S/N) ")
    if escolha.upper() == 'N':
        continuar = False
        print("ADEUS")
        exit()


    










