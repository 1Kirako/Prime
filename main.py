import random

# Nadanie cen skinów

q = 15
w = 16
e = 9
r = 10
t = 59
y = 78
u = 91
g = 100
o = 122
p = 478
a = 583
s = 758
d = 636
f = 3008

# Utworzenie listy skinów

lista_skinow = []

# Nadanie częstości pojawiania sie skinów

qq = 186
qw = 164
qe = 615
qr = 198
qt = 45
qy = 46
qu = 40
qg = 45
qo = 73
qp = 17
qa = 13
qs = 17
qd = 15
qf = 25

# Dodanie skinów do listy

for i in range(qw):
    lista_skinow.append(w)
for i in range(qq):
    lista_skinow.append(q)
for i in range(qe):
    lista_skinow.append(e)
for i in range(qr):
    lista_skinow.append(r)
for i in range(qt):
    lista_skinow.append(t)
for i in range(qy):
    lista_skinow.append(y)
for i in range(qu):
    lista_skinow.append(qu)
for i in range(qg):
    lista_skinow.append(g)
for i in range(qo):
    lista_skinow.append(o)
for i in range(qp):
    lista_skinow.append(p)
for i in range(qa):
    lista_skinow.append(a)
for i in range(qs):
    lista_skinow.append(s)
for i in range(qd):
    lista_skinow.append(d)
for i in range(qf):
    lista_skinow.append(f)

# Nadanie kilku wartości

suma_wynikow = 0
wartosciowszy_skin = 0
liczba_wynikow = 100000

# Wylosowanie liczby skina

for i in range(0, liczba_wynikow):
    r1 = random.randint(0, 1498)
    r2 = random.randint(0, 1498)


# Nadanie skinowi wartości

    skin1 = lista_skinow[r1]
    skin2 = lista_skinow[r2]

# Decydowanie, który skin jest wartościowszy

    if skin1 >= skin2:
        wartosciowszy_skin = skin1
    else:
        wartosciowszy_skin = skin2

# Obliczenie sumy do średniej

    suma_wynikow = suma_wynikow + wartosciowszy_skin

# Obliczenie efektywnej średniej wartości skina

srednia = suma_wynikow / liczba_wynikow
print(srednia)
