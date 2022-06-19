from operator import truediv
from game.card import Card


class Hilo:
    """It is the class to create an object to start the program. 
    
    The responsibility of a Hilo is to control the sequence of play.

    Attributes:
        score: The point gain start with 300 point.
        is_playing (boolean): Whether or not the game is being played.
        Card : new card - have a value that is need to play
        card_value: the value that have the card known
        card_new_value: Is the value card that is unknown
    """
    def __init__(self):
        """Constructs a new Hilo
        
        Args:
            self (Hilo): an instance of Hilo.
        """
        self.score = 300
        self.is_playing = True
        card = Card()
        card.random_value()
        self.card_value = card.get_value()
        self.card_new_value = 0

    def start_game(self):
        """ Start the game
        Args:
            self (Hilo): an instance of Hilo.
        """
        while self.is_playing:
            value = self.card_value
            print(f"The card is: {value}")
            self.new_card()
            option = self.read_option()
            self.evaluetion_result( option)
            self.is_playing = self.play_again()
    
    def new_card(self):
        """ Get the value the new card
        Args:
            self (Hilo): an instance of Hilo.
        """
        card = Card()
        card.random_value()
        self.card_new_value = card.get_value()
    
    def read_option(self):
        """ Get the value h or l 
        Args:
            self (Hilo): an instance of Hilo.
        """
        option = input("Higher or lower? [h/l] ")
        return option

    def evaluetion_result(self, option):
        """ Evaluating the input
        Args:
            self (Hilo): an instance of Hilo.
        """
        print(f"Next card was: {self.card_new_value}")
        if(self.card_value <= self.card_new_value and option == "h" ):
            self.score += 100
        elif(self.card_value > self.card_new_value and option == "l"):
            self.score += 100
        else:
            self.score -= 75
        self.card_value = self.card_new_value
        print(f"Your score is: {self.score}")

    def play_again(self):
        """ verified if can continue or no the game"""
        if(self.score > 0):
            continue_game = input("Play again? [y/n] ")
            if (continue_game == "y"):
                return True
        return False

 