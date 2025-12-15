# Copyright (c) 2025 Jenni Sinisaari
# License: MIT

from datetime import datetime, date



def muunna_tiedot(rivi: list) -> list:
    """Muuntaa oikeisiin tietotyyppeihin laskentaa varten."""
    
    aika = datetime.fromisoformat(rivi[0])
    kulutus = float(rivi[1].replace(",", "."))  # pilkku -> piste floatille 
    tuotanto = float(rivi[2].replace(",", "."))
    lampotila = float(rivi[3].replace(",", "."))

    return [aika, kulutus, tuotanto, lampotila]



def lue_data(tiedoston_nimi: str) -> list:
    """Lukee tiedoston ja palauttaa listan muunnetuista riveistä."""
    
    rivit = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)  # ohitetaan otsikkorivi
        for rivi in f:
            rivi = rivi.strip()
            sarakkeet = rivi.split(";")
            muunnettu = muunna_tiedot(sarakkeet)
            rivit.append(muunnettu)
    return rivit



def paivaraportti(alku: date, loppu: date, rivit: list) -> list:                                              # Päiväraportti
    kulutus = 0.0                                                                                             # kokonaiskulutus
    tuotanto = 0.0                                                                                            # kokonaistuotanto
    lampotila = 0.0                                                                                           # lämpötilojen summa
                                                                                             

    for rivi in rivit:                                                                                        # käy läpi jokainen rivi
        paiva = rivi[0].date()                                                                                # ota rivin päivämäärä
        if alku <= paiva <= loppu:                                                                            # tarkista onko rivin päivä annettujen päivien välillä
            kulutus += rivi[1]                                                                                # laske kokonaiskulutus
            tuotanto += rivi[2]                                                                               # laske kokonaistuotanto
            lampotila += rivi[3]                                                                              # laske lämpötilojen summa                           

    raportti = [ 
        "HAETUN AIKAVÄLIN YHTEENVETO",
        f"Aikaväli: {alku.day}.{alku.month}.{alku.year} - {loppu.day}.{loppu.month}.{loppu.year}",
        f"Kokonaiskulutus: {kulutus:.2f}".replace(".", ",") + " kWh",
        f"Kokonaistuotanto: {tuotanto:.2f}".replace(".", ",") + " kWh",
        f"Keskilämpötila: {(lampotila/((loppu - alku).days*24)):.2f}".replace(".", ",") + " °C",               # keskilämpötila
        
    ]
    return raportti



def kuukausiraportti(kuukausi: int, rivit: list) -> list:                                                      # Kuukausiraportti
                                                      

    kulutus = 0.0                                                                                              # kokonaiskulutus
    tuotanto = 0.0                                                                                             # kokonaistuotanto
    lampotila = 0.0                                                                                            # lämpötilojen summa
    paivien_lukumaara = 0                                                                                      # päivien laskuri

    for rivi in rivit:                                                                                         # käy läpi jokainen rivi
        if rivi[0].month == kuukausi:                                                                          # tarkista onko rivin kuukausi sama kuin annettu kuukausi
            kulutus += rivi[1]                                                                                 # laske kokonaiskulutus
            tuotanto += rivi[2]                                                                                # laske kokonaistuotanto
            lampotila += rivi[3]                                                                               # laske lämpötilojen summa
            paivien_lukumaara += 1                                                                             # jokainen rivi = 1 päivä

    raportti = [  
        "KUUKAUDEN YHTEENVETO",
        f"Kuukausi: {kuukausi}",
        f"Kokonaiskulutus: {kulutus:.2f}".replace(".", ",") + " kWh",
        f"Kokonaistuotanto: {tuotanto:.2f}".replace(".", ",") + " kWh",
        f"Keskilämpötila: {(lampotila/(paivien_lukumaara*24)):.2f}".replace(".", ",") + " °C",
        
    ]
    return raportti



def vuosiraportti(rivit: list) -> list:                                                                         # Vuoden 2025 raportti
    kulutus = 0.0                                                                                               # kokonaiskulutus
    tuotanto = 0.0                                                                                              # kokonaistuotanto
    lampotila = 0.0                                                                                             # lämpötilojen summa
    paivien_lukumaara = 0                                                                                       # päivien laskuri                                                                                        

    for rivi in rivit:                                                                                          # Käy läpi jokainen rivi
        if rivi[0].year == 2025:                                                                                # Vain vuosi 2025
            kulutus += rivi[1]                                                                                  # Laske kokonaiskulutus
            tuotanto += rivi[2]                                                                                 # Laske kokonaistuotanto
            lampotila += rivi[3]                                                                                # Laske lämpötilojen summa
            paivien_lukumaara += 1                                                                              # jokainen rivi = 1 päivä                                                                      

                                      

    raportti = [
        "VUODEN YHTEENVETO",
        "Vuosi: 2025",
        f"Kokonaiskulutus: {kulutus:.2f}".replace(".", ",") + " kWh",
        f"Kokonaistuotanto: {tuotanto:.2f}".replace(".", ",") + " kWh",
        f"Keskilämpötila: {(lampotila/(paivien_lukumaara*24)):.2f}".replace(".", ",") + " °C",
        
    ]
    return raportti



def kirjoita_tiedostoon(raportti: list, tiedoston_nimi: str = "raportti.txt"):                                 # kirjoita raportti tiedostoon
    """Kirjoittaa raportin tiedostoon viivoilla ylä- ja alapuolella."""
    with open(tiedoston_nimi, "w", encoding="utf-8") as f:
         for rivi in raportti:                                                                                 # Käy läpi jokainen rivi raportissa
            f.write(rivi + "\n")                                                                               # Kirjoita jokainen rivi tiedostoon
        






def main():
    tiedot = lue_data("2025.csv")                                                                              # Lue data tiedostosta

    while True:                                                                                                # Pääohjelman silmukka
        print("----------------------------------------")
        print("Valitse raporttityyppi:")
        print()
        print("1) Valittujen päivien aikaväli")
        print("2) Kuukausi")
        print("3) Vuosi 2025")
        print("4) Lopeta")
        valinta = int(input("Valintasi: "))                                                                     # pyydä käyttäjältä valinta
        print("----------------------------------------")

        if valinta == 1:                                                                                        # Päiväraportti
            while True:                                                                                         # jatka kunnes saatu kelvollinen syöte
              try:                                                                                     
                  alku = datetime.strptime(input("Alkupäivä (pv.kk.vvvv): "), "%d.%m.%Y").date()                # pyydä alku- ja loppupäivä käyttäjältä
                  loppu = datetime.strptime(input("Loppupäivä (pv.kk.vvvv): "), "%d.%m.%Y").date()
                  if alku == loppu:                                                                             # tarkista että alku- ja loppupäivä eivät ole samat
                     print("-------------------------------------------------------------")
                     print("Alku- ja loppupäivä eivät voi olla samat, kokeile uudestaan.")
                     continue
                  raportti = paivaraportti(alku, loppu, tiedot)                                                  # Luo raportti
                  break                                                                                          # lopeta silmukka
              except ValueError:                                                                                 # jos syöte ei ole oikeassa muodossa
                 print("-----------------------------------------")
                 print("Päivämäärä on väärin, kokeile uudestaan.")
                    
                                                                  
        elif valinta == 2:                                                                                        # Kuukausiraportti  
            while True:                                                                                           # jatka kunnes saatu kelvollinen syöte
              try:                                                                                 
                  kuukausi = int(input("Kuukauden numero (1-12): "))                                              # pyydä kuukausi käyttäjältä
                  if 1 <= kuukausi <= 12:                                                                         # tarkista että kuukausi on välillä 1-12                     
                     raportti = kuukausiraportti(kuukausi, tiedot)                                                # Luo raportti
                     break                                                                                        # lopeta silmukka
                  else:                                                                                           # jos kuukausi ei ole välillä 1-12
                     print("----------------------------------------")
                     print("Numero pitää olla välillä 1-12.")

              except ValueError:                                                                                  # jos syöte ei ole kokonaisluku
                    print("----------------------------------------")
                    print("Virheellinen syöte, kokeile uudestaan.")
                    print("----------------------------------------")
                                                          
        elif valinta == 3:                                                                                        # Vuosiraportti
            raportti = vuosiraportti(tiedot)                                                                      # Luo raportti
            print("2025")                                                                                         # Tulosta vuosi
        elif valinta == 4:                                                                                        # Lopeta
            print("Ohjelma lopetettu.") 
            print("----------------------------------------")
            print()
            break                                                                                                 # Lopeta ohjelma
            
        else:
            print("Virheellinen valinta, valitse uudestaan.")                                                     # Virheellinen valinta, palaa päävalikkoon.
            continue

        
        print(raportti)                                                                                           # Tulosta raportti konsoliin
        

    
        print("----------------------------------------")                   
        print("Mitä haluat tehdä seuraavaksi?")                                                                # toinen valikko
        print()
        print("1) Kirjoita raportti tiedostoon raportti.txt")                                                  # valinnat 1-3
        print("2) Luo uusi raportti")
        print("3) Lopeta")
        valinta2 = int(input("Valintasi: "))                                                                   # Käyttäjän toinen valinta
        if valinta2 == 1:                                                                                      # Kirjoita raportti tiedostoon -valinta
            kirjoita_tiedostoon(raportti)                                                                      # Kirjoita raportti tiedostoon
            print("----------------------------------------")
            print("Raportti kirjoitettu raportti.txt")                                                         # Tulosta vahvistus            
        elif valinta2 == 2:                                                                                    # Uusi raportti -valinta
            print("--------------------------------------------------------")
            print("Palataan päävalikkoon ja tehdään uusi raportti.")                                           # Palataan päävalikkoon
            continue                                                                                           # Jatketaan pääsilmukassa
        elif valinta2 == 3:                                                                                    # Lopeta -valinta
            print("----------------------------------------")
            print("Ohjelma lopetettu.")                                                                        # Tulosta lopetusviesti
            print("----------------------------------------")
            break                                                                                              # Lopeta ohjelma
        else:
            print("--------------------------------------------")
            print("Virheellinen valinta, palataan päävalikkoon.")                                              # Virheellinen valinta, palaa päävalikkoon ilmoitus.
            
            continue                                                                                           # Jatketaan pääsilmukassa

        
        

if __name__ == "__main__":
    main()












 