import time
import threading  # gestion de la programmation asynchrome

var_lock=threading.RLock() # cree un verrou

class threads(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
    

    def run( self  ):
        i=0
        while i<3:
            liste=["sport"," lecture"," meditation","yoga","dormir"," musique"]
        
            with var_lock:
                for lecture in liste:
                    print(lecture)
                    time.sleep(0.5)
            i+=1



th1=threads()
th2=threads()



th1.start()
th2.start()

th1.join()
th2.join()

print("fin du programme")

