#coding:utf-8
import tkinter 
from tkinter import messagebox



help(tkinter)

def show_about():
    app_second = tkinter.Toplevel(app)
    app_second.title(" about windows")
    
    var_lab=tkinter.Label(app_second, text="a propos de windows")

    
    btn=tkinter.Entry(app_second)

    btn.pack()
    var_lab.pack()

# creaction de la fenetre
app=tkinter.Tk()
app.geometry("650x600+100+100")
app.title("creaction d un menu")


cadre=tkinter.LabelFrame(app, text="fenetre windows", width=12)
var_btn=tkinter.Button(cadre,text="OK")
lab=tkinter.Label(cadre, text="un cadre" ,width=30, height=15, borderwidth=3)


main_menu=tkinter.Menu(app)

option=tkinter.Menu(main_menu, tearoff=0)
option.add_command(label="option 1")
option.add_command(label="option 1")
option.add_command(label="quit", command=app.quit)


comand=tkinter.Menu(main_menu, tearoff=0)
comand.add_command(label="command 1")
comand.add_command(label="command 1")
comand.add_command(label="a propos", command=show_about)


main_menu.add_cascade(label ="premier", menu=option)

main_menu.add_cascade(label="second", menu=comand)












app.config(menu=main_menu)


















lab.pack()
var_btn.pack(ipadx=3, ipady=3)
cadre.pack(side="top", expand=1)

















































"""
def update(*args):
    lab.set(var_ent.get())


var_ent=tkinter.StringVar()
var_entry=tkinter.Entry(app, textvariable=var_ent)

lab=tkinter.StringVar()
lab.trace_add("write", update)
var_label=tkinter.Label(app,textvariable=lab)


var_label.pack()
var_entry.pack()
"""



'''
def hello():
    print("j ecris hello sur le terminal")

def messageErreur ():
    messagebox.showerror("error"," une erreur est supvenu")


btn=tkinter.Button(app, text="erreur", command=messageErreur)
btn.pack()
'''


#message d erreur 



#creaction widget




"""

var_buton=tkinter.Button(app, text=" OK" ,width=5, height=2, command=hello)

var_entry=tkinter.Entry(app, show="**")
var_label1=tkinter.Label(app, text="veuillez entrer un mot de pass")
var_entry1=tkinter.Entry(app, show="**")
var_label2=tkinter.Label(app, text="controler le mot de pass")


var_check=tkinter.Checkbutton(app, text="natation" ,onvalue=2,offvalue=3)
#var_check1=tkinter.Checkbutton(app, text="plongee")
var_radio=tkinter.Radiobutton(app, text="femme", value=1)
var_radio1=tkinter.Radiobutton(app, text="homme", value=0)

var_scale=tkinter.Scale(app)


# affiche le texte sur une ligne
var_label=tkinter.Label(app, text="")
var_label.config(text="bienvenue ds mon quartier")

liste=tkinter.Listbox(app)
liste.insert(1, "windown")
liste.insert(2, "linux")
liste.insert(3, "macOs")
# affiche sur plusieurs ligne
#var_message=tkinter.Message(app, text=" mon jeu est superbe")


  
var_label.pack()
var_entry.pack()
var_label1.pack()
var_entry1.pack()
var_label2.pack()


var_radio.pack()
var_radio1.pack()
var_scale.pack()

#var_check1.pack()
var_check.pack
#var_message.pack()
var_buton.pack()

liste.pack()
"""








# affichage de la fenetre a l infini
app.mainloop()