# -*- coding: utf-8 -*-
print "Pozdravljeni ! Welcome to -PRETVORNIK ENOT-( Kmh --> Mph )"

while True:
    kmh = int(raw_input("Vnesite število kilometrov v kmh: "))
    mph = float(1.6) * kmh
    print mph
    vprasanje = raw_input("Ali želite narediti novo pretvorbo ?")
    if vprasanje == "ne":
        print "End..."
        break

