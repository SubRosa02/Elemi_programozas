#festek
szoba = 75
vodor = 15
vodor_ara = 4300

festek_ara = int(((szoba*2)/vodor)*vodor_ara)
print(str(festek_ara) + " Ft értékben kell festéket vásárolnia.")

#festo
festo_ido = 13
festo_netto_oraber = 2100

netto_osszeg = int((szoba*2*festo_ido)/60)*festo_netto_oraber
print(str(netto_osszeg) + " Ft nettó összegért festi ki a szobát.")
afa = int(netto_osszeg*0.27)
print("A festőnek fizetett végösszeg: " + str(afa+netto_osszeg) + " Ft.")
print("A szobafestés összes kiadása: " + str(afa+netto_osszeg+festek_ara) + " Ft.")