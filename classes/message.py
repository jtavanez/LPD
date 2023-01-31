from classes.server import servidor
from classes.client import cliente  

class message: 
    
    def menumessage(self):
        print("Bemvindo ao nosso servidor/cliente de mensagens")
        print("Escolha a opcao que pretende:")
        print("1. Usar a aplicacao como servidor")
        print("2. Usar a aplicacao como cliente")

        escolha = input("O que pretende fazer? ")
        
        if escolha == '1':
            print("Servidor")
            s = servidor()
            s.servidor()

        elif escolha == '2':
            print("Cliente")
            c = cliente()
            c.cliente()

        else: 
            print("Opção Invalida.")




""" # Geração de chaves
    (public_key, private_key) = generate_keys()

    # Mensagem a ser enviada
    message = input("Que mensagem enviamos? ",123)

    # Criptografia da mensagem com a chave pública
    encrypted_message = encrypt(message, *public_key)

    # Decriptografia da mensagem com a chave privada
    decrypted_message = decrypt(encrypted_message, *private_key)

    # Exibe a mensagem original e a decriptografada
    print("Message:", message)
    print("Decrypted Message:", decrypted_message)
 """
