pris_årskort = int(input("Pris för årskort i hela ören: "))
pris_enkelbiljett = int(input("Pris för enkelbiljett i hela ören: "))
antal_enkelbiljetter = int(input("Antal enkelbiljetter som köps: "))

print("Det lönar sig att skaffa årskort" if pris_årskort < pris_enkelbiljett * antal_enkelbiljetter else "Det lönar sig inte att skaffa årskort")