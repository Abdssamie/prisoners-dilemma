import numpy as np
from tqdm import tqdm
from strategies import TitForTat, Random
import math


class Simulation:
    payoffs_symbols = ["R", "S", "T", "P"]
    payoff_matrix = [3, 5, 5, 1]
    payoffs = dict(zip(payoffs_symbols, payoff_matrix))

    def __init__(self, players, rounds,):
        self.players = self.recruit_strategies(players)
        self.rounds = rounds
        self.players_count = len(self.players)
        self.players_scores = np.zeros((self.players_count,), dtype=int)
        self.games_count = math.comb(self.players_count, 2)
        self.games_board = np.zeros((self.games_count, 2, rounds))

    def recruit_strategies(self, players):
        strategies_names = players
        strategies_objects = [0 for i in range(self.players_count)]
        strategies_ready = dict(zip(strategies_names, strategies_objects))

        for strategy in strategies_names:
            continue
        # TODO: TO COMPLETE

    def start_simulation(self):
        for game in self.games_board:
            continue
        # TODO: To complete


class Game:
    payoffs_symbols = ["R", "S", "T", "P"]
    payoff_matrix = [3, 0, 5, 1]
    payoffs = dict(zip(payoffs_symbols, payoff_matrix))

    def __init__(self, player_1, player_2, rounds):
        self.player_1 = player_1
        self.player_2 = player_2
        self.rounds = rounds
        self.p1_score = 0
        self.p2_score = 0
        self.p1_scores = np.zeros(self.rounds, dtype=int)
        self.p2_scores = np.zeros(self.rounds, dtype=int)
        self.p1_strat_name = self.player_1.name
        self.p2_strat_name = self.player_2.name
        self.winner = None

    def start_game(self):
        rounds_results = np.zeros((2, self.rounds,), dtype=int)

        print(f"Starting game. {self.player_1.name} vs {self.player_2.name} for {self.rounds} rounds")
        for index in tqdm(range(self.rounds),
                          desc="Running game: {}"):
            player_1_choice = self.player_1.make_choice(rounds_results=rounds_results, current_round=index)
            player_2_choice = self.player_2.make_choice(rounds_results=rounds_results, current_round=index)
            rounds_results[:, index] = [player_1_choice, player_2_choice]

            if player_1_choice == 1 == player_2_choice:
                self.p1_scores[index], self.p2_scores[index] = self.payoffs["R"], self.payoffs["R"]

            elif player_1_choice == 0 == player_2_choice:
                self.p1_scores[index], self.p2_scores[index] = self.payoffs["P"], self.payoffs["P"]

            elif player_1_choice == 1 and 0 == player_2_choice:
                self.p1_scores[index], self.p2_scores[index] = self.payoffs["S"], self.payoffs["T"]

            else:
                self.p1_scores[index], self.p2_scores[index] = self.payoffs["T"], self.payoffs["S"]

        self.p1_score = self.p1_scores.sum()
        self.p2_score = self.p2_scores.sum()

        if self.p1_score > self.p2_score:
            winner = self.p1_strat_name
            print(
                f"Player 1  with strategy {winner} has one with a final score of {self.p1_score},"
                f" and a scoring board: \n{self.p1_scores}\n"
                f"While Player 2 with strategy{self.p2_strat_name} lost with a score of {self.p2_score},"
                f" and a scoring board: \n{self.p2_scores}")
        elif self.p1_score < self.p2_score:
            winner = self.p2_strat_name
            print(
                f"Player 2  with strategy {winner} has one with a final score of {self.p2_score},"
                f" and a scoring board: \n{self.p2_scores}\n"
                f"While Player 1 with strategy{self.p1_strat_name} lost with a score of {self.p1_score},"
                f" and a scoring board: \n{self.p1_scores}")
        else:
            print("It's a draw!")


number_of_rounds = 9999
TFT_player = TitForTat(rounds=number_of_rounds, is_p1=True)
random_strategy_player = Random(rounds=number_of_rounds)
test_game = Game(player_1=TFT_player, player_2=random_strategy_player, rounds=number_of_rounds)
test_game.start_game()


