#coding:utf-8
import random
import tkinter
 


def verification():
    verificateur=True
    
    while verificateur:
        try:
            userChoice=input("veuillez choisir un nombre entre 1 et 100  ")
            userChoice=int(userChoice)
            assert userChoice>0
            break
        except AssertionError:
            print("\t ce nombre est negtif et ne sera pas pris en compte")
            continue
        except ValueError:
            print("\t entrer un nombre et non des lettres")
            continue
    return userChoice

    

def GuessNumber():


    random_number=random.randint(1,100)
    verificateur=True
    curseur=0

    
    while verificateur:
        valeurVerifie=verification()
        curseur+=1
        if valeurVerifie<random_number:
            print("le nombre aleatoire est plus grand que : ",valeurVerifie)
            

        elif valeurVerifie>random_number:
            print("le nombre aleatoire est plus petit que : ", valeurVerifie)
        
        else:
            print("bravo *********** vous avez trouvee le nombre aleatoie apres: ",curseur, "tentatives")
            verificateur=False

def bonjour():
    print("ecrire bonjour sur le terminal")


#print(GuessNumber())
mainapp=tkinter.Tk()# constructeur du module tkinter

 # avec tkinter tout un widget mainapp

#mainapp.quit() # permet de quitter la fenetre
mainapp.title("Guessing Number") # le titre de l fenetre
# creaction de label
# < non_variable> =<nom_widgget> (<widget_parent>, text=valeur)


label_welcome=tkinter.Label(mainapp, text="bienvenue sur le jeu du Guessing Number") # affiche le texte sur une seule ligne

message_welcome=tkinter.Message(mainapp, text= "je suis un tres long message qui tiendra sur plusieus ligne")

#entry_name = tkinter.Entry(mainapp, width=45, show="**", exportselection=0) # ecriture ds un widget

button_quit=tkinter.Button (mainapp,text="ok" ,command= bonjour()) 


#print(label_welcome["text"])

#print(label_welcome.cget("text"))
button_quit.pack()
#entry_name.pack()
label_welcome.pack() #  afficher le widget


 

















#mainapp.minsize(650,456) #taille min
#mainapp.maxsize(1280,720) # taille max
#mainapp.resizable(width=False ,height=True)  #interdit ou accepte un redimendionement
#mainapp.geometry( "800x600+15+100" )
mainapp.mainloop() # fonction qui fait une boucle pourque la fenetre reste ouverte jusqu a l utilateur quitte le programme
#mainapp.positionfrom("user")
#mainapp.sizefrom("user ")