def secti(cislo1, cislo2):
    vysledek = cislo1 + cislo2
    return vysledek


print(f"Vysledek je {secti(4, 7)}")

vysledek_souctu_5_a_12 = secti(5, 12)

def uloz_do_souboru(text):
    with open("file.txt", "w") as f:
        f.write(text)

uloz_do_souboru(str(secti(1000, 1)))
