import math

#ho importato la libreria per i calcoli matematici

  
def perimetro(): 
    #ho definito la funzione principale per calcolare il perimetro

    print("\ncalcolatore di perimetri")
    print("1) quadrato")
    print("2) cerchio")
    print("3) rettangolo") #ho inserito le varie opsioni
  
try:    
    scelta = int(input("seleziona una figura: ")) # chiedo all'utente di scegliere la figura
except ValueError:
    print("nope! inserisci un numero valido!")   #se scrive un numero che non c'è da errore

 #   qui definiamo le condizioni con cui il programma eseguira il calcolo
if scelta == 1:
    print(" hai scelto il quadrato")
    lato = float(input("inserisci la lunghezza del lato:  "))
    risultato = 4*lato
    print(f"il risultato del perimetro del quadrato è: {risultato} " )
    
    
elif scelta == 2:
    print(" hai scelto il cerchio")
    raggio = float(input("per favore, inserisci il raggio:  "))
    risultato = 2*math.pi*raggio
    print(f"la circonferenza è:  {risultato}")


elif scelta == 3:
     print("hai scelto il rettangolo")
     base = float(input("ora per favore inserisci il lato del rettangolo:  "))
     altezza = float(input(" inserisci l'altezza:  "))
     risultato = base*2+altezza*2
     print(f"il perimetro del rettangolo è: {risultato}")
    

else:
   print(" scelta non valida, mi spiace riprova!") 






    