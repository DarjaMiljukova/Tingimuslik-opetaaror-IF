from math import *
from pickle import TRUE
#Ülesanne 1
#try:
#    nimi=input("Sisestage oma nimi ")

#    if nimi.upper()=="JUKU":
#        print("Lähme kinno")
#        vanus=int(input("Kui vana sa oled? "))
#        if vanus<=0 or vanus>=100:
#            print("Viga andmetega")
#        elif vanus<6:
#            print("Tasuta")
#        elif vanus>=6 and vanus<=14:
#            print("Lapse pilet")
#        elif vanus>=15 and vanus<=65:
#            print("Täispilet")
#        elif vanus>=65:
#            print("Sooduspilet")
#        elif vanus<=0 or vanus>=100:
#            print("Viga andmetega")

#    else:
#        print("Otsime Juku")
#except:
#    print("Vale Andmetüüp")

#Ülesanne 2
#nimi1=input("Mis sinu nimi on? ")
#nimi2=input("Mis sinu nimi on? ")
#if nimi1.isalpha()==True and nimi2.isalpha():
#    if nimi1.lower()==("Liri") and nimi2.lower()==("Kiri"):
#        print(f"{nimi1} ja {nimi2} olete täna naabrid")
#    else:
#        print()
#else:
#    print("Vale Andmetüüp")

#Ülesanne 3
#try:
#    a=float(input("määrake ristkülikukujulise ruumi pikkus ->"))
#    b=float(input("määrake ristkülikukujulise ruumi laius ->"))
#    if a>=0 and b>=0:
#        S=a*b
#        print(f"ristküliku pindala on {S}")
#        c=int(input("Kas te soovite remonti teha? kui 1=ja või 0=ei: "))
#        if c==1:
#            print("Kui palju ta maksab ruutmeeter ja mitu põranda vahetamise hind?")
#        else:
#            print("Hüvasti")
#    else:
#        print("Vale Andmetüüp")
#except:
#    print("Vale Andmetüüp")

#Ülesanne 4
try:
    hind=float(input("Mis hind?"))
    if hind>0:
        if hind>700:
                print(f"Sul on soodus 30%, {hind-hind*0.3}")

        else:
            print(f"{hind}")
except:
    print("Vale Andmetüüp")


#Ülesanne 5