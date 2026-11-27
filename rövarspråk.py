import re

def sv_to_rövarspråk(string: str):
    konsonanter=r'([bcdfghjklmnpqrstvwxz])'
    rövarspråk=r'\1o\1'
    return re.sub(konsonanter, rövarspråk, string)

def rövarspråk_to_sv(string: str):
    rövarspråk=r'([bcdfghjklmnpqrstvwxz])o([bcdfghjklmnpqrstvwxz])'
    return re.sub(rövarspråk, r'\1', string, flags=re.IGNORECASE)

print(rövarspråk_to_sv("Jojagog totalolaror rorövovarorsospoproråkoketot"))

