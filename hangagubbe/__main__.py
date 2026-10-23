
import random
from graphics import STAGES

gissningar: list[str] = []

val = input("Vill du välja ett ord själv? (j/n): ")

if val == "j":
    ord = input("Skriv in ett ord: ").lower()
    print("\033[H\033[J", end="")
else:
    with open("wordlist.txt", "r") as f:
        lines = f.readlines()
        ord = lines[random.randint(0, len(lines) - 1)].strip()

val = input("Hur vill du dö? (1) Hängas (2) Halshuggas: ")

state = [c if not c.isalpha() else "_" for c in ord]

liv=startliv=10

try: 
    while liv > 0:
        print("\033[H\033[J", end="")

        print(f"Gissat: {', '.join(gissningar)}" if gissningar else "")

        print("♥ "* liv + "♡ " * (startliv - liv))

        print(STAGES[int(val) - 1][startliv - liv])

        print(" ".join(state))

        gissning = input("Gissa: ")

        if gissning.lower() == ord.lower():
            break
        if gissning in gissningar or not gissning.isalpha():
            continue

        for i in range(len(ord)):
            if ord[i].lower() == gissning.lower():
                state[i] = ord[i]

        if "_" not in state:
            break
        if gissning.lower() not in ord.lower():
            liv -= 1
            gissningar.append(gissning.lower())

        if liv == 0:
            print("\033[H\033[J", end="")
            print(f"Du dog. Ordet var {ord}.")
except KeyboardInterrupt:
    print(f"\nDu avbröt spelet. Ordet var {ord}.")
    exit(0)
if liv > 0:
    print(f"Du vann! Ordet var {ord}.")
