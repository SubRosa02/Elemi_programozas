#megoldasok
p = "python"
print("A python szó első és utolsó karaktere: "+p[0]+p[5])

q = "hallgató"
r = "Hiába a hegynyi anyag, a hallgató gyorsan halad"
qinr = r.find(q)
print(r[qinr:qinr + len(q)])

s = "Elemi"
t = "programozás"
print(s + " " + t)


u = "péntek van"
print(7*u[0:6])

print(7*(u[0:6] + " "))

print(7*(u[0:6] + "\n"))

v = "Hiába a hegynyi anyag, a hallgató gyorsan halad"
print("hegy" in v)
print("tananyag" in v)
print("hegy" and "tananyag" in v)