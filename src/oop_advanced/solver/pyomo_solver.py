from solver.solver import Solver
from problem_data import ProblemData
from flow_matrix import FlowMatrix
from pyomo.environ import *


class PyomoSolver(Solver):
    """
    Implements an optimization-based solver for the transportation problem using Pyomo.

    This class overrides the `solve` method from the `Solver` base class.
    """
    def __init__(self, solver_name: str):
        self.__solver_name = solver_name

    def solve(self, data: ProblemData) -> FlowMatrix:

        # Defining the model
        model = ConcreteModel()

        # Defining the sets
        model.S = Set(initialize=[supplier.name for supplier in data.suppliers])
        model.C = Set(initialize=[customer.name for customer in data.customers])

        # Defining the variables
        model.x = Var(model.S, model.C, domain=NonNegativeReals)

        # Defining the objective function
        model.obj = Objective(expr=sum(data[i, j].value * model.x[i,j]
                                       for i in model.S 
                                       for j in model.C), 
                              sense=minimize)

        # Defining the constraints
        model.sup_const = Constraint(
            model.S, 
            rule=lambda m, i: sum(m.x[i, j] 
                                for j in m.C) <= data.get_supplier(i).supply)

        model.dem_const = Constraint(
            model.C, 
            rule=lambda m, j: sum(m.x[i, j] 
                                for i in m.S) >= data.get_customer(j).demand)

        # Configuring the solver
        solver = SolverFactory(self.__solver_name)

        # Solving the model
        solver.solve(model)

        # Extracting the results
        flows = FlowMatrix()
        for i in model.S:
            for j in model.C:
                quantity = value(model.x[i, j])
                supplier = data.get_supplier(i)
                customer = data.get_customer(j)
                supplier.remaining_supply -= quantity
                customer.remaining_demand -= quantity
                flows[supplier, customer] = quantity

        return flows
    