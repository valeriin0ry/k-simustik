from string import *
from time import sleep
from random import *
def loe_ankeet(fail:str)->any:
    fail=open(fail,"r",encoding="utf-8")
    kus=[]
    vas=[]
    #kus_vas={}
    for line in fail:
        n=line.find(":")# , - ???????????
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip())

        #k.v=line.strip().split(":")
        #kus_vas[k]=v

    fail.close()
    return kus,vas #,kus_vas

def autoriseerimine(kasutajad:list, paroolid:list):
    p=0
    while True:
       if kasutajad.index(kasutaja)==paroolid.index(parool):
        kasutaja=input("Sisestage kasutajanimi: ")
        parool=input("Sisestage parool: ")
        print("Sisselogimine �nnestus!")
        return kasutaja
       else:
        p+=1
        print("Vale nimi v�i salas�na!")
       if p==5:
           print("Proovi uuesti 10 sek p�rast")
           for i in range(10):
               sleep(1)
               print(f"On j��nud {10-i} sek")
       else:
          print("Kasutajat pole")
          break
    
def loe(Ankeet:str):
    fail=open(Ankeet,"r",encoding="utf-8")
    kus=[]
    vas=[]
    fail=open(Ankeet, 'r', encoding='utf-8')
    for line in fail:
        n=line.find(":")
        kus.append(line[0:n].strip())
        vas.append(line[n+1:len(line)].strip())
        fail.close()
        return kus,vas

def lisa(kus_vas, Ankeet:str):
    fail=open(Ankeet, 'a', encoding='utf-8')
    for k�simus, vastus in kus_vas.items():
        fail.write(f"{k�simus}:{vastus}\n")
    fail.close()

def k�simus_vastus(kus_vas, n):
    punktid=0
    k�simused=random.sample(list(kus_vas), n)
    for k�simus in k�simused:
        print(k�simus)
        vastus=input("Vastus: ").strip()
        if vastus.lower()==kus_vas[k�simus].lower():
            punktid+=1
    return punktid

def salvesta(osaleja_nimi, punktid, Oiged:str, Valed:str):
    if punktid>len("kus_vas")/2:
        oiged=open(Oiged, 'a', encoding='utf-8')
        oiged.write(f"{osaleja_nimi}\n")
        oiged.close()
    else:
        valed=open(Valed, 'a', encoding='utf-8')
        valed.write(f"{osaleja_nimi}\n")
        valed.close()