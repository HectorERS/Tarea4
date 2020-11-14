import socket
import sys
import os
import elgamal
import pickle



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = b'This is the message.  It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)
    while True:
        amount_received = 0
        amount_expected = len(message)
        data = b'solicitando clave publica'
        print(data)
        sock.sendall(data)
        while amount_received < amount_expected:
            data = sock.recv(300)
            print(data)
            if data:
                restored = sock.recv(1024)
                key = pickle.loads(restored)
                file = open('cifrado1.txt', 'w')
                with open('salida1.txt', 'r') as j:
                    for linea in j:
                        data = elgamal.encrypt(key, linea)
                        file.write(data)
                    print('cifrado el archivo1')
                file2 = open('cifrado2.txt', 'w')
                with open('salida2.txt', 'r') as j:
                    for linea in j:
                        data = elgamal.encrypt(key, linea)
                        file2.write(data)
                    print('cifrado el archivo2')
                file3 = open('cifrado3.txt', 'w')
                with open('salida3.txt', 'r') as j:
                    for linea in j:
                        data = elgamal.encrypt(key, linea)
                        file3.write(data)
                    print('cifrado el archivo3')
                file4 = open('cifrado4.txt', 'w')
                with open('salida4.txt', 'r') as j:
                    for linea in j:
                        data = elgamal.encrypt(key, linea)
                        file4.write(data)
                    print('cifrado el archivo4')
                file5 = open('cifrado5.txt', 'w')
                with open('salida5.txt', 'r') as j:
                    for linea in j:
                        data = elgamal.encrypt(key, linea)
                        file5.write(data)
                    print('cifrado el archivo5')
                    break
finally:
    print('closing socket')
    sock.close()
