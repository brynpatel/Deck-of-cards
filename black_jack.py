from deck_of_cards import *

def check(card1, card2):
    if card1.number == card2.number:
        check = True
        #Add special cards
    elif card1.suit == card2.suit:
        check = True
    else:
        check = False
    return check

def turn(myCard, myHand, opponentsHand, deck):
    cardplayed = False
    while cardplayed == False:
        myCard = input("what card would you like to put down?, press P to pick up. ")
        if myCard.lower() == "p":
            deck.cards[0].move(deck.cards, myHand.cards)
            print("You picked up")
            cardplayed = True
        elif myCard.isdigit():
            if len(myHand.cards) >= int(myCard):
                myCard = int(myCard)-1
                if check(myHand.cards[myCard], discard_pile.get_face_card()) == True:
                    print("You played", myHand.cards[myCard])
                    myHand.cards[myCard].move(myHand.cards, discard_pile.cards)
                    cardplayed = True
                else:
                    print("You can't play that card right now, try again")
            else:
                print("You don't have that many cards!")
        else:
            print("That is not a valid option, try again")
            cardplayed = False

    for card in opponentsHand.cards:
        if check(card, discard_pile.get_face_card()) == True:
            print("I played", card)
            card.move(opponentsHand.cards, discard_pile.cards)
            return
    deck.cards[0].move(deck.cards, opponentsHand.cards)
    print("I had to pick up")

hand_size = 7
deck =Deck()
my_hand = Hand()
opponents_hand = Hand()
discard_pile = Discard_Pile()
my_card = 0
opponents_card = 0
win = False

deck.shuffle()

for i in range(hand_size):
    deck.deal(my_hand)
    deck.deal(opponents_hand)

print(my_hand)
#print(opponents_hand)

deck.cards[0].move(deck.cards, discard_pile.cards)

print(discard_pile.get_face_card())

while win == False:
    turn(my_card, my_hand, opponents_hand, deck)
    if len(my_hand.cards) == 0:
        print("You win")
        win = True
    elif len(opponents_hand.cards) == 0:
        print("You lose")
        win = True
    else:
        win = False
        print("=========================NEXT TURN======================")
        print(my_hand)
        print(discard_pile.get_face_card())
