def separar(arr:list,arrPar:list,arrImpar:list):
    try:
        for i in arr:
            if i%2==0:
                arrPar.append(i)
            else:
                arrImpar.append(i)
        arrPar.sort()
        arrImpar.sort()
    except TypeError:
        print("Solo se admiten numeros")
        

arr1=[6,5,4,3,2,1]
arrP=list()
arrI=list()

separar(arr1,arrP,arrI)
print(arrP)
print(arrI)
