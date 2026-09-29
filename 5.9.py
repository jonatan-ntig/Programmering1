text = input("Skriv in en text: ")
text = text.replace(" ", "")
print(f"Texten är {"" if text == text[::-1] else "inte "}en palindrom")