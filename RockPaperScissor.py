import random
def guess():
    x=random.randint(1,3)
    if x==1:
        return 1
    elif x==2:
        return 2
    elif x==3:
        return 3

print("\t\t\tWELCOME!!\n\nThis is a simple ROCK, PAPER & SCISSORS game.\n\nYou will play against a bot.\nBest of luck.\n\n\n\n")
y=int(input("Enter how many round you want to play: "))
point=0
for i in range(1,y+1):
    if i>1:
        print("\n\n")
    n=input("Type your dicision:  ").lower()
    if n=="rock":
            x=1
    elif n=="paper":
            x=2
    elif n=="scissor":
            x=3
    else:
           print("You have given wrong input :< ")
    g=guess()
    if g==1:
         print("Bot chose ROCK")
    elif g==2:
         print("Bot chose PAPER")
    elif g==3:
         print("Bot chose SCISSOR")
    if x==g:
        print("It's a tie!!")
        print(f"Chances left:    {y-i}")
        point+=0
    elif g==2 and x==3:
        print("YOU WON!!!")
        print(f"Chances left:   {y-i}")
        point+=1
    elif g==3 and x==1:
        print("YOU WON!!!")
        print(f"Chances left:  {y-i}")
        point+=1
    elif g==1 and x==2:
        print("YOU WON!!!")
        print(f"Chances left:  {y-i}")
        point+=1 
    else:
        print("YOU LOST  \n\n:( :(")
        print(f"Chances left:   {y-i}")
        point-=1
        
win=(y/2)+1
print(f"YOUR TOTAL POINT IS:   {point}\n\n\n")
if point>=win:
    print("CONGRATULATION\t\tYOU WON THIS ROUND!!!!")
else:
    print("SORRY!!\t\tYOU LOST THIS ROUND")