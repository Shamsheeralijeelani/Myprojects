import random
import laughtur
def l():
    print('you loose ',"\U0001F923")

p=['rock','paper','scissors']
#print('choose your options 1.rock  2.paper 3.scissors ')
"""nu=int(input())
u=p[nu]
print(u)
sy =p[random.randrange(1,3)]"""
x= 0


while x==0:
    print('choose your options 1.rock  2.paper 3.scissors ')
    
    
    try:
        nu=int(input())
        u=p[nu-1]
        print('your selection is  ',u)
        sy =p[random.randrange(1,3)]
        print('computer selected ', sy)
        if  u==p[0]:
            if sy==p[2]:
                print('you win')
            else:
                l()     

        elif u==p[1]:
            if sy==p[0]:
                print('you win')
            else:
                l()
        else :
            if sy==p[1]:
                print('you win')
            else:
                l()

        print("1 to continue and 2 to exit")
        uuu = int(input())
        if uuu==1:
            x=0
        
        elif uuu==2:
            x=1
            print('thankyou for playing the game, byeeee!!!!!')
            laughtur.a
        
        else:
            print("valid output")
        
    except:
        print('enter valid input')







