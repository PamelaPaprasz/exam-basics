# Create a Card class, that has a color and a value
# Create a constructor for setting those values
# Card should be represented as string in this format:
# 9 Hearts
# Jack Diamonds
# Create a Deck class, that has a list of cards in it
# Create a constructor that takes a whole number as parameter
# The constructor should fill the list with the number of different cards using at least 4 different colors (except if the number given is smaller than four, than all cards should have different colors)
# We should be able to shuffle the deck, which randomly orders the cards
# We should be able to draw the top card which returns the drawn card and also removes it from the deck
# Deck should be represented as string in this format:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
import random 

class Card():
    
    def __init__(self):
        self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'King', 'Queen', 'Ace']
        self.possible_colors = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.value = random.choice(self.possible_values)
        self.color = random.choice(self.possible_colors)
        
class Deck(Card):
    
    def __init__(self, number):
        self.card_list = []
        self.number = number
        
        while number > 0:
            card = Card()
            self.card_list.append(card)
            number -= 1    
            
    def shuffle_cards(self): 
        random.shuffle(self.card_list)
        
    def draw(self):
        top_card = self.card_list[0]
        self.card_list.remove(top_card)
        return top_card
        

card =  Card()
print(card)
deck = Deck(12)
print(deck.card_list)
# Should print out:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
top_card = deck.draw()
print(top_card)
print(deck)
# Should print out:
# Queen Spades
# 11 cards - 3 Clubs, 3 Diamonds, 3 Hearts, 2 Spades
