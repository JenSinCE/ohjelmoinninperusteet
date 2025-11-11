def main():
    tiedosto = "sana.txt"
    
    try:
        with open(tiedosto, "r", encoding="utf-8") as f:
            sana = f.read().strip()
        print(sana)

        if not sana:
            print("Virhe: Tiedosto on tyhjä.")
            return
        
        print(sana)

    except FileNotFoundError:
        print(f"Virhe: Tiedostoa '{tiedosto}' ei löydy.")
    except PermissionError:
        print(f"Virhe: tiedostoon '{tiedosto}' ei ole lukuoikeutta.")
    except Exception as e:
        print(f"Tuntematon virhe: {e}")
if __name__ == "__main__":
    main()
        