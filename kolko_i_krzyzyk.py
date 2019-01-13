def wyswietlPlansze(lista2D):
    for i in lista2D:
        for e in i:
            print(e,end=" ")
        print()

graKrzyzyk=False
start=input("X czy O: ")

plansza=[["*","*","*",],["*","*","*",],["*","*","*",]]

wyswietlPlansze(plansza)