from solver import Solver, FlowDict
from problem_data import ProblemData
from visualization import plot_demand, plot_supply, plot_flows


class TransportationProblem:
    def __init__(self, supply_file: str, demand_file: str, costs_file: str, 
                 solver: Solver):
        
        self.__data = ProblemData.from_csvs(supply_file, demand_file, costs_file)
        self.__solver = solver

    def solve(self) -> FlowDict:

        plot_supply(self.__data)
        plot_demand(self.__data)        
        flows = self.__solver.solve(self.__data)
        plot_flows(self.__data, flows)

        return flows