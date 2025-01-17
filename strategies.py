import random
import numpy as np


class Strategy:
    """
    Base class for implementing prisoner's dilemma strategies.

    This class provides a template for creating specific strategy implementations.
    It should be subclassed to create concrete strategies.
    """

    def __init__(self, rounds, is_p1=None):
        """
        Initialize a new Strategy instance.

        Parameters:
        rounds (int): The total number of rounds in the game.
        is_p1 (bool, optional): Indicates whether this strategy is for player 1. Defaults to None.
        """
        self.rounds = rounds
        self.tournament_score = 0
        self.is_p1 = is_p1
        self.payoff_dict = {
            (0, 1): 0,  # Player 0 defects, Player 1 cooperates -> S = 0
            (0, 0): 1,  # Both defect -> P = 1
            (1, 0): 5,  # Player 0 cooperates, Player 1 defects -> T = 5
            (1, 1): 3  # Both cooperate -> R = 3
        }

    def make_choice(self, rounds_results=None, current_round=None):
        """
        Make a choice for the current round of the game.

        This method should be overridden in subclasses to implement specific strategies.

        Parameters:
        rounds_results (numpy.ndarray, optional): A 2D array containing the results of previous rounds.
            Shape is (2, num_rounds), where rounds_results[0] contains player 1's choices
            and rounds_results[1] contains player 2's choices. Defaults to None.
        current_round (int, optional): The current round number (0-indexed). Defaults to None.

        Returns:
        int: The choice made by the strategy (1 for cooperate, 0 for defect).

        Raises:
        NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError()


# 1 for cooperation and 0 for defection
class TitForTat(Strategy):
    """
    Implements the Tit for Tat strategy in the Prisoner's Dilemma game.

    This strategy cooperates on the first move and then replicates the opponent's previous move.
    """

    name = "TitForTat"
    abbreviation = "TFT"

    def __init__(self, rounds, is_p1):
        """
        Initialize a new TitForTat strategy instance.

        Parameters:
        rounds (int): The total number of rounds in the game.
        is_p1 (bool): Indicates whether this strategy is for player 1 (True) or player 2 (False).
        """
        super().__init__(rounds, is_p1)

    def make_choice(self, rounds_results=None, current_round=None):
        """
        Make a choice for the current round based on the Tit for Tat strategy.

        Parameters:
        rounds_results (numpy.ndarray, optional): A 2D array containing the results of previous rounds.
            Shape is (2, num_rounds), where rounds_results[0] contains player 1's choices
            and rounds_results[1] contains player 2's choices. Defaults to None.
        current_round (int, optional): The current round number (0-indexed). Defaults to None.

        Returns:
        int: The choice made by the strategy (1 for cooperate, 0 for defect).
        """
        if current_round == 0:
            return 1
        if self.is_p1:
            opponent_last_choice = rounds_results[1, current_round - 1]
        else:
            opponent_last_choice = rounds_results[0, current_round - 1]

        return 1 if opponent_last_choice == 1 else 0


class CooperateUnconditionally(Strategy):
    name = "Cooperate Unconditionally"
    abbreviation = "CU"

    def __init__(self, rounds):
        super().__init__(rounds)

    def make_choice(self, rounds_results=None, current_round=None):
        return 1


class DefectUnconditionally(Strategy):
    name = "Defect Unconditionally"
    abbreviation = "DU"

    def __init__(self, rounds):
        """
        Initialize a new DefectUnconditionally strategy instance.

        Parameters:
        rounds (int): The total number of rounds in the game.
        """
        super().__init__(rounds)

    def make_choice(self, rounds_results=None, current_round=None):
        """
        Make a choice for the current round based on the Defect Unconditionally strategy.

        Parameters:
        rounds_results (numpy.ndarray, optional): A 2D array containing the results of previous rounds.
            Shape is (2, num_rounds), where rounds_results[0] contains player 1's choices
            and rounds_results[1] contains player 2's choices. Defaults to None.
        current_round (int, optional): The current round number (0-indexed). Defaults to None.

        Returns:
        int: The choice made by the strategy, which is always 0 (defect).
        """
        return 0


class Random(Strategy):
    name = "Random"

    def __init__(self, rounds):
        super().__init__(rounds)

    def make_choice(self, rounds_results=None, current_round=None):
        """
        Make a random choice for the current round in the Prisoner's Dilemma game.

        This strategy randomly chooses between cooperation (1) and defection (0) 
        with equal probability, regardless of previous rounds' results.

        Parameters:
        rounds_results (numpy.ndarray, optional): A 2D array containing the results of previous rounds.
            Shape is (2, num_rounds), where rounds_results[0] contains player 1's choices
            and rounds_results[1] contains player 2's choices. Defaults to None.
        current_round (int, optional): The current round number (0-indexed). Defaults to None.

        Returns:
        int: The choice made by the strategy (1 for cooperate, 0 for defect).
        """
        return random.choice((1, 0))


class ProbabilityCooperator(Strategy):
    name = "Probability Cooperator"
    abbreviation = "PC"

    def __init__(self, rounds, probability=0.6):
        super().__init__(rounds)
        self.probability = probability

    def make_choice(self, rounds_results=None, current_round=None):
        return 1 if random.random() < 0.6 else 0


class TitForTwoTats(Strategy):
    name = "Tit For Two Tats"
    abbreviation = "TFTT"

    def __init__(self, rounds, is_p1):
        super().__init__(rounds, is_p1)

    def make_choice(self, rounds_results=None, current_round=None):
        """
                :param rounds_results: the previous round results
                :param current_round: number of the current round (based on 0)
                :return: choice;
                """

        # making choice for first round
        if current_round == 0:
            choice = 1

        elif current_round == 1:
            opponent_last_choice = rounds_results[1, current_round - 1] if self.is_p1 \
                else rounds_results[0, current_round - 1]
            if opponent_last_choice == 1:
                choice = 1
            else:
                choice = 0

        else:
            opponents_previous_two_choices = list(rounds_results[1, [current_round-2, current_round-1]]) if self.is_p1 \
                else list(rounds_results[0, [current_round-2, current_round-1]])
            if opponents_previous_two_choices == [0, 0]:
                choice = 0
            else:
                choice = 1

        return choice


class GrimTrigger(Strategy):
    name = "Grim Trigger"
    abbreviation = "GT"

    def __init__(self, rounds):
        super().__init__(rounds)
        self.triggered = False

    def make_choice(self, rounds_results=None, current_round=None):
        if self.triggered:
            return 0  # After the first defection, always defect
        if current_round == 0:
            return 1  # First round, cooperate
        # Check if the opponent defected in the previous round
        opponent_last_choice = rounds_results[1, current_round-1] if self.is_p1 else rounds_results[0, current_round-1]
        if opponent_last_choice == 0:
            self.triggered = True  # Trigger defection after opponent defects
            return 0
        return 1  # Otherwise, cooperate


class TitForTatWithForgiveness(Strategy):
    name = "TitForTatWithForgiveness"
    abbreviation = "TFTF"

    def __init__(self, rounds, is_p1):
        super().__init__(rounds, is_p1)

    def make_choice(self, rounds_results=None, current_round=None):
        # In the first round, cooperate
        if current_round == 0:
            return 1

        # Check opponent's last choice
        opponent_last_choice = rounds_results[1, current_round - 1] if self.is_p1 else rounds_results[
            0, current_round - 1]

        # Forgive if the opponent defected once
        if opponent_last_choice == 0:
            if random.random() < 0.5:  # 50% chance to forgive
                return 1  # Forgive and cooperate
            else:
                return 0  # Defect
        return 1  # Cooperate if the opponent cooperated in the last round


class SuspiciousTitForTat(Strategy):
    name = "SuspiciousTitForTat"
    abbreviation = "STFT"

    def __init__(self, rounds, is_p1):
        super().__init__(rounds, is_p1)

    def make_choice(self, rounds_results=None, current_round=None):
        if current_round == 0:
            return 0
        if self.is_p1:
            opponent_last_choice = rounds_results[1, current_round - 1]
        else:
            opponent_last_choice = rounds_results[0, current_round - 1]

        return 1 if opponent_last_choice == 1 else 0


class ImperfectTitForTat(Strategy):
    name = "ImperfectTitForTat"
    abbreviation = "ITFT"

    def __init__(self, rounds, is_p1, retaliation_probability):
        super().__init__(rounds, is_p1)
        if retaliation_probability <= 0 or retaliation_probability >= 1:
            self.probability = 0.9
        else:
            self.probability = retaliation_probability

    def make_choice(self, rounds_results=None, current_round=None):
        if current_round == 0:
            return 1

        if self.is_p1:
            opponent_last_choice = rounds_results[1, current_round - 1]
        else:
            opponent_last_choice = rounds_results[0, current_round - 1]

        if opponent_last_choice == 1:
            return 1 if random.random() <= 0.9 else 0

        return 0 if random.random() <= 0.9 else 1


class TwoTitsForTat(Strategy):
    name = "TwoTitsForTat"
    abbreviation = "TTFT"

    def __init__(self, rounds, is_p1):
        super().__init__(rounds, is_p1)
        self.rounds_to_defect = np.zeros(rounds, dtype=bool)

    def make_choice(self, rounds_results=None, current_round=None):
        if current_round == 0:
            return 1

        if self.is_p1:
            opponent_last_choice = rounds_results[1, current_round - 1]
            if opponent_last_choice == 0 and current_round != self.rounds - 1:
                self.rounds_to_defect[[current_round, current_round + 1]] = [True, True]

        else:
            opponent_last_choice = rounds_results[0, current_round - 1]
            if opponent_last_choice == 0:
                self.rounds_to_defect[[current_round, current_round + 1]] = [True, True]

        return 0 if self.rounds_to_defect[current_round] else 1


class Pavlov(Strategy):
    name = "Pavlov"
    abbreviation = "WSLS"

    def __init__(self, is_p1):
        super().__init__(self, is_p1)

    def make_choice(self, rounds_results=None, current_round=None):
        if current_round == 0:
            return 1 if random.random() < 0.5 else 0

        if self.is_p1:
            opponent_last_choice = rounds_results[1, current_round - 1]
            strategy_last_choice = rounds_results[0, current_round - 1]
        else:
            opponent_last_choice = rounds_results[0, current_round - 1]
            strategy_last_choice = rounds_results[1, current_round - 1]

        if opponent_last_choice == strategy_last_choice:
            return 1
        else:
            return 0


class MemoryOne(Strategy):
    name = "Memory-one"
    abbreviation = "S(p,q,r,s)"
    """
    Implements a Memory-one strategy in the Prisoner's Dilemma game.

    This strategy cooperates with probabilities p, q, r, or s
    after outcomes (C,C), (C,D), (D,C), or (D,D) respectively.
    """

    def __init__(self, rounds, is_p1, p, q, r, s):
        """
        Initialize a new Memory-one strategy instance.

        Parameters:
        rounds (int): The total number of rounds in the game.
        is_p1 (bool): Indicates whether this strategy is for player 1 (True) or player 2 (False).
        p (float): Probability of cooperating after (C,C) outcome.
        q (float): Probability of cooperating after (C,D) outcome.
        r (float): Probability of cooperating after (D,C) outcome.
        s (float): Probability of cooperating after (D,D) outcome.
        """
        super().__init__(rounds, is_p1)
        self.rounds_to_defect = np.zeros(rounds, dtype=bool)

        self.p = p if self.is_valid_proba(p) else 0.8
        self.q = q if self.is_valid_proba(q) else 0.4
        self.r = r if self.is_valid_proba(r) else 0.7
        self.s = s if self.is_valid_proba(s) else 0.5

    @staticmethod
    def is_valid_proba(probability):
        """
        Check if a given probability is valid (between 0 and 1, inclusive).

        Parameters:
        probability (float): The probability to check.

        Returns:
        bool: True if the probability is valid, False otherwise.
        """
        return 0 <= probability <= 1

    def make_choice(self, rounds_results=None, current_round=None):
        """
        Make a choice for the current round based on the Memory-one strategy.

        Parameters:
        rounds_results (numpy.ndarray, optional): A 2D array containing the results of previous rounds.
            Shape is (2, num_rounds), where rounds_results[0] contains player 1's choices
            and rounds_results[1] contains player 2's choices. Defaults to None.
        current_round (int, optional): The current round number (0-indexed). Defaults to None.

        Returns:
        int: The choice made by the strategy (1 for cooperate, 0 for defect).
        """
        if current_round == 0:
            return 1 if random.random() < self.p else 0

        if self.is_p1:
            opponent_last_choice = rounds_results[1, current_round - 1]
            strategy_last_choice = rounds_results[0, current_round - 1]
        else:
            opponent_last_choice = rounds_results[0, current_round - 1]
            strategy_last_choice = rounds_results[1, current_round - 1]

        if opponent_last_choice == 0 and strategy_last_choice == 0:
            return 1 if random.random() < self.p else 0
        elif opponent_last_choice == 0 and strategy_last_choice == 1:
            return 1 if random.random() < self.q else 0
        elif opponent_last_choice == 1 and strategy_last_choice == 0:
            return 1 if random.random() < self.r else 0
        else:
            return 1 if random.random() < self.s else 0


class Reactive(Strategy):
    name = "Reactive"
    abbreviation = "R(y,p,q)"

    def __init__(self, is_p1, y, p, q):
        super().__init__(self, is_p1)
        self.y = y if self.is_valid(y) else 0.55
        self.p = p if self.is_valid(p) else 0.7
        self.q = q if self.is_valid(q) else 0.4

    @staticmethod
    def is_valid(probability):
        return 0 <= probability <= 1

    def make_choice(self, rounds_results=None, current_round=None):
        if current_round == 0:
            return 1 if random.random() < self.y else 0

        if self.is_p1:
            opponent_last_choice = rounds_results[1, current_round - 1]
        else:
            opponent_last_choice = rounds_results[0, current_round - 1]

        if opponent_last_choice == 0:
            return 1 if random.random() < self.p else 0
        else:
            return 1 if random.random() < self.q else 0


class ZeroDeterminant(MemoryOne):
    name = "Zero-determinant"
    abbreviation = "ZD(p,q,r,s)"

    def __init__(self, rounds, is_p1, p, q, r, s):
        super().__init__(rounds, is_p1, p, q, r, s)


class Equalizer(ZeroDeterminant):
    name = "Equalizer"
    abbreviation = "SET-n"

    def __init__(self, rounds, is_p1, p, q, r, s, target):
        super().__init__(rounds, is_p1, p, q, r, s)
        self.target = target

    def find_optimal_choice(self, current_round, counts):
        """
        Let's define this function which measures the difference between the total goal score for the opponent
        in the infinite Prisoner's Dilemma and the current score using t, r, p which respectively stand for number
        times to Temptation, Reward and Punishment to the opponent while s not mentioned in the function, is the number
        of times when the opponent got Sucker result
            f_m (t,r,p) = 5t + 3r + p - mn
        The absolute value of this function should be as close as possible to 0 in each iteration m
        For each iteration there are 4 possible values for the function:

            """

        s, p, t, r = counts
        m = current_round
        n = self.target

        f_m_possibilities = np.array([
            5 * t + 3 * r + p - m * n,
            5 * t + 3 * r + p + 1 - m * n,
            5 * (t + 1) + 3 * r + p - m * n,
            5 * t + 3 * (r + 1) + p - m * n
        ])

        min_index = np.argmin(f_m_possibilities)

        return 0 if min_index == 0 or min_index == 1 else 1

    def make_choice(self, rounds_results=None, current_round=None):

        if current_round == 0:
            return self.find_optimal_choice(1, [0, 0, 0, 0])

        if self.is_p1:
            # Ignore The Warning Here
            opponent_payoffs = [self.payoff_dict[tuple(map(int, list(reversed(round_result))))]
                                for round_result in rounds_results]
        else:
            opponent_payoffs = [self.payoff_dict[tuple(map(int, list(round_result)))]
                                for round_result in rounds_results]

        # Count occurrences of each payoff
        unique_payoffs, counts = np.unique(opponent_payoffs, return_counts=True)

        return self.find_optimal_choice(current_round, counts)
