import importlib
import chess
import random

class Simulation:
    def __init__(self,verbose = False) -> None:
        self.__agents = dict()
        self.verbose = verbose
        self.score = [0,0]

    def import_agent(self, name, module):
        self.__agents[name] = importlib.import_module(module)()

    def compete_agents(self,agent_0,agent_1,number_rounds=10,move_time = 3,game_time = 180) -> tuple[float,float]:
        self.score = [0,0]
        for _ in range(number_rounds):
            self.run_game(agent_0,agent_1,move_time,game_time)
        return self.score

    def run_game(self,agent_0,agent_1,move_time,game_time):
        if random.random()>0.5:
            #randomly select white and black roles
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
                #white move
                move = white.decide(board)
            else:
                #black move
                move = black.decide(board)
            try:
                #attempt to 
                board.push_san(move)
            except(ValueError):
                if self.verbose:
                    if board.turn:
                        print("ERROR: invalid move by agent {}.".format(white_agent_number))
                        self.log_game("0-1",white_agent_number)
                    else:
                        print("ERROR: invalid move by agent {}.".format(1-white_agent_number))
                        self.log_game("1-0",white_agent_number)
        self.log_game(board.result(),white_agent_number)
        

    def log_game(self,result,white_agent_number):
        if result=="1-0":
            #white winner
            self.score[white_agent_number]+=1
        if result=="0-1":
            #black winner
            self.score[1-white_agent_number]+=1
        else:
            #draw
            self.score[0]+=0.5
            self.score[1]+=0.5





if __name__ == "__main__":
    sim = Simulation()
    

   