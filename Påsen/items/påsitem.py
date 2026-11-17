
import secrets
import string

class Item:
    def __init__(self, typ, innehåll):
        self.typ = typ
        self.id = ''.join(secrets.choice(string.ascii_lowercase + string.digits) for _ in range(3))
        self.innehåll = innehåll