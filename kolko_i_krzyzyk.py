def wyswietlPlansze(lista2D):
    for i in lista2D:
        for e in i:
            print(i,end="")
        print()

plansza=[["*","*","*",],["*","*","*",],["*","*","*",]]

wyswietlPlansze(plansza)