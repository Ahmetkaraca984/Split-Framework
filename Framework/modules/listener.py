import socket
import os

CONFIG_PATH = os.path.join("config", "listener_conf.txt")

# Config dosyasını oku
with open(CONFIG_PATH, "r") as f:
    lines = f.readlines()
    LHOST = lines[0].strip()
    LPORT = int(lines[1].strip())  


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind((LHOST, LPORT))

# Dinlemeye başla
s.listen(5)  
print(f"Listener başlatıldı: {LHOST}:{LPORT}")
client,addr= s.accept()
while True:
    client, addr = s.accept()
    print(f"Yeni Bağlantı: {addr}")