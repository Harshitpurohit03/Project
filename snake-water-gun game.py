import random
def game(comp,you):
    if(comp==you):
        return None
    if(comp=='s'):
        if(you=='w'):
            return True
        elif(you=='g'):
            return True
        else:
            return False
    elif(comp=='w'):
        if(you=='s'):
            return False
        if(you=='g'):
            return False
        else:
            return True
    elif(comp=='g'):
        if(you=='w'):
            return False
        elif(you=='s'):
            return False
        else:
            return True
print("Computer's Turn")
num=random.randint(1,3)
you=input("Your Turn:")
if(num==1):
    comp= 's'
elif (num==2):
    comp= 'w'
if (num==3):
    comp= 'g'
a=game(comp,you)
print("Computer's Move is",comp)
if(a==None):
    print("Game Draw")
elif(a==True):
    print("You Win,Hurray")
elif(a==False):
    print("Sorry,You Lose")
