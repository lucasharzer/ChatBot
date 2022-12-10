import socket


# Criando o soquete e aceitando o nome do host de entrada do usuário
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

# Conectando-se ao Servidor
print('Esse é o seu endereço de IP:', ip)
server_host = input('Digite o endereço IP do amigo: ')
name = input('Digite o nome do amigo: ')
 
socket_server.connect((server_host, sport))

# Recebendo Pacotes/Mensagens do Servidor
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()
 
print(server_name, 'se juntou...')

while True:
    message = (socket_server.recv(1024)).decode()
    print(f"\n{server_name}: {message}")
    message = input("\nEu: ")
    socket_server.send(message.encode())
