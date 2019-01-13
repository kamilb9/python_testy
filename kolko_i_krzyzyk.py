def wyswietlPlansze(lista2D):
    print("",1,2,3)
    nr_wiersza=1
    for i in lista2D:
        print(nr_wiersza,end="")
        for e in i:
            print(e,end=" ")
        nr_wiersza+=1
        print()

graKrzyzyk=False
start=input("X czy O: ")

if start == "X":
    graKrzyzyk=True

def wygrana(lista2D):
    for x in range(0,3):
        if mapa2D[x][0]==mapa2D[x][1] and mapa2D[x][1]==mapa2D[x][2]:
            return True
    for y in range(0,3):
        if mapa2D[0][y]==mapa2D[0][y] and mapa2D[0][y]==mapa2D[0][y]:
            return True
    if mapa2D[0][0]==mapa2D[1][1] and mapa2D[1][1]==mapa2D[2][2]:
        return True
    if mapa2D[0][2]==mapa2D[1][1] and mapa2D[1][1]==mapa2D[2][0]:
        return True
    return False

def remis(lista2D):
    if not wygrana(lista2D):
        wolnePole= False
        for x in lista2D:



plansza=[["*","*","*",],["*","*","*",],["*","*","*",]]

wyswietlPlansze(plansza)