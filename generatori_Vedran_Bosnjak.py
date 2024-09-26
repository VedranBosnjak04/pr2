"""Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra."""

n = int(input("Unesi broj: "))
def parni(n):
    for i in range(0,n):
        if i % 2 == 0:
            yield i

iter_parni = iter(parni(n))
print("Parni brojevi manji od", n)
while True:
    try:
        print(next(iter_parni))
    except StopIteration:
        break
    
def neparni(n):
    for j in range(0,n):
        if j % 2 != 0:
            yield j

iter_neparni = iter(neparni(n))
print("Neparni brojevi manji od",n)
while True:
    try:
        print(next(iter_neparni))
    except StopIteration:
        break
