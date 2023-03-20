melysegek=[]

with open("melyseg.txt","r",encoding="utf-8") as fin:
    fin.readline()
    fin.readline()
    for sor in fin:
        seged_lista=list(map(int,sor.strip().split()))
        print(seged_lista)
        melysegek.append(seged_lista)

# print(melysegek)

from colorama import Fore,Back

for melyseg_sor in melysegek:
    for melyseg in melyseg_sor:
        if melyseg>0:
            print(f"{Back.BLUE}{Fore.WHITE}{melyseg:2d}", end=" ")
        else:
            print(f"{Back.RESET}{melyseg:2d}", end=" ")
    print()


#tört x=3.1415  print(f"{x:0.2f}")
#egész f=1  print(f"{f:2d}")

print("2. feladat")
be_sor=int(input("A mérés sorának azonosítója= ") or "12")
be_oszlop=int(input("A mérés oszlopának azonosítója= ") or "6")
print(f"A mért mélység az adott helyen {melysegek[be_sor-1][be_oszlop-1]} dm")