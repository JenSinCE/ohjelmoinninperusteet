# Copyright (c) 2025 Jenni Sinisaari
# License: MIT

from datetime import datetime, date, timedelta                              # Tuodaan datetime, date ja timedelta moduulit   

def muunna_tiedot(kulutus_tuotanto: list) -> list:                          
    """muuntaa rivin tiedot oikeisiin tietotyyppeihin ja arvot Wh-kWh."""
    
    muutettu = []                                                           # Lista muunnetuista tiedoista
    
    
    aika = datetime.fromisoformat(kulutus_tuotanto[0])                      # Muunna aikaleima datetime-tyyppiseksi
    muutettu.append(aika) 
    
    
    for i in range(1, 7):                                                   # Muunna kulutus- ja tuotantoarvot Wh -> kWh
        arvo_kwh = int(kulutus_tuotanto[i]) / 1000                          # Muunna Wh kWh:ksi ja tietotyypiksi float
        muutettu.append(arvo_kwh)                                           # Lisää muunnettu arvo listaan
    return muutettu                                                         # Palauta muunnetut tiedot listana






def lue_data(tiedoston_nimi: str) -> list:    
    """lukee tiedoston ja palauttaa rivit oikeissa tietotyypeissä."""
    
    rivit = []                                                               # Lista kaikista riveistä muunnetuissa tietotyypeissä
    
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:                   # Avaa tiedosto lukemista varten
        next(f)  # ohitetaan otsikkorivi   
        
        for rivi in f:                                                       # Käy läpi tiedoston jokainen rivi
            rivi = rivi.strip()                                              # Poista rivin alusta ja lopusta ylimääräiset välilyönnit ja rivinvaihdot
            sarakkeet = rivi.split(";")                                      # Jaa rivi sarakkeisiin puolipisteen kohdalta
            
            muunnettu = muunna_tiedot(sarakkeet)                             # Muunna sarakkeet oikeisiin tietotyyppeihin
            rivit.append(muunnettu)                                          # Lisää muunnettu rivi listaan
    
    return rivit                                                             # Palauta kaikki rivit listana






def paivan_tiedot(paiva: date, rivit: list) -> list:
    """
    laskee yhden päivän kulutus- ja tuotantotiedot vaiheittain.
    
    Parametrit:
        paiva (date) = päivämäärä, jolta tiedot lasketaan.
        rivit (list) =lista rivejä, jokaisessa datetime on kWh1, kWh2, kWh3, t1, t2, t3
        
    Palauttaa:
        päivämäärä merkkijonona, kulutus v1-v3, tuotanto v1-v3
    """
    kulutus = [0.0, 0.0, 0.0]                                       # Lista kulutukselle vaiheittain
    tuotanto = [0.0, 0.0, 0.0]                                      # Lista tuotannolle vaiheittain 

    for rivi in rivit:                                              # Käy läpi kaikki rivit
        if rivi[0].date() == paiva:                                 # Jos rivin päivämäärä vastaa haluttua päivää
            for i in range(3):                                      # Käy läpi vaiheet 0, 1, 2
                kulutus[i] += rivi[1 + i]                           # lasketaan kulutus lisäten arvot vaiheittain
                tuotanto[i] += rivi[4 + i]                          # lasketaan tuotanto lisäten arvot vaiheittain

    # Muodostetaan tulostukseen sopivat merkkijonot
    return [                                                       # Palauttaa listan merkkijonoina
        f"{paiva.day}.{paiva.month}.{paiva.year}",                 # Päivämäärä merkkijonona
        f"{kulutus[0]:.2f}".replace(".", ","),                     #pistettä vaihdetaan pilkuksi
        f"{kulutus[1]:.2f}".replace(".", ","),
        f"{kulutus[2]:.2f}".replace(".", ","),
        f"{tuotanto[0]:.2f}".replace(".", ","),
        f"{tuotanto[1]:.2f}".replace(".", ","),
        f"{tuotanto[2]:.2f}".replace(".", ","),
    
    ]

def viikkoraportti(viikkonumero: int, aloituspv: datetime.date, rivit: list) -> str:              
    """
    Laskee viikkoraportin annettuihin viikonpäiviin ja

    Parametrit:
     viikkonumero (int): Raportoivan viikon numero
     aloituspv (datetime.date): Viikon ensimmäinen päivämäärä
     tietokanta (list): Kulutus- ja tuotantotiedot + päivämäärät

    Palautus:
     raportti (Str): Raportti tekstinä
    """
 
    viikonpaivat = [                                                                                          # listaus viikonpäivistä
        "maanantai", "tiistai\t", "keskiviikko",
        "torstai\t", "perjantai", "lauantai", "sunnuntai"
    ]

    raportti = f"\nVIIKON {viikkonumero} SÄHKÖNKULUTUS JA -TUOTANTO💡⚡ (kWh, vaiheittain)\n\n"              
    raportti += "Viikonpäivä\tPäivämäärä\tKulutus [kWh]\t\tTuotanto [kWh]\n"
    raportti += "\t\t\t\t\t\t v1\t\t v2\t\t v3\t\t v1\t\t v2\t\t v3\n"
    raportti += "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
    for i, paiva in enumerate(viikonpaivat):                                                                 # Käy läpi viikonpäivät
        raportti += paiva + "\t" + "\t".join(paivan_tiedot(aloituspv+timedelta(days=i), rivit)) + "\n"       # Lisää päivän tiedot raporttiin

    raportti += "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n" 
    return raportti                                                                                          # Palauta muodostettu raportti

def main():   #pääohjelma
    
    
    """
     pääohjelma lukee datan, laskee yhteenvedot ja tulostaa raportin + listaus viikon päivämääristä
    """
    kt41 = lue_data("viikko41.csv")                                                                           # Lista kaikista riveistä muunnetuissa tietotyypeissä
    kt42 = lue_data("viikko42.csv") 
    kt43 = lue_data("viikko43.csv")                  

    aloituspv = date(2025, 10, 6)  # maanantai                                                                # Viikon 41 aloituspäivä 

    raporttivko41 = viikkoraportti(41, aloituspv, kt41)                                                       # Viikon 41 raportti
    raporttivko42 = viikkoraportti(42, aloituspv + timedelta(weeks=1), kt42)                                  # Viikon 42 raportti
    raporttivko43 = viikkoraportti(43, aloituspv + timedelta(weeks=2), kt43)                                  # Viikon 43 raportti          

    with open("yhteenveto.txt", "w", encoding="utf-8") as f:                                                  # avaa tiedosto kirjoittamista varten
        f.write(raporttivko41)                                                                                # kirjoita viikon 41 raportti tiedostoon
        f.write(raporttivko42)                                                                                # kirjoita viikon 42 raportti tiedostoon
        f.write(raporttivko43)                                                                                # kirjoita viikon 43 raportti tiedostoon

    print("RAPORTTI LUOTU 📋🗂️") 


if __name__ == "__main__":
    main()
    
