from abc import ABC, abstractmethod

from flow_matrix import FlowMatrix
from problem_data import ProblemData


class Visualizer(ABC):
    """
    Abstract base visualizer for the transportation problem.
    Subclasses must implement:     
     - visualize_supply()
     - visualize_demand()
     - visualize_flows()
    """

    @abstractmethod
    def visualize_supply(self, data: ProblemData) -> None:
        """Visualize suppliers' supply."""
        pass

    @abstractmethod
    def visualize_demand(self, data: ProblemData) -> None:
        """Visualize customers' demand."""
        pass

    @abstractmethod
    def visualize_flows(self, flows: FlowMatrix) -> None:
        """Visualize the flows."""
        pass

