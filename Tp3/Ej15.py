import random
def generaDado():
    return  random.randint(1,6)

def juego(apuesta:float):
    dados=0
    while(dados>3 or dados<1):
        dados=int(input("Puede elegir de 1 a 3 dados. Con cuantos dados quiere jugar?: "))
        if(dados>3 or dados<1):
            print("Elija entre 1 y 3")
    suma=0
    for i in range(dados):
        dado=generaDado()
        print(f"El {i+1}° dado cayó en el número {dado}")
        suma+=dado
    if dados==1 and suma>4:
        print(f"Usted gana ${apuesta*0.1}")
    elif dados==2 and suma>8:
        print(f"Usted gana ${apuesta*0.5}")
    elif dados==3 and suma==18:
        print(f"Usted gana ${apuesta*3}")
    else:
        print(f"Usted pierde ${apuesta}")
    
juego(100)