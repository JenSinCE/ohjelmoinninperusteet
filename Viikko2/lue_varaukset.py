"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
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
        varausnumero = varaus[0]
        varaaja = varaus[1]
        paiva = varaus[2]
        aika = varaus[3]
        tuntimaara = varaus[4]
        tuntihinta = float(varaus[5].replace(",", "."))
        kokonaishinta = float(tuntimaara) * tuntihinta
        maksettu = varaus[6]
        kohde = varaus[7]
        puhelin = varaus[8]
        sahkoposti = varaus[9]

        print(f"Varausnumero: {varausnumero}")
        print(f"Varaaja: {varaaja}")
        print(f"Päivämäärä: {paiva}")
        print(f"Aloitusaika: {aika}")
        print(f"Tuntimäärä: {tuntimaara}")
        print(f"Tuntihinta: {tuntihinta} €")
        print(f"Kokonaishinta: {kokonaishinta} €")
        print(f"Maksettu: {maksettu}")
        print(f"Kohde: {kohde}")
        print(f"Puhelin: {puhelin}")
        print(f"Sähköposti: {sahkoposti}")


if __name__ == "__main__":
    main()