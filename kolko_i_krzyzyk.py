def wyswietlPlansze(lista2D):
    print("",1,2,3)
    nr_wiersza=1
    for i in lista2D:
        print(nr_wiersza,end="")
        for e in i:
            print(e,end=" ")
        nr_wiersza+=1
        print()

def wygrana(lista2D):
    for x in range(0,3):
        if lista2D[x][0] == lista2D[x][1] and lista2D[x][1] == lista2D[x][2] and lista2D[x][2] == "X" or lista2D[x][2] == "O":
            return True
    for y in range(0,3):
        if lista2D[0][y] == lista2D[0][y] and lista2D[0][y] == lista2D[0][y] and lista2D[0][y] == "X" or lista2D[0][y] == "O":
            return True
    if lista2D[0][0] == lista2D[1][1] and lista2D[1][1] == lista2D[2][2]and lista2D[2][2] == "X" or lista2D[2][2] == "O":
        return True
    if lista2D[0][2] == lista2D[1][1] and lista2D[1][1] == lista2D[2][0] and lista2D[2][0] == "X" or lista2D[2][0] == "O":
        return True

    return False

def remis(lista2D):
    if not wygrana(lista2D):
        for x in lista2D:
            for y in x:
                if y=="*":
                    return False
        return True
    else:
        return False

graKrzyzyk=False
start=input("Wybierasz kółko O czy krzyżyk X?: ")
if start == "X":
    graKrzyzyk=True
plansza=[["*","*","*",],["*","*","*",],["*","*","*",]]

while (not remis(plansza)) and (not wygrana(plansza)):
    wyswietlPlansze(plansza)
    x, y = [int(x) for x in input("Podaj współrzedne stawianego X lub O").split()]
    if plansza[x-1][y-1]=="*":
        if graKrzyzyk:
            plansza[x-1][y-1]="X"
            graKrzyzyk=False
        else:
            plansza[x-1][y-1]="O"
            graKrzyzyk=True
wyswietlPlansze(plansza)

if wygrana(plansza):
    if graKrzyzyk:
        print("Wygrały O")
    else:
        print("Wygrał X")
else:
    print("Remis")