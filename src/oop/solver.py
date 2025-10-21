from abc import ABC, abstractmethod
from problem_data import ProblemData


FlowDict = dict[tuple[str, str], float]


class Solver(ABC):
    """
    Abstract base solver for the transportation problem.

    Subclasses must implement solve().
    """

    @abstractmethod
    def solve(self, data: ProblemData) -> FlowDict:
        """Run the algorithm."""
        pass
