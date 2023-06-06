zviratka = ["Alík", "Rex", "Jumbo", "Agáta", "Emilka"]
zviratka[2] = "Míša"
del zviratka[2]
zviratka.remove("Rex")
zviratka.append("Agáta")
zviratka.count("Agáta")
zviratka.insert(2, "Rex")
zviratka[-1]
zviratka[-5]
zviratka[2:5]
zviratka[2:]
zviratka[:5]
zviratka[2:5:2]

zvirata = ["opice", "kočka", "myš", "slon", "buvol", "surikata"]
zvirata.sort()

nova_zvirata = zvirata[:]
zvirata.sort(key=len) # těžké!!!