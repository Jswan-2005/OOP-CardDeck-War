#OOP - Deck of Cards
#Implemented into a 'War' Game
import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))

    def __str__(self):
        value_lookup = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        val = value_lookup.get(self.value, str(self.value))
        return f"{val} of {self.suit}"


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] =  self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

    def splitDeck(self):
        half = len(self.cards)//2
        return self.cards[:half], self.cards[half:]

class Player():
    def __init__(self, name, individualDeck):
        self.name = name
        self.individualDeck = individualDeck

    def show(self):
        for c in self.individualDeck:
            c.show()

    def __len__(self):
        count = 0
        for card in self.individualDeck:
            count += 1
        return count

    def pop(self):
        return self.individualDeck.pop()

    def add_cards(self, cards):
        for card in cards:
            self.individualDeck.append(card)




def War(name):
    gameStart = input("Would you like to play a round of WAR (Y/N): ")
    print()
    if gameStart.lower() == 'n':
        print("Thanks for playing!")
        quit()
    if gameStart.lower() == 'y':
        deck = Deck()
        deck.shuffle()

        userDeck, AIDeck = deck.splitDeck()

        userPlayer = Player(name, userDeck)
        AIPlayer = Player('AI', AIDeck)

        while len(userPlayer) != 0 and len(AIPlayer) != 0:
            #Retrieve the top card from the deck
            userCard = userPlayer.pop()
            AICard = AIPlayer.pop()

            #Retrieve the value of these cards
            userValue = userCard.value
            AIValue = AICard.value

            #Wager
            userWager = [userCard]
            AIWager = [AICard]

            #Print out both the userValue and the AIValue
            print(f"Your card is a {userCard}")
            print(f"Your opponents card is a {AICard}")
            print()

            #Logic - Whose card is 'greater' than anothers
            if userValue > AIValue:
                print("You have won this round")
                print()
                #The opponents card is retrieved and placed on the bottom of the users deck along with his card
                userPlayer.add_cards(userWager + AIWager)
            elif userValue < AIValue:
                #The users card is retrieved and placed on the bottom of the opponents deck along with his card
                AIPlayer.add_cards((AIWager + userWager))
                print("You have lost this round")
                print()
            elif userValue == AIValue:
                #Both players wager three more cards face down and then one more face up and compare
                print("This round is a tie")
                print("Three more cards will be wagered on your next turn")
                print()
                if len(userPlayer) < 4:
                    print("You don't have enough cards for war. You lose!")
                    return
                if len(AIPlayer) < 4:
                    print("Your opponent doesn't have enough cards for war. You win!")
                    return


            userWager += [userPlayer.pop(), userPlayer.pop(), userPlayer.pop()]
            AIWager += [AIPlayer.pop(), AIPlayer.pop(), AIPlayer.pop()]
            print(f'You have {len(userPlayer)} cards remaining')
            print(f'Your opponent has {len(AIPlayer)} card remaining')

            next_turn = input("Press Enter to play the next round (or type 'q' to quit): ")
            print()
            if next_turn.lower() == 'q':
                print("Thanks for playing!")
                quit()

        if len(userPlayer) == 0:
            print("You lose")
        elif len(AIPlayer) == 0:
            print("You win")

if __name__ == "__main__":
    userName = input("Whats your name?: ")
    War(userName)

