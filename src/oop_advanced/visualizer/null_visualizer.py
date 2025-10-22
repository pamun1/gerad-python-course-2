from problem_data import ProblemData
from flow_matrix import FlowMatrix
from visualizer import Visualizer


class NullVisualizer(Visualizer):
    
    def visualize_supply(self, data: ProblemData) -> None:        
        pass

    def visualize_demand(self, data: ProblemData) -> None:
        pass

    def visualize_flows(self, flows: FlowMatrix) -> None:
        pass