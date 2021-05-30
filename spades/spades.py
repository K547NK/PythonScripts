#spades games
#    bid  x10               #    A,K,Q,J,10,9,8,7,6,5,4,3,2
#    bag  x1 10B = -100p    #    DECLARATION 
#    NIL  100               #    HEARTS   = H
#    BLIND NIL 200          #    DIAMONDS = D
#    TOTAL 13               #    SPADES   = S
#    SPADES RULES           #    CLUBS    = C
#import
import random
#Deck
deck =['2C','2D','2H','3C','3D','3H','4C','4D','4H','5C','5D','5H','6C','6D','6H','7C','7D','7H','8C','8D','8H','9C','9D','9H','10C','10D','10H','JC','JD','JH','QC','QD','QH','KC','KD','KH','AC','AD','AH','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS']

def shuffledHands():
    random.shuffle(deck)                          #deck shuffles
    shuffledDeck = deck                           #show what new deck looks like
    handOne   = shuffledDeck[0:13]                #divide cards by index
    handTwo   = shuffledDeck[13:26]
    handThree = shuffledDeck[26:39]
    handFour  = shuffledDeck[39:52]

#Players
def players():
    playerOne   = input('Enter 1UP:')
    playerTwo   = input('Enter 2UP:')
    playerThree = input('Enter 3UP:')
    playerFour  = input('Enter 4UP:')

print (players().playerOne)
#Commands
shuffle = shuffledHands()
newPlayers = players()

#Input for actual gameplay
#playerOneInput = (str(players.playerOne) + input('its your turn:'))
#playerThreeInput = (str(playerTwo) + input('its your turn:'))
#playerThreeInput = (str(playerThree) + input('its your turn:'))
#playerFourInput = (str(playerFour) + input('its your turn:'))

