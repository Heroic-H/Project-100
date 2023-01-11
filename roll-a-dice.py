import random

question=0

dice=["[   ]\n"+"[ 0 ]\n"+"[   ]\n","[  0]\n"+"[   ]\n"+"[0  ]\n","[  0]\n"+"[ 0 ]\n"+"[0  ]\n","[0 0]\n"+"[   ]\n"+"[0 0]\n","[0 0]\n"+"[ 0 ]\n"+"[0 0]\n","[0 0]\n"+"[0 0]\n"+"[0 0]\n"]

cont=0

while question!="y":
    question=str(input("do you want to roll a dice? y/n"))

while cont!="n":
    no=random.randint(1,6)
    print(dice[no-1])
    cont=str(input("do u want to continue? y/n"))
    if cont=="n":
        quit()