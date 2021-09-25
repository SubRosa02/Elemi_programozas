#elso
eletkor = int(input("Adja meg az életkorát: "))
nem = input("Adja meg a nemét, fiú(m) / lány(f): ")
if eletkor >= 10 and eletkor <=12:
    if nem == "f":
        print("Játszhat.")
    else:
        print("Nem játszhat.")
else:
    print("Nem játszhat.")

#masodik
n = input("Adja meg a nemét, fiú(m) / lány(f): ")
if n == "f":
    e = int(input("Adja meg az életkorát: "))
    if e >= 10 and e <=12:
        print("Játszhat")
    else:
        print("Nem játszhat.")
else:
    print("Nem játszhat.")
