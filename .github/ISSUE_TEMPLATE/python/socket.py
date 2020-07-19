#server 
import socket
UDP_IP = "192.168.31.163"
UDP_PORT = 5005
MESSAGE = b"Hello word"

printf("UDP target IP: %s"%UDP_IP)
print("UDP target port: %s"% UDP_PORT)
printf("message: %s" %s MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                       sock.bind((UDP_IP,UDP_PORT)))
 