import base64
import time
file = input("Encode Edilecek Dosyayı Söyle: ")
with open(file, "rb") as f:  
    içerik = f.read()
output = base64.b64encode(içerik).decode("utf-8")
print("Şifrelenmiş Hali:")
time.sleep(1)
print(output)