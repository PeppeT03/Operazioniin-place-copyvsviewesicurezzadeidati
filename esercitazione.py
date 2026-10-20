import pandas as pd
import numpy as np

dati = {
    "Prodotto" : ["Spatola","Mutanda","Ps5","Cuffie","Asciugapalle"],
    "Prezzo" : [10.0,1000.0,500.0,49.0,51.0]
}

print(dati)

df = pd.DataFrame(dati)

print(df)

prodotti_filtrati = df["Prezzo"]>50
print(df.loc[prodotti_filtrati])

prodotti_selezionati = df.loc[prodotti_filtrati].copy()

print(prodotti_selezionati)

prodotti_selezionati["Costoso"]= prodotti_selezionati["Prezzo"] > 100

print(prodotti_selezionati)

prodotti_selezionati.sort_values(by="Prezzo",ascending=False,inplace=True)

print(prodotti_selezionati)

# Esercizio 2 - Gestione dei libri

dati_libri = {
    "Titolo": [
        "Il piccolo principe",
        "1984",
        "Il Signore degli Anelli",
        "Dune",
        "Harry Potter"
    ],
    "Autore": [
        "Antoine de Saint-Exupéry",
        "George Orwell",
        "J.R.R. Tolkien",
        "Frank Herbert",
        "J.K. Rowling"
    ],
    "Pagine": [120, 328, 560, 412, 250],
    "Prezzo": [12.50, 15.00, 32.90, 24.50, 18.00]
}

df_libri = pd.DataFrame(dati_libri)

print(df_libri)

filtrolibri = df_libri["Pagine"] > 300
copialibri = df_libri.loc[filtrolibri].copy()

print(copialibri)

copialibri["Lungo"] = copialibri["Pagine"] > 400
copialibri.sort_values(by="Prezzo",ascending=True,inplace=True)
print(copialibri)

dati_clienti = {
    "Nome": ["Anna", "Luca", "Marco", "Sara", "Giulia"],
    "Citta": ["Napoli", "Roma", "Milano", "Napoli", "Torino"],
    "Spesa": [800, 1200, 2000, 1500, 950]
}

df_clienti = pd.DataFrame(dati_clienti)
print(df_clienti)

filtroclienti = df_clienti["Spesa"] > 1000
copiaclienti = df_clienti.loc[filtroclienti].copy()
copiaclienti["VIP"] = copiaclienti["Spesa"] > 1500
copiaclienti.sort_values(by="Spesa",ascending=False,inplace=True,ignore_index=True)
print(copiaclienti)