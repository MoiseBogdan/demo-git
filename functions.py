def cleanup(string):
    """Sterge spatiile de la inceput si de la sfarsit
    Transforma stringul in formatul prima litera mare, urmatoarele mici
    Returneaza stringul"""


    new_string = string.strip()
    new_string = new_string.capitalize()
    return new_string


print(cleanup("   text de transformat"))
print(cleanup("tesT"))
print(cleanup("  un  text "))
