from solver.solver import Solver
from problem_data import ProblemData
from flow_matrix import FlowMatrix


class GreedySolver(Solver):
    """
    Implements a greedy heuristic for the transportation problem.
    
    This class overrides the `solve` method from the `Solver` base class.
    """
    def __init__(self):
        pass

    def solve(self, data: ProblemData) -> FlowMatrix:
        
        flow_matrix = FlowMatrix()

        sorted_costs = sorted(data.costs)

        for cost_obj in sorted_costs:

            supplier = cost_obj.supplier
            customer = cost_obj.customer

            quantity = min(supplier.remaining_supply, customer.remaining_demand)

            flow_matrix[supplier, customer] = quantity
            
            supplier.remaining_supply -= quantity
            customer.remaining_demand -= quantity

        return flow_matrix
    