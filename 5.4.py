s = input("Skriv en text: ")
for i, c in enumerate(s):
    if (c == " " or c == "\t"):
        print(f"Första vita tecken finns på plats nr {i+1}")
        exit(0)

print("Det finns inga vita tecken i texten")