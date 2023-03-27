from tkinter import *
import customtkinter
import random

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

##Startup
ctk = customtkinter
root = ctk.CTk()
root.resizable(False,False)
root.geometry("1200x800")
SideEntryValue = 6

#Neon theme
#EntryColor = '#1F1D36'
#TableColor = '#864879'
#InputColor = '#3F3351'
#FrameColor = '#1F1D36'

ButtonWidth = 100
ButtonHeight = 75
NameMode = 2
#|  Name modes:
#   Full name    = 0
#   First letter  = 1
#   Periodic Table = 2

ButtonFrame = ctk.CTkScrollableFrame(root,label_text='Class map (good luck >:)',width=800,corner_radius=0)
InputFrame = ctk.CTkFrame(root,width=200,corner_radius=0)

def ReadFile(string):
    with open(string+'.txt') as f:
        return f.readlines()

def Genlist():  #is perfect
    ClassList = []
    file = 'eksempel'         #TEMPORARY
    EleverName = ReadFile(file)
    print(EleverName)
    for i in range(0,len(EleverName)):
        ClassList.append(EleverName[i-1].replace("\n",""))
    random.shuffle(ClassList)
    print(ClassList)
    return ClassList


def Genmap(list):
    x = 0
    y = 0
    ButtonFrame.config(width=(10*(2+ButtonWidth) * len(list)))
    for i in range(0,len(list)):
        match NameMode:
            case 0:
                Name = list[i]
            case 1:
                Name = list[i][0]
            case 2:
                Name = list[i][0] + list[i][1]  #Reads only the 2 first letters
            
        globals()[f"Person_{i}"] = ctk.CTkButton(ButtonFrame,text=Name,width=ButtonWidth,height=ButtonHeight)
        globals()[f"Person_{i}"].grid(column=x,row=y,padx=2,pady=2)
        x += 1
        if x%(SideEntryValue) == 0:
            y += 1
            x = 0
            

EleverName = ReadFile('eksempel')
Entry = ctk.CTkTextbox(root,width=200,height=root.winfo_height(),corner_radius=0)
for Name in EleverName:
    Entry.insert(INSERT, Name)
Map = Genlist()
Genmap(Map)
    


Entry.pack(side='right',fill="y")
InputFrame.pack(side='right',fill="y")
ButtonFrame.pack(side="left",fill="y")

Entry.configure(height=root.winfo_height())
root.mainloop()