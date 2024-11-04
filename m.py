import random
def gucci():
    uc=str(input("enter your choice")).lower()
    while uc not in["rock","paper","scissors"]:
        print("invalid choice")
        uc=input("enter correct choize bro/sis").lower()
        return uc

def icc():
    return random.choice(["rock","paper","scissors"])

def play():
    print("welcome to rock piaper siciasor")
    uc= gucci()
    cc=icc()
    print("u chose {uc}")
    print("computer chose {cc}")
    result=winner(uc,cc)
    print(result)

def winner(uc,cc):
    if uc==cc:
        return "tie!"
    elif(uc=="rock" and cc=="scissors")or\
        (uc=="paper" and cc=="rock")or\
        (uc=="sicssor" and cc=="paper"):

        return "u win"

    else:
        return "computer wins"

if __name__=="__m__":
    play()
