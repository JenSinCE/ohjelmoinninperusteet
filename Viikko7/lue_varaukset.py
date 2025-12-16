
"""
Tässä ohjelmassa varaukset tallennetaan sanakirjoina (dict).
Sanakirjat ovat selkeämpiä kuin listat, koska kenttiin viitataan
loogisilla avaimilla (esim. 'nimi', 'vahvistettu') indeksien sijaan.
Tämä parantaa koodin luettavuutta ja ylläpidettävyyttä.
"""


from datetime import datetime

def muunna_varaustiedot(varaus: list[str]) -> dict:
    return {
        "id": int(varaus[0]),
        "nimi": varaus[1],
        "sahkoposti": varaus[2],
        "puhelin": varaus[3],
        "paiva": datetime.strptime(varaus[4], "%Y-%m-%d").date(),
        "kellonaika": datetime.strptime(varaus[5], "%H:%M").time(),
        "kesto": int(varaus[6]),
        "hinta": float(varaus[7]),
        "vahvistettu": varaus[8].lower() == "true",
        "kohde": varaus[9],
        "luotu": datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S"),
    }


def hae_varaukset(varaustiedosto: str) -> list[dict]:
    varaukset = []

    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for rivi in f:
            rivi = rivi.strip()
            varaustiedot = rivi.split("|")
            varaukset.append(muunna_varaustiedot(varaustiedot))

    return varaukset


def vahvistetut_varaukset(varaukset: list[dict]):
    for varaus in varaukset:
        if varaus["vahvistettu"]:
            print(f"- {varaus['nimi']}, {varaus['kohde']}, {varaus['paiva'].strftime('%d.%m.%Y')} klo {varaus['kellonaika'].strftime('%H.%M')}")

    print()

def pitkat_varaukset(varaukset: list[dict]):
    for varaus in varaukset:
        if varaus["kesto"] >= 3:
            print(f"- {varaus['nimi']}, {varaus['paiva'].strftime('%d.%m.%Y')} klo {varaus['kellonaika'].strftime('%H.%M')}, kesto {varaus['kesto']} h, {varaus['kohde']}")

    print()

def varausten_vahvistusstatus(varaukset: list[dict]):
    for varaus in varaukset:
        if varaus["vahvistettu"]:
            print(f"{varaus['nimi']} → Vahvistettu")
        else:
            print(f"{varaus['nimi']} → EI vahvistettu")

    print()

def varausten_lkm(varaukset: list[dict]):
    vahvistetutVaraukset = 0
    eiVahvistetutVaraukset = 0
    for varaus in varaukset:
        if varaus["vahvistettu"]:
            vahvistetutVaraukset += 1
        else:
            eiVahvistetutVaraukset += 1

    print(f"- Vahvistettuja varauksia: {vahvistetutVaraukset} kpl")
    print(f"- Ei-vahvistettuja varauksia: {eiVahvistetutVaraukset} kpl")
    print()

def varausten_kokonaistulot(varaukset: list[dict]):
    varaustenTulot = 0
    for varaus in varaukset:
        if varaus["vahvistettu"]:
            varaustenTulot += varaus["kesto"]*varaus["hinta"]
    print("Vahvistettujen varausten kokonaistulot:", f"{varaustenTulot:.2f}".replace('.', ','), "€")
    print()

def main():
    
    varaukset = hae_varaukset("varaukset.txt")

    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)

    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)

    print("3) Varausten vahvistusstatus")
    varausten_vahvistusstatus(varaukset)

    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)

    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)


if __name__ == "__main__":
    main()