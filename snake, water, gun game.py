import random as r
list=["s","w","g"]
choose= r.choice(list)
score=0
chances=10
while( chances>=1):
 print("enter a choice    snake/  water/  gun")
 user= input()                                         # snake water gun game
 if user=='snake' and choose=='w':
  score=score+1
  chances-=1
 elif user=='water' and choose=='g':
    score+=1
    chances-=1
 elif user=='gun' and choose=='s':
     score+=1
     chances-=1
 elif user=='water' and choose=='s':
     score = score
     chances-=1
 elif user=='gun' and choose=='w':
     score = score
     chances -= 1
 elif user=='snake' and choose=='g':
     score = score
     chances -= 1
 elif user==choose:
     score=score
     chances-=1
 print("computer choice=",choose)
 print("your choice=",user)
 print("score=", score)
 print("chances", chances)
if score>=5:
    print("Congrats!! you won the game" )
else:
    print("Ops! you lost")
