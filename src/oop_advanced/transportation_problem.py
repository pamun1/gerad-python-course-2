from solver.solver import Solver
from problem_data import ProblemData
from visualizer.plot_visualizer import Visualizer
from flow_matrix import FlowMatrix


class TransportationProblem:
    def __init__(self, supply_file: str, demand_file: str, costs_file: str, 
                 solver: Solver, visualizer: Visualizer):
        
        self.__data = ProblemData.from_csvs(supply_file, demand_file, costs_file)
        self.__solver = solver
        self.__visualizer = visualizer

    def solve(self) -> FlowMatrix:

        self.__visualizer.visualize_supply(self.__data)
        self.__visualizer.visualize_demand(self.__data)        
        flows = self.__solver.solve(self.__data)
        self.__visualizer.visualize_flows(flows)

        return flows