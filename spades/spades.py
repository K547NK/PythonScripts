''''spades games
    bid  x10
    bag  x1 10B = -100p 
    NIL  100
    BLIND NIL 200
    TOTAL 13
    SPADES RULES
    A,K,Q,J,10,9,8,7,6,5,4,3,2
    DECLARATION 
    HEARTS   = H
    DIAMONDS = D
    SPADES   = S
    CLUBS    = C

'''
import random

# Declare Card Values
[2C, 2D, 2H] = 1
[3C, 3D, 3H] = 2
[4C, 4D, 4H]= 3
[5C, 5D, 5H]= 4
[6C, 6D, 6H] = 5
[7C, 7D, 7H] = 6
[8C, 8D, 8H] = 7
[9C, 9D, 9H ]= 8
[10C, 10D, 10H] = 9
[JC, JD, JH ]= 10
[QC, KD, KH ]= 11
[KC, KD, KH ]= 12
[AC, AD, AH ]= 13
2S = 14
3S = 15
4S = 15
5S = 16
6S = 17
7S = 18
8S = 19
9S = 20
10S = 21
JS = 22
QS = 23
KS = 24
AS = 25
#Spades
deck = [2C, 2D, 2H, 3C, 3D, 3H,4C, 4D, 4H 5C, 5D, 5H, 6C, 6D, 6H, 7C, 7D, 7H, 8C, 8D, 8H, 9C, 9D, 9H, 10C, 10D, 10H,JC, JD, JH,QC, KD, KH,KC, KD, KH, AC, AD, AH, 2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S, 10S, JS, QS, KS, AS]
shuffleCards = shuffle(deck)
dealCards = print(random.shuffleCards(13))

#Players
P1 = input('Enter 1UP:')
P2 = input('Enter 2UP:')
P3 = input('Enter 3UP:')
P4 = input('Enter 4UP:')

#Deal the cards
print(' Shuffle up and deal !')
x = 4
for x in dealCards:
    print ('dealing 1UP')
    x - 1
    dealCards
    if x == 3 :
        dealCards
        print('dealing 2UP')
        x - 1
    elif x == 2 :
        dealCards
        print ('Dealing 3UP')
        x - 1
    elif x == 1 :
        dealCards
        print ('Dealing 4UP')
        x - 1
    elif x == 0
        print ('Dealing done Enjoy!')
        break
  
  
