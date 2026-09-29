import re

s = input("Skriv en text: ")
match = re.search(r'\s', s)
if match:
    print(f"Första vita tecken finns på plats nr {match.start()+1}")
else:
    print("Det finns inga vita tecken i texten")