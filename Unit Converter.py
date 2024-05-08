from Converter_values import *        

print(options["help"])              
vstup = input("Příkaz: ")

while vstup.lower() != "x":  # ukončení programu     
    vstup = vstup.strip().split(" ")
    
    try:        # ošetření chyby
        if len(vstup) == 1:
            print(options[vstup[0]])                                  
            
        elif len(vstup) == 4: # převod jednotek
            for i in vstup[3].split(','):
                value = round( eval( "{} * {}['{}'] / {}['{}']".format(vstup[2],vstup[0],i,vstup[0],vstup[1]) ) , 6 )    
                print("{} \t : {}".format(i,value))                               
                 
        else:
            print("Neplatný příkaz")
            
    except:
        print("Neplatný příkaz")

    vstup = input("\nPříkaz: ")

    

