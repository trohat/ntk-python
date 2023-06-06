menu = {
    "polevka": 20,
    "salat": 30,
    "řízek": 80,
    "kachna": 100,
    "losos": 50,
    "zákusek": 25
}

# B
menu["kuře"] = 60
menu["hranolky"] = 30

# C
menu["kachna"] = 120

# D
del menu["zákusek"]

# 2
def vypis_jidel():
    for jidlo in menu.keys():
        print(jidlo)

vypis_jidel()

def vypis_jidel_i_s_cenami(menu):
    for jidlo, cena in menu.items():
        print(f"Nabízíme {jidlo} za {cena} Kč.")

vypis_jidel_i_s_cenami(menu)

def objednavka(menu):
    celkova_cena = 0
    while True:
        jidlo = input("Zadej na co máš chuť, když nic nezadáš, funkce skončí. ")
        if jidlo == "":
            break
        if jidlo in menu:
            cena = menu[jidlo]
            celkova_cena += cena
            print(f"Objednal sis {jidlo} za {cena} korun.")
        else:
            print("Tohle jídlo bohužel nemáme, zkus to znovu.")
    return celkova_cena


print(f"Najedl ses za {objednavka(menu)} korun.")
