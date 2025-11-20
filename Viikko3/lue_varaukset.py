"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin käyttäen funkitoita.
Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19,95 €
Kokonaishinta: 39,90 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""
from datetime import datetime


def main():
    tiedosto = "varaukset.txt"

    with open(tiedosto, "r", encoding="utf-8") as f:
        rivit = f.readlines()

    for rivi in rivit:
        varaus = rivi.strip().split('|')
        hae_varausnumero(varaus)
        hae_varaaja(varaus)
        hae_paiva(varaus)
        hae_aika(varaus)
        hae_tuntimaara(varaus)
        hae_tuntihinta(varaus)
        hae_kokonaishinta(varaus)
        hae_maksettu(varaus)
        hae_kohde(varaus)
        hae_puhelin(varaus)
        hae_sahkoposti(varaus)

def hae_varausnumero(varaus):
    numero = varaus[0]
    print(f"Varausnumero: {numero}")

def hae_varaaja(varaus):
    nimi = varaus[1]
    print(f"Varaaja: {nimi}")

def hae_paiva(varaus):
    paiva = datetime.strptime(varaus[2], "%Y-%m-%d").strftime("%d.%m.%Y")
    print(f"Päivämäärä: {paiva}")

def hae_aika(varaus):
    aika = varaus[3].replace(":", ".")
    print(f"Aloitusaika: {aika}")

def hae_tuntimaara(varaus):
    tuntimaara = varaus[4]
    print(f"Tuntimäärä: {tuntimaara}")

def hae_tuntihinta(varaus):
    tuntihinta = varaus[5]
    print(f"Tuntihinta: {tuntihinta} €")

def hae_kokonaishinta(varaus):
    tuntimaara = float(varaus[4])
    tuntihinta = float(varaus[5].replace(",", "."))
    kokonaishinta = tuntimaara * tuntihinta
    print(f"Kokonaishinta: {kokonaishinta:.2f} €")

def hae_maksettu(varaus):
    maksettu = varaus[6].lower() == "true"
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")

def hae_kohde(varaus):
    kohde = varaus[7]
    print(f"Kohde: {kohde}")

def hae_puhelin(varaus):
    puhelin = varaus[8]
    print(f"Puhelin: {puhelin}")

def hae_sahkoposti(varaus):
    sahkoposti = varaus[9]
    print(f"Sähköposti: {sahkoposti}")


        
if __name__ == "__main__":
    main()