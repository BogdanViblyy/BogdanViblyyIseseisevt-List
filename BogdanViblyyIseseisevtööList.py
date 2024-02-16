#1
#from string import *
#vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
#konsonanti="qwrtpsdfghjklzxcvbnm"
#markid=punctuation
#v=k=m=t=0
#tekst=input("Sisesta sõna või lause: ").lower()
#tekst_list=list(tekst)
#for sümbol in tekst_list:
#    if sümbol in vokaali:
#        v+=1
#    elif sümbol in konsonanti:
#        k+=1
#    elif sümbol in markid:
#        m+=1
#    elif sümbol ==" ":
#        t+=1
#print("Vokaali:",v,"\nKonsonanti:",k)
#print("Kirjuvahemärgid:",m)
#print("Tühikud:",t)


#2
#nimed=[]
#for i in range(5):
#    nimi=input("Sisesta nimi: ").capitalize()
#    nimed.append(nimi)
#print("Loetelu oli: ",nimed)
#nimed.sort()
#print("Loetelu sorteeritud: ",nimed)
#for n in range (len(nimed)):
#    print(n+1,".",nimed[n],sep="")
#print("Vimasena oli lisatud: ",nimi)

#uued_nimed=[]
#for nimi in nimed:
#    if nimi not in uued_nimed:
#        uued_nimed.append(nimi)
#print(uued_nimed)



#from random import *
#nimekiri=[]
#n=int(input("Nimekirja pikkus: "))
#for i in range(n):
#    arv=randint(10,100)
#    nimekiri.append(arv)
#    n=len(nimekiri)
#maksimum=max(nimekiri)
#maksimumikoht=nimekiri.index(maksimum)
#vajavarv=maksimum/len(nimekiri)
#nimekiri.remove(maksimum)
#nimekiri.insert(maksimumikoht,vajavarv)
#print("Muudetud imekiri: ",nimekiri)


# Ülesanne nr 7
from random import *
nimekiri=[]
try:
    n=int(input("Nimekirja pikkus: "))
except ValueError:
    print("Viga")
for i in range(n):
    arv=randint(10,100)
    nimekiri.append(arv)
    n=len(nimekiri)
try:
    kuidassorteerida=int(input("Kuidas tahad nimekirja sorteerida, suurest väiksemale(1), või väiksest suuremale(0)?"))
except ValueError:
    print("Viga")
if kuidassorteerida == 1:
    nimekiri.sort(reverse=True)
    print("Nimekiri, sorteeritud suurest väiksemale:", nimekiri)
else:
    nimekiri.sort()
    print("Nimekiri, sorteeritud väiksest suuremale:", nimekiri)