import random

def name_to_number(name):
    """
    Takes name and converts it to a number.
    In case of incorrect input return None.
    """

    # Your code goes here.


def number_to_name(num):
    """
    Takes a number and converts it into a name.
    """

    # Your code goes here.


def get_random_number():
    """
    Just get a random number from 0 through 4.
    """

    # Your code goes here.


def rpsls(user_name):
    """
    Takes a name that user inputs.
    Generates a random computer’s choice and announces the winner.
    """
    DRAW = "Draw!"
    COMPUTER_WINS = "Computer wins!"
    PLAYER_WINS = "Player wins!"

    player_number = name_to_number(user_name)
    if player_number is None:
        return "Input a correct choice!"

    # Your code goes here.

    phrase = "Player chooses {}\nComputer chooses {}\n{}".format(user_name, comp_name, announce)
    return phrase


if __name__ == "__main__":
    print(rpsls("rock")) # spock, paper etc.
