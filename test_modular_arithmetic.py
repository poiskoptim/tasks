import unittest
from modular_arithmetic import name_to_number, \
    number_to_name, get_random_number, rpsls


class TestGeneral(unittest.TestCase):
    def test_name_to_number(self):
        self.assertEqual(name_to_number("rock"), 0)
        self.assertEqual(name_to_number("spock"), 1)
        self.assertEqual(name_to_number("paper"), 2)
        self.assertEqual(name_to_number("lizard"), 3)
        self.assertEqual(name_to_number("scissors"), 4)
        self.assertEqual(name_to_number("not_rock"), None)

    def test_number_to_name(self):
        self.assertEqual(number_to_name(0), "rock")
        self.assertEqual(number_to_name(1), "spock")
        self.assertEqual(number_to_name(2), "paper")
        self.assertEqual(number_to_name(3), "lizard")
        self.assertEqual(number_to_name(4), "scissors")
        self.assertEqual(number_to_name(6), None)

    def test_random_number(self):
        success_list = []
        for i in range(100):
            random_number = get_random_number()
            for i in [0, 1, 2, 3, 4]:
                if (random_number == i) and (i not in success_list):
                    success_list.append(i)
        success_list.sort() # Just for convenience when doing manual debugging.
        self.assertTrue(0 in success_list)
        self.assertTrue(1 in success_list)
        self.assertTrue(2 in success_list)
        self.assertTrue(3 in success_list)
        self.assertTrue(4 in success_list)
        self.assertFalse(6 in success_list)

    def test_correct_input(self):
        draw = "Draw!"
        computer_wins = "Computer wins!"
        player_wins = "Player wins!"
        expected_list = [
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player = "scissors",
                                                                                    computer = "paper",
                                                                                    result=player_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player = "scissors",
                                                                computer = "rock",
                                                                result = computer_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player = "scissors",
                                                                computer = "lizard",
                                                                result = player_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player = "scissors",
                                                                computer = "spock",
                                                                result = computer_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player = "scissors",
                                                                computer = "scissors",
                                                                result = draw),
            ##
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="paper",
                                                                                    computer="rock",
                                                                                    result=player_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="paper",
                                                                                    computer="lizard",
                                                                                    result=computer_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="paper",
                                                                                    computer="spock",
                                                                                    result=player_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="paper",
                                                                                    computer="scissors",
                                                                                    result=computer_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="paper",
                                                                                    computer="paper",
                                                                                    result=draw),
            ##
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="rock",
                                                                                    computer="lizard",
                                                                                    result=player_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="rock",
                                                                                    computer="spock",
                                                                                    result=computer_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="rock",
                                                                                    computer="scissors",
                                                                                    result=player_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="rock",
                                                                                    computer="paper",
                                                                                    result=computer_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="rock",
                                                                                    computer="rock",
                                                                                    result=draw),
            ##
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="lizard",
                                                                                    computer="spock",
                                                                                    result=player_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="lizard",
                                                                                    computer="scissors",
                                                                                    result=computer_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="lizard",
                                                                                    computer="paper",
                                                                                    result=player_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="lizard",
                                                                                    computer="rock",
                                                                                    result=computer_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="lizard",
                                                                                    computer="lizard",
                                                                                    result=draw),
            ##
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="spock",
                                                                                    computer="scissors",
                                                                                    result=player_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="spock",
                                                                                    computer="paper",
                                                                                    result=computer_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="spock",
                                                                                    computer="rock",
                                                                                    result=player_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="spock",
                                                                                    computer="lizard",
                                                                                    result=computer_wins),
            "Player chooses {player}\nComputer chooses {computer}\n{result}".format(player="spock",
                                                                                    computer="spock",
                                                                                    result=draw),
        ]
        actual_list = []
        player_names = ["scissors", "paper", "rock", "lizard", "spock"]
        for player_name in player_names:
            for i in range(1000):
                result = rpsls(player_name)
                if result not in actual_list:
                    actual_list.append(result)
        expected_set = set(expected_list)
        actual_set = set(actual_list)
        self.assertEqual(expected_set.difference(actual_set), set([]))

    def test_incorrect_input(self):
        # Incorrect choice.
        self.assertEqual(rpsls("abracadabra"), "Input a correct choice!")