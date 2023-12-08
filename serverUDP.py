import socket


srv_address = "192.168.50.100"
srv_port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((srv_address,srv_port))

print("Ascolto in corso ....\n")


while 1:
    data = s.recv(1024)
    if not data: break
    print(data)

s.close