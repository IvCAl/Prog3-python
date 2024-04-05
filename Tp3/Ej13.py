def rimanPares(arr:list):
    lenArr=len(arr)
    if lenArr<2:
        print("Se necesitan mas de dos palabras.")
    elif lenArr>=2:
        for i in range(lenArr-1):
            cadA=str(arr[i]).upper()
            lenA=len(cadA)
            for j in range(i+1,lenArr):
                cadB=str(arr[j]).upper()
                lenB=len(cadB)
                men=min(lenA,lenB)
                if men>2:
                    if (cadA[lenA-1]==cadB[lenB-1] and cadA[lenA-2]==cadB[lenB-2] and cadA[lenA-3]==cadB[lenB-3]):
                        print(f"{cadA} y {cadB} Riman")
                    elif (cadA[lenA-1]==cadB[lenB-1] and cadA[lenA-2]==cadB[lenB-2]):
                        print(f"{cadA} y {cadB} Riman un poco")
                    else:
                        print(f"{cadA} y {cadB} NO riman")
                elif men==2:
                    if (cadA[lenA-1]==cadB[lenB-1] and cadA[lenA-2]==cadB[lenB-2]):
                        print(f"{cadA} y {cadB} Riman un poco")
                    else:
                        print(f"{cadA} y {cadB} NO riman")
                else:
                    print(f"{cadA} y {cadB} deben tener al menos 2 letras")


rimanPares(["n","an", "uan","juan"])