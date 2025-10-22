from abc import ABC, abstractmethod
from problem_data import ProblemData
from flow_matrix import FlowMatrix


class Solver(ABC):
    """
    Abstract base solver for the transportation problem.

    Subclasses must implement solve().
    """

    @abstractmethod
    def solve(self, data: ProblemData) -> FlowMatrix:
        """Run the algorithm."""
        pass
