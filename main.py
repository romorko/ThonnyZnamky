#Praca so subormi 

def citaj_cely_subor(nazov_suboru:str)->str:
    """Precita naraz cely obsah suboru do jedneho retazca
       mozny parameter n read(n) je max. pocet precitanych znakov
    """
    with open(nazov_suboru,'r',encoding="utf-8") as f:
        obsah = f.read()
    return obsah


def citaj_jeden_riadok(nazov_suboru:str)->str:
    """Precita jeden riadok zo suboru vratane konca riadku
        strip odstrani koniec riadku aj medzery na zaciatku a konci
        rstrip('\n') odstrani len koniec riadku a medzery necha
    """
    with open(nazov_suboru,'r',encoding="utf-8") as f:
        riadok = f.readline().strip()
    return riadok

def citaj_vsetky_riadky(nazov_suboru:str)->list[str]:
    """Precita vsetky riadky a vrati ich ako zoznam retazcov
        cita aj konce riadkov
    """
    with open(nazov_suboru,'r',encoding="utf-8") as f:
        riadky = f.readlines()
    return riadky

def citaj_po_riadkoch(nazov_suboru:str)->None :
    """Najlepsi sposob spracovania textoveho suboru citanim po riadkoch"""
    with open(nazov_suboru,'r',encoding="utf-8") as f:
        for riadok in f:
            print(riadok)  #alebo in0 spracovanie riadku...
            slova = riadok.split() #napr rozdeli riadok na slova podla medzier
            
def citaj_po_znakoch(nazov_suboru:str)->None :
    """Cita po znakoch do konca suboru 
    """
    with open(nazov_suboru, "r", encoding="utf-8") as f:
        while znak := f.read(1):
            print(repr(znak))
            
def citaj_po_znakoch_po_riadkoch(nazov_suboru:str)->None :
    """Cita po znakoch po riakoch do konca suboru
        restrip odsekne znak noveho riadku
    """
    with open(nazov_suboru, "r", encoding="utf-8") as f:
        for riadok in f:
            for znak in riadok.rstrip("\n"):
                print(repr(znak))
            
            
def zapis_retazec_do_suboru(nazov_suboru:str,text:str)->int:
    """Zapise text do suboru, predtym ho VYMAZE!!!
        Kazdy write vrati pocet zapisanych znakov
        Koniec riadku sa musi zapisat zvlast
    """
    with open(nazov_suboru, "w", encoding="utf-8") as f:
        pocet_zapisanych_znakov = f.write(text)
    return pocet_zapisanych_znakov

def zapis_retazce_do_suboru(nazov_suboru:str,retazce:list[str])->None :
    with open(nazov_suboru, "w", encoding="utf-8") as f:
        f.writelines(retazce)
        

def pridaj_retazec_do_suboru(nazov_suboru:str,text:str)->int:
    with open(nazov_suboru, "a", encoding="utf-8") as f:
        pocet = f.write(text)    
    return pocet
    
