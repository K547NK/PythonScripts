#spades games
#    bid  x10
#    bag  x1 10B = -100p 
#    NIL  100
#    BLIND NIL 200
#    TOTAL 13
#    SPADES RULES
#    A,K,Q,J,10,9,8,7,6,5,4,3,2
#    DECLARATION 
#    HEARTS   = H
#    DIAMONDS = D
#    SPADES   = S
#    CLUBS    = C
import random
#Deck
deck =['2C','2D','2H','3C','3D','3H','4C','4D','4H','5C','5D','5H','6C','6D','6H','7C','7D','7H','8C','8D','8H','9C','9D','9H','10C','10D','10H','JC','JD','JH','QC','QD','QH','KC','KD','KH','AC','AD','AH','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS']
# Add value to index groups of 3 items at a time
deck[0:2] = 1
deck[3:5] = 2
deck[6:8] = 3
deck[9:11]= 4
deck[12:14]=5
deck[15:17]=6
deck[18:20]=7
deck[21:23]=8
deck[24:26]=9
deck[27:29]=10
deck[30:32]=11
deck[33:35]=12
deck[36:38]=13

def spade(s):
   deck[-40:51]
sum = 14
for s in sum:
   s = sum #individual index
if sum < 27:
   sum ++
elif sum == 27:
    break



#Players
P1 = input('Enter 1UP:')
P2 = input('Enter 2UP:')
P3 = input('Enter 3UP:')
P4 = input('Enter 4UP:')

#Shuffle Darks
shuffleCards = shuffle(deck)

#Deal the cards
dealCards = print(random.shuffleCards(13))
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
  
  
