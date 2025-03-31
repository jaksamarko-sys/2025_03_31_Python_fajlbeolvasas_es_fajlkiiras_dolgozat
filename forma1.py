"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""
forma1 = []

with open ('./beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = str(adatok[0])
        team = str(adatok[1])
        wins = int(adatok[2])
        runs = int(adatok[3])
        forma1.append([nev, team, wins, runs])

legtobb_futamgyozelemu_versenyzo = None
legtobb_futamgyozelem = 0
for versenyzok in forma1:
    if legtobb_futamgyozelem < versenyzok[2]:
        legtobb_futamgyozelem = versenyzok[2]
        legtobb_futamgyozelemu_versenyzo = versenyzok

legtobb_futam = None
legtobb_futamos = 0
for versenyzok in forma1:
    if legtobb_futamos < versenyzok[3]:
        legtobb_futamos = versenyzok[3]
        legtobb_futam = versenyzok


atlag = 0
for versenyzo in forma1:
    atlag += versenyzo[3]

with open('./kiirt_adatok/statisztika.txt', 'w', encoding='utf-8') as celfajl:
    print(f"A beolvasott fájlban összesen {len(forma1)} versenyző szerepel.", file=celfajl)
    print(f"A legtöbb futamot nyert versenyző: {legtobb_futamgyozelemu_versenyzo[2]}", file=celfajl)
    print(f"A legtöbb futamot teljesített versenyző: {legtobb_futam}", file=celfajl)
    print(f"Az átlagos futamszám: {atlag / len(forma1)}", file=celfajl)