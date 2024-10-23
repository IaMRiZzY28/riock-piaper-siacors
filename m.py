import random
def  gucci():
    ucci=str(input("enter your choice")).lower()
    while ucci not in["rock","paper","scissors"]:
        print("invalid choice")
        ucci=input("enter correct choize bro/sis").lower()
        return ucci

def icc():
    return random.choice(["rock","paper","scissors"])