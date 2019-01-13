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


plansza=[["*","*","*",],["*","*","*",],["*","*","*",]]

wyswietlPlansze(plansza)