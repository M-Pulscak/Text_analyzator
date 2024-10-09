"""
Text_analyzator.py: první projekt do Engeto "Datový analytik s Pythonem"
author: Michal Pulščák
email: pumi666@atlas.cz
discord: pumi_666
"""
TEXTS = ['''Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly
impressive topographic feature that rises sharply some 1000 feet above Twin Creek 
Valley to an elevation of more than 7500 feet above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, which traverse the valley. ''',
         '''At the base of Fossil Butte are the bright red, purple, yellow and gray beds 
of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually 
upward from the valley floor and steepen abruptly. Overlying them and extending to 
the top of the butte are the much steeper buff-to-white beds of the Green River 
Formation, which are about 300 feet thick.''',
         '''The monument contains 8198 acres and protects a portion of the largest 
deposit of freshwater fish fossils in the world. The richest fossil fish deposits are 
found in multiple limestone layers, which lie some 100 feet below the top of the butte. 
The fossils represent several varieties of perch, as well as other freshwater genera 
and herring similar to those in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

uziv = dict(bob="123", ann="pass123", mike="password123", liz="pass123")
odd = "-" * 50

# Kontrola přihlášení
jmeno = input("Vítej ;) \nZadej své přihlašovací jméno: ")
if jmeno in uziv:
    print("Ahoj", jmeno)
    heslo = input("Zadej svoje heslo: ")
    if heslo != uziv[jmeno]:
        print("Toto není tvoje heslo, konec programu."), exit()
else:
    print("Neregistrovaný uživatel, konec programu."), exit()
print(odd, "Přihlášení je v pořádku", "Vítej v aplikavci Text Analyzátor", odd,  sep="\n")

# Výběr a kontrola volby
volba = input("Který text chceš analyzovat? Vlož číslo 1-3: ")
if not volba.isdigit():
    print("Tvá volba nebylo číslo. Konec programu."), exit()
volba = int(volba) - 1
if volba not in range(0, 3):
    print("Tvé číslo není v nabídce. Konec programu."), exit()
print(odd)

# Příprava slov
slova = []
for s in TEXTS[volba].split():
    cs = s.strip(",.:;'")
    slova.append(cs)
                                                                    # proměnné pro výpočty výskytu:
pv, vv, vm, c, suma, n, graf = 0, 0, 0, 0, 0, 0, 0
pocty_pismen = []
pocet = len(slova)                                          # počet slov

for s in slova:                                                # projíždění slov:
    pocty_pismen.append(len(s))
    if s.istitle(): pv += 1                                 # prvni velké
    elif s.isupper(): vv += 1                            # všechny velké
    elif s.islower(): vm += 1                           # všechny malé
    elif s.isnumeric():
        c += 1                                                  # číselné
        suma += int(s)                                      # součet

print("Vybraný text obsahuje celkem", pocet, "slov.")               # Tisk
print("Velkým písmenem začíná", pv, "slov/a.")
print("Velkými písmeny je", vv, "slov/a.")
print("Malými písmeny je", vm, "slov/a.")
print("Text obsahuje ", c, "čísla.")
print("Součet všech čísel v textu je", suma)
print("Nejdelší slovo má", max(pocty_pismen), "znaků.")

# Grafika a četnosti slov
print(odd, "Četnost délek slov:", sep="\n")
print("Znaků |            Výskyt           | Počet slov", odd, sep="\n")

for i in range(1, max(pocty_pismen) + 1):           # počítadlo na písmena
    for _ in pocty_pismen:                          # projíždění délek slov
        n = pocty_pismen.count(i)
        graf = "x" * n
    sl = int(32-n/2)                                # počet mezer středního sloupce
    print(f" {i:^8}|{graf.ljust(sl)}|{n:>8}")
print(odd, "Konec výpisu. Program skončil.".center(45), odd, sep="\n")
