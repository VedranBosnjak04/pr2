"""Definirati dvije funkcije koje kao parametar primaju ime ali vraćaju različitu poruku dobrodošlice.
Jedna neka ispisuje “Pozdrav {ime}!”, a druga “Dobrodošao {ime}!”
Jedna od funkcija neka bude definirana lambda izrazom, a druga standardnim načinom.
Zatim definiraj treću funkciju koja kao parametar prima naziv funkcije za ispis dobrodošlice i poziva je tako
što pošalje vaše ime u nju.
Pozvati treću funkciju prosljeđujući joj neku od prve dvije definirane funkcije."""

ime = input("Unesi ime: ")

def pozdrav(ime):
    return f"Pozdrav {ime}!"

print(pozdrav(ime))

dobrodosao = lambda ime: f"Dobrodošao {ime}!"

def ispis_dobrodoslice(f, ime):
    print(f(ime))

print(ispis_dobrodoslice(dobrodosao,ime))
print(ispis_dobrodoslice(pozdrav, ime))
