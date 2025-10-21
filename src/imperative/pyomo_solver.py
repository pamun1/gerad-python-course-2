from pyomo.environ import *
from greedy_solver import CostDict, FlowDict


def pyomo_solve(
        supply_by_sup: dict[str, float],
        demand_by_cust: dict[str, float],
        cost_by_sup_cust: CostDict,
        solver_name: str = "cbc"
        ) -> FlowDict:

    # Defining the model
    model = ConcreteModel()

    # Defining the sets
    model.S = Set(initialize=supply_by_sup.keys())
    model.C = Set(initialize=demand_by_cust.keys())

    # Defining the variables
    model.x = Var(model.S, model.C, domain=NonNegativeReals)

    # Defining the objective function
    model.obj = Objective(expr=sum(cost_by_sup_cust[(i,j)] * model .x[i, j]
                                   for i in model.S 
                                   for j in model.C), 
                          sense=minimize)

    # Defining the constraints
    model.sup_const = Constraint(
        model.S, 
        rule=lambda m, i: sum(m.x[i, j] 
                            for j in m.C) <= supply_by_sup[i])

    model.dem_const = Constraint(
        model.C, 
        rule=lambda m, j: sum(m.x[i, j] 
                            for i in m.S) >= demand_by_cust[j]
    )

    # Configuring the solver
    solver = SolverFactory(solver_name)

    # Solving the model
    solver.solve(model)

    # Extracting the results
    flow_by_sup_cust: FlowDict = {}
    for i in model.S:
        for j in model.C:
            flow_by_sup_cust[(i, j)] = value(model.x[i, j])

    return flow_by_sup_cust
    