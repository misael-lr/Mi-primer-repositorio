
import socket

ip = input("Ingresa la direccion IP a escanear: ")

for puerto in range(1,65555):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    result = sock.connect_ex((ip, puerto))

    if result == 0:
        print("Puerto abierto: " + str(puerto))
        sock.close()
    else:
        print("Puerto cerrado: " + str(puerto))
    
