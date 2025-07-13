#obbiettivo del programma dove l'utente inserirà una frase e il
#programma dovrà effettuare una analisi grammaticale
import spacy 
try:
    nlp = spacy.load("it_core_news_sm")
except OSError:
    print("Errore: Il modello linguistico 'it_core_news_sm' non è stato trovato.")
    print("Assicurati di averlo scaricato con: python -m spacy download it_core_news_sm")
    exit() # Esce dal programma se il modello non c'è


frase_utente = input("Per favore inserisci una frase:  ")
doc = nlp(frase_utente)
print("\n---ANALISI GRAMMATICALE---")
print("{:<15}{:<15}{:<15}".format("verbo","aggettivo ","articolo"))

for token in doc:

    print("{:<15}{:<15}{:<15}".format(token.noun, token.adj, token.adp))
print("\n---FINE ANALISI---")


