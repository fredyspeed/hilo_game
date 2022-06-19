import random


class Card:
    """This Class is need to known the values for the game 
    
    Attributes:
        value: the is a int get random.
        
    """
    def __init__(self):
        """Constructs a new Card
        
        Args:
            self (Card): an instance of Card.
        """
        self.value = 0

    def random_value(self):
        """ Give the value random
        Args:
            self (Card): an instance of Card.
        """
        self.value = random.randint(1, 12)
    
    def get_value(self):
        """ return the attribute value
        Args:
            self (Card): an instance of Card.
        """
        return self.value

        