import time
from aphyt import omron
from threading import Thread
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("600x600")
root.title("Python NX5 Comm")

eip_instance = omron.n_series.NSeries()
eip_instance.connect_explicit('192.168.250.1')
eip_instance.register_session()

my_tab = customtkinter.CTkTabview(root)
my_tab.pack(pady=10)

tab_1 = my_tab.add("tab 1")
tab_2 = my_tab.add("Tab 2")


thread_on = True 

# Definizione della funzione per l'aggiornamento dei dati
def update_time():
       
    while True:
        time.sleep(1)
        text_output.configure(text = eip_instance.read_variable('TestInt'))
        text_output1.configure(text = eip_instance.read_variable('TestInt1'))
        text_output2.configure(text = eip_instance.read_variable('TestInt2'))
        text_output3.configure(text = eip_instance.read_variable('TestInt3'))
        AxisMonitor_eip = eip_instance.read_variable('AxisMonitor')
        text_actpos_0.configure(text = round(float(str(AxisMonitor_eip[0]["ActPos"])),2))
        text_actvel_0.configure(text = round(float(str(AxisMonitor_eip[0]["ActVel"])),2))
        text_actpos_1.configure(text = round(float(str(AxisMonitor_eip[1]["ActPos"])),2))
        text_actvel_1.configure(text = round(float(str(AxisMonitor_eip[1]["ActVel"])),2))
        text_enabled_0.configure(text = str(AxisMonitor_eip[0]["Enabled"]))
        text_error_0.configure(text = str(AxisMonitor_eip[0]["Error"]))
        text_enabled_1.configure(text = str(AxisMonitor_eip[1]["Enabled"]))
        text_error_1.configure(text = str(AxisMonitor_eip[1]["Error"]))

        if str(AxisMonitor_eip[0]["Enabled"]) == "True":
            text_enabled_0.configure(fg_color = "yellow", text_color = "black")
        else:
            text_enabled_0.configure(fg_color = "black", text_color = "white")
            
        if str(AxisMonitor_eip[0]["Error"]) == "True":
            text_error_0.configure(fg_color = "yellow", text_color = "black")
        else:
            text_error_0.configure(fg_color = "black", text_color = "white")

        if str(AxisMonitor_eip[1]["Enabled"]) == "True":
            text_enabled_1.configure(fg_color = "yellow", text_color = "black")
        else:
            text_enabled_1.configure(fg_color = "black", text_color = "white")
            
        if str(AxisMonitor_eip[1]["Error"]) == "True":
            text_error_1.configure(fg_color = "yellow", text_color = "black")
        else:
            text_error_1.configure(fg_color = "black", text_color = "white")

        
def write_var():
    eip_instance.write_variable('TestInt', int(entry_1.get()))
    eip_instance.write_variable('TestInt1', int(entry_2.get()))
    eip_instance.write_variable('TestInt2', int(entry_3.get()))
    eip_instance.write_variable('TestInt3', int(entry_4.get()))

def nx_enable():
    eip_instance.write_variable('PyCmdEnable', 1)
    
def nx_disable():
    eip_instance.write_variable('PyCmdDisable', 1)
    
def nx_jog():
    eip_instance.write_variable('PyCmdMovVel', 1)
    
def nx_stop():
    eip_instance.write_variable('PyCmdStop', 1)

# Avvio del thread se non già avviato
thread1 = Thread(target=update_time)
thread1.start()

entry_1 = customtkinter.CTkEntry(tab_1)
entry_1.grid(row=1, column=0)

entry_2 = customtkinter.CTkEntry(tab_1)
entry_2.grid(row=2, column=0)

entry_3 = customtkinter.CTkEntry(tab_1)
entry_3.grid(row=3, column=0)

entry_4 = customtkinter.CTkEntry(tab_1)
entry_4.grid(row=4, column=0)

button_1 = customtkinter.CTkButton(tab_1, text= "Write", command= write_var)
button_1.grid(row=0, column=0)

text_output = customtkinter.CTkLabel(tab_1, text="0", width=150)
text_output.grid(row=1, column=1)

text_output1 = customtkinter.CTkLabel(tab_1, text="0", width=150)
text_output1.grid(row=2, column=1)

text_output2 = customtkinter.CTkLabel(tab_1, text="0", width=150)
text_output2.grid(row=3, column=1)

text_output3 = customtkinter.CTkLabel(tab_1, text="0", width=150)
text_output3.grid(row=4, column=1)

text_actpos_0 = customtkinter.CTkLabel(tab_2, text="0", width=150)
text_actpos_0.grid(row=5, column=1)

text_actvel_0 = customtkinter.CTkLabel(tab_2, text="0", width=150)
text_actvel_0.grid(row=6, column=1)

text_actpos_1 = customtkinter.CTkLabel(tab_2, text="0", width=150)
text_actpos_1.grid(row=7, column=1)

text_actvel_1 = customtkinter.CTkLabel(tab_2, text="0", width=150)
text_actvel_1.grid(row=8, column=1)

text_enabled_0 = customtkinter.CTkLabel(tab_2, text="a", width=150)
text_enabled_0.grid(row=5, column=0)

text_error_0 = customtkinter.CTkLabel(tab_2, text="a", width=150)
text_error_0.grid(row=6, column=0)

text_enabled_1 = customtkinter.CTkLabel(tab_2, text="a", width=150)
text_enabled_1.grid(row=7, column=0)

text_error_1 = customtkinter.CTkLabel(tab_2, text="a", width=150)
text_error_1.grid(row=8, column=0)

button_2 = customtkinter.CTkButton(tab_2, text= "Enable", command = nx_enable)
button_2.grid(row=5, column=2)

button_3 = customtkinter.CTkButton(tab_2, text= "Disable", command= nx_disable)
button_3.grid(row=6, column=2)

button_4 = customtkinter.CTkButton(tab_2, text= "Jog", command= nx_jog)
button_4.grid(row=7, column=2)

button_5 = customtkinter.CTkButton(tab_2, text= "Stop", command= nx_stop)
button_5.grid(row=8, column=2)

root.mainloop()