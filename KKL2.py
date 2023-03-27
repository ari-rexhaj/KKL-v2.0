from tkinter import *
import customtkinter
import random

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

##Startup
ctk = customtkinter
root = ctk.CTk()
root.resizable(False,False)
root.geometry("1200x800")
SideEntryValue = 6

ButtonWidth = 100
ButtonHeight = 75

ButtonFrame = ctk.CTkScrollableFrame(root,label_text='Class map (good luck >:)',width=800)
InputFrame = ctk.CTkFrame(root,width=200)

def ReadFile(string):
    with open(string+'.txt') as f:
        return f.readlines()

def Genlist():
    def takeSecond(elem):
        return elem[1]
    global EleverName
    Spots = []
    for i in range(0,len(EleverName)):
        Spots.append(i)
    random.shuffle(Spots)

    ClassList = []
    (0,len(EleverName))
    for i in range(0,len(EleverName)):
        Name = EleverName[i-1].replace("\n","")
        Spot = Spots[0]
        Spots.pop(0)
        ClassList.append((Name,Spot))

    ClassList.sort(key=takeSecond)
    print(ClassList)
    return ClassList


def Genmap(list):
    x = 0
    y = 0
    ButtonFrame.config(width=(10*(2+ButtonWidth) * len(list)))
    for i in range(0,len(list)):
        Name = list[i][0]
        globals()[f"Person_{i}"] = ctk.CTkButton(ButtonFrame,text=Name,width=ButtonWidth,height=ButtonHeight)
        globals()[f"Person_{i}"].grid(column=x,row=y,padx=2,pady=2)
        x += 1
        if x%(SideEntryValue) == 0:
            y += 1
            x = 0
            

EleverName = ReadFile('elever')
Entry = ctk.CTkTextbox(root,width=200,height=root.winfo_height())
for Name in EleverName:
    Entry.insert(INSERT, Name.replace('\n','')+','+'\n')
Map = Genlist()
Genmap(Map)
    


Entry.pack(side='right',fill="y")
InputFrame.pack(side='right',fill="y")
ButtonFrame.pack(side="left",fill="y")

Entry.configure(height=root.winfo_height())
root.mainloop()