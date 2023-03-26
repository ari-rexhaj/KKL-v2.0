from tkinter import *
import customtkinter
import random

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

ctk = customtkinter
root = ctk.CTk()
root.geometry("900x800")

EleverName = []
def ReadFile(string):
    global EleverName
    with open(string+'.txt') as f:
        EleverName = f.readlines()

def Genlist():
    global EleverName
    Spots = []
    for i in range(0,len(EleverName)):
        Spots.append(i)
    (0,len(EleverName))
    for i in range(0,len(EleverName)):
        rng = int(random.randint(0,len(EleverName)-1))
        Name = EleverName[i-1]
        Spot = Spots[rng]
        Spots.pop[rng]
##Startup
ReadFile('elever')
ButtonFrame = ctk.CTkScrollableFrame(root,label_text='Class map (good luck >:)')
InputFrame = ctk.CTkFrame(root)

Entry = ctk.CTkTextbox(root,width=150,height=root.winfo_height())
for Name in EleverName:
    Entry.insert(INSERT, Name.replace('\n','')+','+'\n')

ExampleButton = ctk.CTkButton(ButtonFrame,text='Ari Rexhaj',width=100,height=75)

        
Genlist()



ButtonFrame.pack(side='left')
Entry.pack(side='right')
InputFrame.pack(side='right')

ExampleButton.grid(column=0,row=0)
Entry.configure(height=root.winfo_height())
root.mainloop()