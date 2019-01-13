# szachy
print("szachownica")
print()
szachownica=(("W","S","G","D","H","K","G","S","W"),("P","P","P","P","P","P","P","P","P"),("*","*","*","*","*","*","*","*","*"),("*","*","*","*","*","*","*","*","*"),("*","*","*","*","*","*","*","*","*"),("*","*","*","*","*","*","*","*","*"),("P","P","P","P","P","P","P","P","P"),("W","S","G","D","H","K","G","S","W"))

for i in szachownica:
    for p in i:
        print(p,end="")
    print()


# losowanie
import random

liczby=set()
while len(liczby)<6:
    liczby.add(random.randint(1,49))

print()
print(liczby)
print()

# słownik

slownik=dict()
slownik={"pierwsza" : [1,2,3],"druga" : [4,4,5],"inna" : [2,4,5]}

for i in slownik:
    print(i,end=" ")
