def vytiskni(veta1, veta2, *args, konec="", **kwargs):
    print(veta1)
    print(kwargs["opice"])



vytiskni("abc", "def", "ghi", "jkl", konec="prasatko", slon="Jumbo", opice="Agáta")