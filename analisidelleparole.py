import re

from collections import Counter

#chiediamo all'utente di inserire una frase

frase_utente = input(" per favore inserisca una frase  ")

parole_da_cercare = input("quale parola vuoi contare?  ")

parole_nella_frase = re.findall(r'\b\w+\b', frase_utente.lower())

frequenza_parole = Counter(parole_nella_frase)

conteggio = frequenza_parole[parole_da_cercare.lower()]
 
print(f"la parola {parole_da_cercare} compare {conteggio} volta/e nella frase.  ")
