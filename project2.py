import random
n=random.randint(1,100)
guesses=0

a=-1
while(a!=n):
    a=int(input("enter a number"))
    guesses+=1
    if a>n:
        print("guess a lower number")
    else:
        print("guess a higher number")
print(f"correct guess in {guesses} attempt")
