import random
import numpy as np


class Strategy:
    def __init__(self, rounds, is_p1=None):
        self.rounds = rounds
        self.tournament_score = 0
        self.is_p1 = is_p1

    def make_choice(self, rounds_results=None, current_round=None):
        """
        Default behavior for strategies.
        Should be overridden in subclasses.
        """
        raise NotImplementedError()


# 1 for cooperation and 0 for defection
class TitForTat(Strategy):
    name = "TitForTat"
    abbreviation = "TFT"

    def __init__(self, rounds, is_p1):
        super().__init__(rounds, is_p1)

    def make_choice(self, rounds_results=None, current_round=None):
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
        super().__init__(rounds)

    def make_choice(self, rounds_results=None, current_round=None):
        return 0


class Random(Strategy):
    name = "Random"

    def __init__(self, rounds):
        super().__init__(rounds)

    def make_choice(self, rounds_results=None, current_round=None):
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
        opponent_last_choice = rounds_results[1, current_round - 1] if self.is_p1 else rounds_results[0, current_round - 1]
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
            self.probability = retaliation_probability
        else:
            self.probability = 0.9

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
            if opponent_last_choice == 0 and current_round != self.rounds-1:
                self.rounds_to_defect[[current_round, current_round+1]] = [True, True]

        else:
            opponent_last_choice = rounds_results[0, current_round - 1]
            if opponent_last_choice == 0:
                self.rounds_to_defect[[current_round, current_round + 1]] = [True, True]

        return 0 if self.rounds_to_defect[current_round] else 1
