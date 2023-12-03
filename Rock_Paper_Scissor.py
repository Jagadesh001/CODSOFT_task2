#Importing the random module
import random

#Creating a list for the game
#R - Rock, P - Paper, S - Scissor
game = ['R','P','S']
ans = 'y'

#points of the user and AI from the computer respectively
up = 0
AIp = 0

#User wins when the following happens:
#User - Rock , AI -  Scissor
#User -  Paper, AI - Rock
#User - Scissor, AI paper
#Similarly AI wins when the vice-versa happens

#Here this program will run on a loop, according to the time the user wants to spend playing this game, when the user says yes the game will continue, else it will stop

while(ans=='y'):
    print('1.Rock')
    print('2.Paper')
    print('3.Scissor')
    user = input('enter rock/paper/scissor:')
    AI = random.choice(game)
    if(user in game):
       if(user=='R'):
          if(AI=='S'):
             print('user wins')
             up+=1
             print('User points: ',up)
             print('AI points: ',AIp)
          elif(AI=='P'):
             print('AI wins')
             AIp+=1
             print('User points: ',up)
             print('AI points: ',AIp)
          elif(AI=='R'):
             print('game draw')
             print('User points: ',up)
             print('AI points: ',AIp)
          ans=input('Do you want to continue?: ')

       if(user=='P'):
          if(AI=='R'):
             print('user wins')
             up+=1
             print('User points: ',up)
             print('AI points: ',AIp)
          elif(AI=='S'):
             print('AI wins')
             AIp+=1
             print('User points: ',up)
             print('AI points: ',AIp)
          elif(AI=='P'):
             print('game draw')
             print('User points: ',up)
             print('AI points: ',AIp)
          ans=input('Do you want to continue?: ')

       if(user=='S'):
          if(AI=='P'):
             print('user wins')
             up+=1
             print('User points: ',up)
             print('AI points: ',AIp)
          elif(AI=='R'):
             print('AI wins')
             AIp+=1
             print('User points: ',up)
             print('AI points: ',AIp)
          elif(AI=='S'):
             print('game draw')
             print('User points: ',up)
             print('AI points: ',AIp)
          ans=input('Do you want to continue?: ')

    else:
        print('wrong choice')
        ans = input('Do you want to try again?: ')

print('Final scores')
print('User: ',up)
print('AI: ',AIp)
if(up>AIp):
  print('User wins the game')
elif(AIp>up):
  print('AI wins the game')
else:
  print('match drawn')
ans = input('Do you want to continue?: ')
