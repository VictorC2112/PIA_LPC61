import socket
import sys
import threading

print("1: Escaneo UDP")
print("2: Escaneo completo")
print("3: Deteccion de sistema operativo")
print("4: Escaneo de red con ping")
print()

opcion = input("Escribe el numero de opcion: ")

if opcion == 1:
    def tcp_test(port):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print("Opened Port:", port)
    ports=[21, 22, 25, 80]
    for port in range(start_port, end_port):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((target_ip, port))
    if result == 0:
        opened_ports.append(port)
elif opcion == 2:
    def tcp_test(port):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print("Opened Port:", port)
        for i in range(1,255):
            addr="192.168.0.{}".format(i)
        for port in ports:
            result=scan(addr, port)
            if result==0:
                print(addr, port, "OK")
            else:
                print(addr, port, "Failed")

elif opcion == 3:
    host = sys.argv[1]
    portstrs = sys.argv[2].split('-')
    start_port = int(portstrs[0])
    end_port = int(portstrs[1])
    hilos = []
    for port in range(start_port, end_port):
        hilo = threading.Thread(target=tcp_test, args=(port,))
        hilos.append(hilo)
        hilo.start()

elif opcion == 4:
    def scan(addr, port):
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
    
        result = socket_obj.connect_ex((addr,port))
    
        socket_obj.close()
    
        return result
ports=[21, 22, 25, 80]
for i in range(1,255):
    addr="192.168.0.{}".format(i)
    for port in ports:
        result = scan(addr, port)
        if result==0:
            print(addr, port, "OK")
        else:
            print(addr, port, "Failed")

else:
    print("Opcion no encontrada")
    
# Escaner de puertos ip
# Víctor Manuel Cárdenas Cavazos
# Matricula: 1919410