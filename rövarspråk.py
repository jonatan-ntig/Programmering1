import re
konsonanter=r'([bcdfghjklmnpqrstvwxz])'
rövarspråk=r'([bcdfghjklmnpqrstvwxz])o([bcdfghjklmnpqrstvwxz])'

def sv_to_rövarspråk(string: str):
    return re.sub(konsonanter, r'\1o\1', string, flags=re.IGNORECASE)

def rövarspråk_to_sv(string: str):
    return re.sub(rövarspråk, r'\1', string, flags=re.IGNORECASE)

def översätt(string: str):
    if re.fullmatch(r'(?:([bcdfghjklmnpqrstvwxz])o\1|[aouåeiyäö])*', string, flags=re.IGNORECASE):
        return rövarspråk_to_sv(string)
    else:
        return sv_to_rövarspråk(string)

print(översätt(input("Skriv in texten du vill översätta: ")))