options = {
"symboly":'''
Délka : L 
----------
centimetr : cm
foot (stopa) : ft
inch (palec): in
kilometr : km
metr : m
mikrometr ; um
míle : mi
millimetr : mm
nanometr : nm
námořní míle : nmi
yard : yd                      

Obsah : A 
----------
akr : ac
hektar : ha
stopy čtverční: ft2
palce čtv : in2
km čtv: km2
m čtv. : m2
míle čtv. : mi
yardy čtv. : yd2

Objem : V 
----------
kubický cm : cm3
kubická stopa : ft3
kubický palec : in3
kubický m : m3
litr : l
mililitr : ml

Váha : M 
----------
gram : g
kilogram : kg
miligram : mg
unce : oz
libra : lb
tuna : t

Čas : T
----------
den : d
hodina : h
minuta : min
sekunda : sek
týden : tyd
rok : r

''',

"help":'''

Vítejte v převodníku jednotek.


Hodnoty pro výpočet zadávejte v následujícím formátu:

Zadávejte ve formátu:
Kategorie jednotek <mezera> Jednotka <mezera> Hodnota <mezera> Jednotka do které bude převáděno

Kategorie jednotek : L pro délku, T pro čas, A pro obsah, V pro objem.
U jednotek například m pro metr, km pro kilometr, ft pro stopy, ha pro hektar...


Příklad :   T tyd 4 h  (Převede čas, konkrétně 4 týdny na hodiny)

Zadejte   "help"    pro nápovědu 
Zadejte   "symboly" pro zobrazení symbolů jednotek
Zadejte   "x"       pro ukončení programu

'''
}



#table s jednotkami
L= {"m":1 ,
    "km":10**(-3),
    "cm":10**(2),
    "mm":10**(3),
    "um":10**(6),
    "nm":10**(9),
    "mi":0.000621,
    "ft":3.28084,
    "in":39.3701,
    "yd":1.09361,
    "nmi":0.0005399}

A= {"ha":10**(-4),
    "ac":0.000247,
    "km2":10**(-6),
    "m2":1,
    "mi2":3.86*(10**-7),
    "ft2":10.7639,
    "in2":1550.0031,
    "yd2":1.19599 }

V= {"m3":1 ,
    "cm3":10**(6),
    "ml":10**(6),
    "l":10**(3),
    "in3":61023.7441,
    "ft3":35.31467}

M= {"g":1 ,
    "kg":10**(-3),
    "mg":10**(3),
    "t":10**(-6),
    "lb":0.0022046,
    "oz":0.03527}

T= {"r":0.0027397,
    "tyd":0.142857,
    "d":1,
    "h":24,
    "min":1440,
    "sek":86400 }
