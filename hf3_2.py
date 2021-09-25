termek_ara = int(input("Adja meg a termék árát: "))
if termek_ara < 10000:
    print("Kedvezmény: ", termek_ara*0.1, "Ft. A kedvezményes ár: ",termek_ara-(termek_ara*0.1), "Ft.")
else:
    print("Kedvezmény: ", termek_ara*0.2, "Ft. A kedvezményes ár: ",termek_ara-(termek_ara*0.2), "Ft.")