import random
pl_score=0
comp_score=0
x=["rock","paper","scissor"]
while(True):
    pl_value=input("press r for rock, press p for paper, press s for scissor: ")
    comp_value=random.choice(x)
    print("you chose ",pl_value)
    print("computer chose ",comp_value)
    if(pl_value=="r" and comp_value=="scissor"):
        print("you won this round")
        pl_score=pl_score+1
    elif(pl_value=="r" and comp_value=="paper"):
        print("computer won this round")
        comp_score=comp_score+1
    elif(pl_value=="p" and comp_value=="rock"):
        print("you won this round")
        pl_score=pl_score+1
    elif(pl_value=="p" and comp_value=="scissor"):
        print("computer won this round")
        comp_score=comp_score+1
    elif(pl_value=="s" and comp_value=="paper"):
        print("you won this round")
        pl_score=pl_score+1
    elif(pl_value=="s" and comp_value=="rock"):
        print("computer won this round")
        comp_score=comp_score+1
    else:
        print("this round is draw")
    print("your score : ",pl_score)
    print("computer score: ",comp_score)
    if(pl_score >= 5 or comp_score >= 5 ):
        break       
if pl_score==5 :
    print("congrats!, you won")
elif comp_score==5:
    print("suck it,loser!")