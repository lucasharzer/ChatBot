import socket
 

# Criando o soquete e recuperando o nome do host
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080

# Ligando o Host e a Porta
new_socket.bind((host_name, port))

print("Conexão bem-sucedida!")
print("Esse é seu IP:", s_ip)

# Ouvindo conexões
name = input('Nome de entrada: ')
 
new_socket.listen(1) 

# Aceitando Conexões de Entrada
conn, add = new_socket.accept()
 
print("Conexão recebida de", add[0])
print('Conexão estabelecida. Conectado de:', add[0])

# Armazenando dados de conexão de entrada
client = (conn.recv(1024)).decode()
print(client + ' conectou.')
 
conn.send(name.encode())

# Entrega de pacotes/mensagens
while True:
    message = input('\nEu: ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(f"\n{client}: {message}")
