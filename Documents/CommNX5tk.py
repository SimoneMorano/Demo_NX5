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

thread_on = True 

# Definizione della funzione per l'aggiornamento dei dati
def update_time():
    #thread_on = True    
    while True:
        time.sleep(1)
        text_output.configure(text = eip_instance.read_variable('TestInt'))
        text_output1.configure(text = eip_instance.read_variable('TestInt1'))
        text_output2.configure(text = eip_instance.read_variable('TestInt2'))
        text_output3.configure(text = eip_instance.read_variable('TestInt3'))
        AxisMonitor_eip = eip_instance.read_variable('AxisMonitor')
        text_output4.configure(text = round(float(str(AxisMonitor_eip[0]["ActPos"])),2))
        text_output5.configure(text = round(float(str(AxisMonitor_eip[0]["ActVel"])),2))
        text_output6.configure(text = round(float(str(AxisMonitor_eip[1]["ActPos"])),2))
        text_output7.configure(text = round(float(str(AxisMonitor_eip[1]["ActVel"])),2))
        text_output8.configure(text = str(AxisMonitor_eip[0]["Enabled"]))
        text_output9.configure(text = str(AxisMonitor_eip[0]["Error"]))
        text_output10.configure(text = str(AxisMonitor_eip[1]["Enabled"]))
        text_output11.configure(text = str(AxisMonitor_eip[1]["Error"]))

        if str(AxisMonitor_eip[0]["Enabled"]) == "True":
            text_output8.configure(fg_color = "yellow", text_color = "black")
        else:
            text_output8.configure(fg_color = "black", text_color = "white")
            
        if str(AxisMonitor_eip[0]["Error"]) == "True":
            text_output9.configure(fg_color = "yellow", text_color = "black")
        else:
            text_output9.configure(fg_color = "black", text_color = "white")

        if str(AxisMonitor_eip[1]["Enabled"]) == "True":
            text_output10.configure(fg_color = "yellow", text_color = "black")
        else:
            text_output10.configure(fg_color = "black", text_color = "white")
            
        if str(AxisMonitor_eip[1]["Error"]) == "True":
            text_output11.configure(fg_color = "yellow", text_color = "black")
        else:
            text_output11.configure(fg_color = "black", text_color = "white")
            
        
'''      
        if thread_on == False:
            return
def set_stop():
    global thread_on
    thread_on = False 
'''
        
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

entry_1 = customtkinter.CTkEntry(root)
entry_1.grid(row=1, column=0)

entry_2 = customtkinter.CTkEntry(root)
entry_2.grid(row=2, column=0)

entry_3 = customtkinter.CTkEntry(root)
entry_3.grid(row=3, column=0)

entry_4 = customtkinter.CTkEntry(root)
entry_4.grid(row=4, column=0)

button_1 = customtkinter.CTkButton(root, text= "Write", command= write_var)
button_1.grid(row=0, column=0)

text_output = customtkinter.CTkLabel(root, text="0", width=150)
text_output.grid(row=1, column=1)

text_output1 = customtkinter.CTkLabel(root, text="0", width=150)
text_output1.grid(row=2, column=1)

text_output2 = customtkinter.CTkLabel(root, text="0", width=150)
text_output2.grid(row=3, column=1)

text_output3 = customtkinter.CTkLabel(root, text="0", width=150)
text_output3.grid(row=4, column=1)

text_output4 = customtkinter.CTkLabel(root, text="0", width=150)
text_output4.grid(row=5, column=1)

text_output5 = customtkinter.CTkLabel(root, text="0", width=150)
text_output5.grid(row=6, column=1)

text_output6 = customtkinter.CTkLabel(root, text="0", width=150)
text_output6.grid(row=7, column=1)

text_output7 = customtkinter.CTkLabel(root, text="0", width=150)
text_output7.grid(row=8, column=1)

text_output8 = customtkinter.CTkLabel(root, text="a", width=150)
text_output8.grid(row=5, column=0)

text_output9 = customtkinter.CTkLabel(root, text="a", width=150)
text_output9.grid(row=6, column=0)

text_output10 = customtkinter.CTkLabel(root, text="a", width=150)
text_output10.grid(row=7, column=0)

text_output11 = customtkinter.CTkLabel(root, text="a", width=150)
text_output11.grid(row=8, column=0)

button_2 = customtkinter.CTkButton(root, text= "Enable", command = nx_enable)
button_2.grid(row=1, column=2)

button_3 = customtkinter.CTkButton(root, text= "Disable", command= nx_disable)
button_3.grid(row=2, column=2)

button_4 = customtkinter.CTkButton(root, text= "Jog", command= nx_jog)
button_4.grid(row=3, column=2)

button_5 = customtkinter.CTkButton(root, text= "Stop", command= nx_stop)
button_5.grid(row=4, column=2)

root.mainloop()