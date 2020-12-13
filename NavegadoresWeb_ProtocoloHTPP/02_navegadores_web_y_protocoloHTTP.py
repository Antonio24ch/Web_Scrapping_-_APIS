
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.connect(('www.w3.org', 80)) #puerto 80, conec servidor

# Solcitan el archivo, protoclo HTPP se utliza get
# get 'dame archivo' protocolo http version 1.0 -- salto de linea, encode para enviar al servidor
cmd = 'GET https://www.w3.org/TR/PNG/iso_8859-1.txt HTTP/1.0\r\n\r\n'.encode()

# Send para enviar datos
sock.send(cmd)

# Para salir del bucle break
while True:
    data = sock.recv(512) #512 bits
    if len(data)<1:
        break # Cuando los datos sean menor que 1, para salir del bucle se usa break
    print(data.decode(), end= '')
        
sock.close() 

# RECEPCION PAGINAS WEB - LIBRERIA URLLIB
# Extracción de una forma más rápida y fácil

import urllib.request

pw = urllib.request.urlopen('https://www.w3.org/TR/PNG/iso_8859-1.txt')

for line in pw: #recorrer objeto para imprimir contenido
    print(line.decode().strip())