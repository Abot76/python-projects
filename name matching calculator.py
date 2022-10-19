ime1 = str(input("First name: "))
ime2 = str(input("Second name: "))
SkupnoIme = str(ime1) + str(ime2)
PreverjeneCrke = []
StevilkaCrke = 0 
TrenutnaCrka = SkupnoIme[StevilkaCrke] 
ListPonavljanjaCrk = [] 
CrkaSePonovi = 0
DolzinaSkupnegaImena = len(SkupnoIme)
SestevekStevilk = []
DolzinaLista = 0
Sestevek = 0
Stevilka1 = 0
Stevilka2 = 0
OdKonca = 0
OdZacetka = 0
DolzinaSestevka = 0
middle = 0
a = 0




def preveriPonavljanje(str, x): 
    Stej = 0
    for i in range(len(str)):
        if (str[i] == x) :
            Stej += 1
    return Stej 
 


for q in range(DolzinaSkupnegaImena):  

    if TrenutnaCrka in PreverjeneCrke: 


        
        StevilkaCrke += 1
        if StevilkaCrke < DolzinaSkupnegaImena:
            TrenutnaCrka = SkupnoIme[StevilkaCrke]

    else: 
        CrkaSePonovi = preveriPonavljanje(SkupnoIme, TrenutnaCrka)
        ListPonavljanjaCrk.append(CrkaSePonovi)
        PreverjeneCrke.append(TrenutnaCrka)

        

        
        StevilkaCrke += 1
        if StevilkaCrke < DolzinaSkupnegaImena:
            TrenutnaCrka = SkupnoIme[StevilkaCrke]
    




while len(ListPonavljanjaCrk) > 2:

    if len(ListPonavljanjaCrk) % 2 != 0:
        middle = (len(ListPonavljanjaCrk)-1) // 2
        a = ListPonavljanjaCrk[middle]
        ListPonavljanjaCrk.pop(middle)


    i = 1
    DolzinaLista = int(len(ListPonavljanjaCrk) / 2)  
    for w in range(DolzinaLista):
        OdZacetka = w
        Stevilka1 = ListPonavljanjaCrk[OdZacetka]
        OdKonca = len(ListPonavljanjaCrk) -(w+1)
        Stevilka2 = ListPonavljanjaCrk[OdKonca]
        Sestevek = int(Stevilka1) + int(Stevilka2)
        SestevekStevilk.append(Sestevek)
        
    i += 1


    if a != 0:
        SestevekStevilk.append(a)
        
    ListPonavljanjaCrk = SestevekStevilk
    SestevekStevilk = []

    


procenti= "".join(map(str, ListPonavljanjaCrk))
print(f"compatibility is {procenti}%")
