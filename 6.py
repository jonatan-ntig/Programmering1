import bcrypt

correct = "$2b$12$yc736XKBsEs.pGCvQuJsS..6cTFi.0deGn0o5YnfzPuQhBmClKTte"
password = input("Vad har du för lösenord? ")

print("Välkommen" if bcrypt.checkpw(password.encode("utf-8"), correct.encode("utf-8")) else "Fel lösenord!")
