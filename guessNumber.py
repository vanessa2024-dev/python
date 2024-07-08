#coding:utf-8
import random
import tkinter
import time
from datetime import datetime


    

debut=time.time()

def verification():
    verificateur=True
    
    while verificateur:
        try:
            username=input(" veuillez entrer un nombre compris entre 1 et 100 ")
            username=int(username)
            
            assert username>0
            break
        except AssertionError:
            print("\t ce nombre est negtif et ne sera pas pris en compte")
            continue
        except ValueError:
            print("\t entrer un nombre et non des lettres")
            continue
    return username


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

    
print(datetime.today())
#print(time.strftime("%d/%m/%Y"))

print(GuessNumber())
end = time.time()
print(f" vous avez passer {end-debut} secondes sur le jeu the Guessing Number")


