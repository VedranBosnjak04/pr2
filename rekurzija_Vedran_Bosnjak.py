"""Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada."""

def unazad(s):
    if s == "":
        return s
    else:
        return unazad(s[1:]) + s[0]

print(unazad("Onomatopeja"))
