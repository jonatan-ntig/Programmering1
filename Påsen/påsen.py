from items.bilditem import BildItem
from items.doomitem import DoomItem
from items.ljuditem import LjudItem
from items.textitem import TextItem
påsen = []

while True:
    val = input("""Vad vill du göra?
        [V] Visa innehållet i påsen
        [S] Spara i påsen
        [F] Hitta i påsen
        [Q] Avsluta
""").lower()
    
    match val:
        case "s":
            item = input("Vad vill du spara i påsen? (text, ljud, bild, doom): ")
            match item:
                case "text":
                    påsen.append(TextItem())
                case "ljud":
                    påsen.append(LjudItem())
                case "bild":
                    påsen.append(BildItem())
                case "doom":
                    påsen.append(DoomItem())
                case _:
                    print("Ogiltigt val. Försök igen.")
        case "v":
            if påsen:
                for item in påsen:
                    print(item)
            else:
                print("Påsen är tom.")
        case "f":
            search_id = input("Ange ID för att hitta i påsen: ")
            found_items = [item for item in påsen if item.id == search_id]
            if len(found_items) != 1:
                print("Det måste finnas exakt ett objekt med det ID:t i påsen.")
            else:
                item = found_items[0]
                item.open()
        case "q":
            print("Avslutar programmet.")
            break