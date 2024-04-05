def muestraAgenda(dic:dict):
    dicAux=dict(sorted(dic.items()))
    for i in dicAux:
        for j in dic[i]:
            print(f"{i}, {j} {dic[i][j]}")


dic={'Caceres':{'Pedro':'usuario1@gmail.com'},
     'AGomez':{'RGustavo':'usuario2@hotmail.com'},
     'ZGomez':{'TGustavo':'usuario2@hotmail.com'},
     'DGomez':{'YGustavo':'usuario2@hotmail.com'},
     'EGomez':{'UGustavo':'usuario2@hotmail.com'},
     'Lamas':{'Mario':'usuario3@outlook.com'}
     }
muestraAgenda(dic)