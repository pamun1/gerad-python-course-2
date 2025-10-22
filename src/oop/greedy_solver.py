from solver import Solver, FlowDict
from problem_data import ProblemData


class GreedySolver(Solver):
    """
    Implements a greedy heuristic for the transportation problem.
    
    This class overrides the `solve` method from the `Solver` base class.
    """
    def __init__(self):
        pass

    def solve(self, data: ProblemData) -> FlowDict:
        
        flow_by_sup_cust: FlowDict = {}

        sorted_costs = sorted(data.costs, key=lambda x: x.value)

        for cost_obj in sorted_costs:

            supplier = cost_obj.supplier
            customer = cost_obj.customer

            quantity = min(supplier.remaining_supply, customer.remaining_demand)

            flow_by_sup_cust[(supplier.name, customer.name)] = quantity
            
            supplier.remaining_supply -= quantity
            customer.remaining_demand -= quantity

        return flow_by_sup_cust
    
