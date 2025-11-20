import csv
import random
from typing import Dict, List, Tuple
from domino import Domino
from chicken_foot_line import ChickenFootLine, LineNode
from random import randrange

class PossibleMove:
    def __init__(self, target_line: ChickenFootLine, domino: Domino) -> None:
        self.target_line = target_line
        self.domino = domino

class ChickenFoot:
    def __init__(self, num_players: int, max_pips: int) -> None:
        self.num_players = num_players
        self.max_pips = max_pips
        self.dominos_dealt: List[List[Domino]] = []
        self.all_lines: List[ChickenFootLine] = []
        self.current_player = 0

    def start_game(self, starting_pips: int, dominos_dealt: List[List[Domino]] = None) -> None:
        if dominos_dealt is not None:
            self.dominos_dealt = dominos_dealt
        else:
            self.dominos_dealt = []

        starting_domino = Domino(starting_pips, starting_pips)
        starting_domino.set_open_value(starting_pips)
        starting_node = LineNode(starting_domino)

        for _ in range(6):
            new_line = ChickenFootLine(starting_node)
            self.all_lines.append(new_line)

    def find_moves(self) -> List[PossibleMove]:
        possible_moves: List[PossibleMove] = []

        for line in self.all_lines:
            first_domino = line.get_first_domino()

            if first_domino.is_double():
                for domino in self.dominos_dealt[self.current_player]:
                    if domino.value[0] == first_domino.open_end or domino.value[1] == first_domino.open_end:
                        move = PossibleMove(line, domino)
                        possible_moves.append(move)
            else:
                for domino in self.dominos_dealt[self.current_player]:
                    if domino.value[0] == first_domino.open_end or domino.value[1] == first_domino.open_end:
                        move = PossibleMove(line, domino)
                        possible_moves.append(move)

        return possible_moves

    def draw_domino(self, domino: Domino = None) -> Domino:
        if domino is None:
            random_value_1 = random.randint(0, self.max_pips)
            random_value_2 = random.randint(0, self.max_pips)
            domino = Domino(random_value_1, random_value_2)

        self.dominos_dealt[self.current_player].append(domino)
        return domino

    def place_domino(self, domino: Domino, place: ChickenFootLine) -> None:
        open_end = place.first.domino.open_end
        domino.set_open_value(open_end)
        place.add(domino)

        if domino.is_double():
            new_node = place.first
            for _ in range(3):
                new_line = ChickenFootLine(new_node)
                self.all_lines.append(new_line)
            self.all_lines.remove(place)

        self.dominos_dealt[self.current_player].remove(domino)

    def end_turn(self) -> None:
        if self.current_player + 1 >= self.num_players:
            self.current_player = 0
        else:
            self.current_player += 1

    def get_ends_of_lines(self) -> List[ChickenFootLine]:
        return self.all_lines

    def calculate_scores(self) -> List[int]:
        scores = []

        for player_hand in self.dominos_dealt:
            score = 0
            for domino in player_hand:
                score += domino.value[0] + domino.value[1]
            scores.append(score)

        return scores