import importlib


class Simulation:
    def __init__(self) -> None:
        self.__agents = dict()

    def import_agent(self, name, module):
        self.__agents[name] = importlib.import_module(module)()


if __name__ == "__main__":
    sim = Simulation()
    sim.import_agent("hachess.agents._template.Agent")
