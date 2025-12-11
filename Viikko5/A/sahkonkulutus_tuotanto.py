
# Copyright (c) 2025 Jenni Sinisaari
# License: MIT

from datetime import datetime, date                                         # Tarvitaan datetime ja date tietotyyppejä varten


def muunna_tiedot(kulutus_tuotanto: list) -> list:                          
    """Muuntaa rivin tiedot oikeisiin tietotyyppeihin ja arvot Wh-kWh."""
    
    muutettu = []                                                           # Lista muunnetuista tiedoista
    
    
    aika = datetime.fromisoformat(kulutus_tuotanto[0])                      # Muunna aikaleima datetime-tyyppiseksi
    muutettu.append(aika) 
    
    
    for i in range(1, 7):                                                   # Muunna kulutus- ja tuotantoarvot Wh -> kWh
        arvo_kwh = int(kulutus_tuotanto[i]) / 1000                          # Muunna Wh kWh:ksi ja tietotyypiksi float
        muutettu.append(arvo_kwh)                                           # Lisää muunnettu arvo listaan
    return muutettu                                                         # Palauta muunnetut tiedot listana






def lue_data(tiedoston_nimi: str) -> list:    
    """Lukee tiedoston ja palauttaa rivit oikeissa tietotyypeissä."""
    
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
    Laskee yhden päivän kulutus- ja tuotantotiedot vaiheittain.
    
    Parametrit:
        paiva (date): Päivämäärä, jolta tiedot lasketaan.
        rivit (list): Lista rivejä, jokaisessa [datetime, kWh1, kWh2, kWh3, t1, t2, t3]
        
    Palauttaa:
        list: [päivämäärä merkkijonona, kulutus v1-v3, tuotanto v1-v3]
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




def main():   #pääohjelma
    
    
    """
     Pääohjelma lukee datan, laskee yhteenvedot ja tulostaa raportin.
    """
    rivit = lue_data("viikko42.csv")                   # Lue data tiedostosta
    viikonpaivat = [                                   # listaus viikonpäivistä
        "maanantai", "tiistai", "keskiviikko",
        "torstai", "perjantai", "lauantai", "sunnuntai"
    ]

    paivat = [               #listaus viikon päivämääristä
        date(2025, 10, 13),  # maanantai
        date(2025, 10, 14),  # tiistai
        date(2025, 10, 15),  # keskiviikko
        date(2025, 10, 16),  # torstai
        date(2025, 10, 17),  # perjantai
        date(2025, 10, 18),  # lauantai
        date(2025, 10, 19)   # sunnuntai
    ]

    print("Viikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)")                                    # Tulostetaan otsikko
    print()
    print("    Päivä           Pvm         Kulutus [kWh]        Tuotanto [kWh] ")                       # Tulostetaan sarakeotsikot
    print("                (pv.kk.vvvv)     v1     v2       v3      v1      v2      v3")               
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    for i in range(7):                                                                                   # Käydään läpi viikon päivät
        tiedot = paivan_tiedot(paivat[i], rivit)                                                         # Haetaan päivän tiedot
        print(f"{viikonpaivat[i]:<12}\t" + "\t".join(tiedot))                                            # Tulostetaan päivän tiedot muodossa, 12 merkkiä vasemmalle tasattuna

    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print()

     
     






if __name__ == "__main__":
    main()
