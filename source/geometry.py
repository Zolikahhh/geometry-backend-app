"""
Szoftverfesztelési folyamatok példaprogram
SZTE TTIK, Informatikai Intézet, Szoftverfejlesztés Tanszék
cc-by-nc-nd
"""

import math

"""
A függvény feladata kiszámolni egy tehén által lelegelhető fű mennyiségét
köbméterben, ezredre kerekítve. A tehén egy l méter hosszúságú egyenes
sínhez van kikötve egy r méter hosszúságú kötéllel, ennek megfelelő
területen tud legelni. Az egész területen egységesen h centiméter magasra nő
a fű. A tehén csak az 5 cm-nél nagyobb füvet legeli le, de azt úgy, hogy
2 cm-t meghagy belőle. A fű "sűrűsége" 0.1%, azaz 1 köbméter térfogatban
0.001 köbméternyi fű van.
Negatív fűmagasság nincs, ilyenkor a függvény ValueError-t dob.

Ha például l = 10m, r = 5m és h = 20cm, akkor az eredmény 0.032 köbméter.
De ha a fű csak h = 4cm magas, akkor 0.000, mert a tehén nem nyúl hozzá.
"""
def volume(l, r, h):
    if h < 5:
        return 0.0
    return round(area(l, r) * h / 1000.0, 3)

"""
A függvény feladata kiszámolni egy tehén által lelegelhető területet
nagyságát négyzetméterben, ezredre kerekítve. A tehén úgy van kikötve, hogy
egy l méter hosszúságú egyenes sínhez rögzítjük az r méter hosszúságú kötél
egyik, és a tehénhez a másik végét. A kötél egyik vége a sínen elcsúszhat,
így a tehén a síntől legfeljebb r távolságra lévő bármely pontot le tudja
legelni.
Negatív sínhossz, vagy nem pozitív kötélhossz esetén a függvény egy
ValueError-t dob.

Ha például l = 10m, r = 5m, akkor az eredmény 178.540 négyzetméter.
Ha l = 0m, akkor a tehén egyetlen ponthoz van kikötve, és r = 5m kötéllel
78.540 négyzetmétert legel le.
De ha l negatív, vagy r nem pozitív, akkor ValuError-t kell kapnunk.
"""
def area(l, r):
    return round(area_c(r) + area_r(l, r), 3)

"""
A függvény feladata kiszámolni egy r sugarú kör területét (r²π), ezredre
kerekítve.
Ha a sugár nem pozitív, a függvény egy ValueError-t kell, hogy dobjon.
"""
def area_c(r):
    t = r * r * math.pi
    if t <= 0:
        raise ValueError()
    return round(t, 3)

"""
A függvény feladata kiszámolni egy a és b oldalú téglalap területét (a*b),
ezredre kerekítve.
Negatív oldalhossz esetén a függvény egy ValueError-t kell, hogy dobjon.
"""
def area_r(a, b):
    t = a * b
    if t <= 0:
        raise ValueError()
    return round(t, 3)
