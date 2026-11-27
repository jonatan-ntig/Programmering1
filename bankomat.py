def visa_meny():
    print("Vad vill du göra?")
    print("[1] sätta in pengar")
    print("[2] ta ut pengar")
    print("[3] visa saldo")
    print("[4] avsluta")

def sätta_in(saldo, belopp):
    saldo += belopp
    return saldo

def ta_ut(saldo, belopp):
    if saldo >= belopp:
        saldo -= belopp
    else:
        print("Du har inte tillräckligt med pengar på kontot.")
    return saldo

def visa_saldo(saldo):
    print(f"Ditt saldo är {saldo} kr.")
saldo = 0

while True:
    visa_meny()
    val = input("Välj ett alternativ: ")

    if val == "1":
        belopp = int(input("Ange belopp att sätta in: "))
        saldo = sätta_in(saldo, belopp)
    elif val == "2":
        belopp = int(input("Ange belopp att ta ut: "))
        saldo = ta_ut(saldo, belopp)
    elif val == "3":
        visa_saldo(saldo)
    elif val == "4":
        print("Tack för att du använde bankomaten!")
        break
