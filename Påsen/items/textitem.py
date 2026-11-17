from items.påsitem import Item

class TextItem(Item):
    def __init__(self):
        innehåll = input("Skriv in texten du vill spara: ")
        super().__init__("text", innehåll)

    def __str__(self):
        return f"ID: {self.id}, Typ: Text, Innehåll: {self.innehåll}"

    def open(self):
        print(f"Text: {self.innehåll}")