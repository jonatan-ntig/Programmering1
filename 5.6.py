# Den katastofalt dåliga lösningen boken kräver
s = input("Skriv ett svenskt datum som YYYY-MM-DD: ")
år = s[2:4]
månad = s[5:7]
dag = s[8:10]

print(f"{månad}/{dag}/{år}")