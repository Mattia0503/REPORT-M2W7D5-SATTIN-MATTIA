import socket
import random

ip = input("Inserire IP: ")
port = int(input("Inserire Porta: "))

connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connection.bind((ip,port))

print("Server connesso!\n")

nmess = int(input("Inserire quanti pacchetti mandare: "))
sent = 0
while sent<nmess :
    messaggio = random._urandom(1024)
    connection.sendall(messaggio)
    sent +=1


