def privitej_navstevnika(prijmeni, vek, cislo_OP=False):
    print(f"Dobrý den, pane {prijmeni}")
    print("Založte si naši průkazku.")
    print(f"Číslo občanky je {cislo_OP}")
    if vek < 15:
        print("Knihy pro děti jsou ve druhém patře.")
    else:
        print("Knihy pro dospělé jsou v prvním patře.")

privitej_navstevnika("Novák", 60, "AB123456")
privitej_navstevnika("Černý", 30, "XY456789")
privitej_navstevnika("Jedlička", 12, False)
privitej_navstevnika("Mrzout", 43)
