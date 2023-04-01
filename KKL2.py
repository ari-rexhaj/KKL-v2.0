from tkinter import *
import customtkinter
import random

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

##Startup
funnytexts = ["I live in your walls","bitcoin miner","Get mad!","Lykke te 😈","<3","动态网自由门 天安門 天安门","The cake is a lie","Kanye East ©","https://tiny.cc/allahisbig","flyplassen wiki under construction","0 days without sarcasm","they are coming","promise that you will sing about me","'Desperate measures' på spotify"]
TrademarkText = funnytexts[random.randint(0,len(funnytexts)-1)]

ctk = customtkinter
root = ctk.CTk()
root.resizable(False,False)
root.geometry("1500x800")

SideEntryValue = 6
SideEntryValue_Max = 10

Themes = ['Full name','First letters','Periodic table']
NameMode = StringVar()
NameMode.set(Themes[0])

ButtonAmplifier = 1.5
ButtonWidth = 100*ButtonAmplifier
ButtonHeight = 75*ButtonAmplifier

InputFrame = ctk.CTkFrame(root,width=200,corner_radius=0)
ButtonFrame = ctk.CTkScrollableFrame(root,label_text=('Class map\n'+TrademarkText),width=1100,corner_radius=0)
Entry = ctk.CTkTextbox(root,width=200,height=root.winfo_height(),corner_radius=0)
Entry.configure(state=NORMAL)

def EventThemeChanged(theme):
    global Map
    Genmap(Map)

OptionsMenu = ctk.CTkOptionMenu(InputFrame,values=Themes,variable=NameMode,command=EventThemeChanged)

def ReadFile(string):
    with open(string+'.txt') as f:
        return f.readlines()
    
def WriteFile(text=None):   #Done to save map and stuff
    if text == None:
        return
    else:
        print("IDK HOW TO WRITE TO FILE",text)

EleverAmount = len(ReadFile('eksempel'))    #TEMPORARY

def Genlist():  #is perfect
    global EleverAmount
    ClassList = []
    file = 'eksempel'         #TEMPORARY
    EleverName = ReadFile(file)
    for i in range(0,len(EleverName)):
        ClassList.append(EleverName[i-1].replace("\n",""))
    random.shuffle(ClassList)
    EleverAmount = len(ClassList)
    return ClassList


def Genmap(list):
    ButtonFrame.config(width=(10*(2+ButtonWidth) * len(list)))
    for i in range(0,len(list)):
        match NameMode.get():
            case 'Full name':
                Name = list[i]
            case 'First letters':
                Name = list[i][0]
            case 'Periodic table':
                if len(list[i]) >= 2:
                    Name = list[i][0] + list[i][1]  #Reads only the 2 first letters
                else:
                    Name = list[i][0]
        globals()[f"Person_{i}"].configure(text=Name)
            
def Genbuttons(Amount):
    x = 0
    y = 0
    for i in range(0,Amount):
        globals()[f"Person_{i}"] = ctk.CTkButton(ButtonFrame,text="",width=ButtonWidth,height=ButtonHeight)
        globals()[f"Person_{i}"].grid(column=x,row=y,padx=2,pady=2)
        x += 1
        if x%(SideEntryValue) == 0:
            x = 0
            y += 1

def WriteToTextbox(Read,message=''):        #Very primal solution i want to do better here
    EleverName = ReadFile('eksempel')
    if Read is True:
        Entry.delete(1.0,END)
        for Name in EleverName:
            Entry.insert(INSERT, Name)
    if message != '':
        Entry.insert(INSERT,"\n"+message)
        WriteFile(text=message)

def Newmap():
    ButtonFrame.configure(label_text=str("Class map\n"+funnytexts[random.randint(0,len(funnytexts)-1)]))
    WriteToTextbox(True)
    global Map
    Map = Genlist()
    Genmap(Map)


Genbuttons(EleverAmount)
WriteToTextbox(True,message="This was written in the program")
Map = Genlist()
Genmap(Map)


Entry.pack(side='right',fill="y")
InputFrame.pack(side='right',fill="y")
ctk.CTkLabel(InputFrame,text="",width=200).pack(side=BOTTOM)        #For stretching the inputframe to 200 pixels
ctk.CTkLabel(InputFrame,text="Inputs").pack(side='top')
ctk.CTkButton(InputFrame,text="Generate\nnew map",width=150,height=100,command=Newmap).pack()
OptionsMenu.pack(side=BOTTOM)
ctk.CTkLabel(InputFrame,text='Themes').pack(side=BOTTOM)
ButtonFrame.pack(side="left",fill="y")
Entry.configure(height=root.winfo_height())
root.mainloop()