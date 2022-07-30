import chess
import random

from importlib import import_module


class Simulation:
    def __init__(self, verbose: bool = False) -> None:
        """
        A simulation class that allows you to run two chess agents against each other.

        Args:
            verbose (bool, optional): Defaults to False.
        """
        self.verbose = verbose
        self.__init_logs()
        self.__init_score()
        self.__init_agents()

    def __init_logs(self) -> None:
        "Initializes logs dictionary"
        self.__logs = dict()

    def __init_score(self) -> None:
        "Initializes score dictionary"
        self.__score = dict()

    def __init_agents(self) -> None:
        "Initializes agents dictionary"
        self.__agents = dict()

    def import_agent(self, name: str):
        """
        Imports and instantiates an agent.

        Args:
            name (str): the name of the agent (the directory the agent is stored in)
        """
        self.__agents[name] = getattr(
            import_module(f"hachess.agents.{name}.agent"), "Agent"
        )()

    def compete_agents(
        self,
        agent_0: str,
        agent_1: str,
        number_rounds: int,
        move_time: int,
        game_time: int,
    ) -> tuple[float, float]:
        for _ in range(number_rounds):
            results = self.run_game(agent_0, agent_1, move_time, game_time)

    def run_game(self, agent_0: str, agent_1: str, move_time: int, game_time: int):
        if random.random() > 0.5:
            # randomly select white and black roles
            white = self.__agents[agent_0]
            black = self.__agents[agent_1]
            white_agent_number = 0
        else:
            white = self.__agents[agent_1]
            black = self.__agents[agent_0]
            white_agent_number = 1

        board = chess.Board()

        while board.outcome() == None:
            if board.turn:
                # white move
                move = white.decide(board)
            else:
                # black move
                move = black.decide(board)
            try:
                # attempt to
                board.push(move)
            except (ValueError):
                if self.verbose:
                    if board.turn:
                        print(
                            "ERROR: invalid move by agent {}.".format(
                                white_agent_number
                            )
                        )
                        self.log_game("0-1", white_agent_number)
                    else:
                        print(
                            "ERROR: invalid move by agent {}.".format(
                                1 - white_agent_number
                            )
                        )
                        self.log_game("1-0", white_agent_number)

        self.log_game(board.result(), white_agent_number)

    def log_game(self, result, white_agent_number):
        if result == "1-0":
            # white winner
            self.score[white_agent_number] += 1
        elif result == "0-1":
            # black winner
            self.score[1 - white_agent_number] += 1
        else:
            # draw
            self.score[0] += 0.5
            self.score[1] += 0.5

    def run(self, A: str, B: str, games: int, move_time: int, game_time: int) -> None:
        """
        Runs the simulation, given the agent dir names.

        Args:
            A (str): _description_
            B (str): _description_
        """
        # import agents
        self.import_agent(A)
        self.import_agent(B)
        score = self.compete_agents(A, B, games, move_time, game_time)
        self.__logs["score"] = score
        return self.__logs


if __name__ == "__main__":
    sim = Simulation()
