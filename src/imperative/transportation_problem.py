from data import read_from_csv
from greedy_solver import greedy_solve
from pyomo_solver import pyomo_solve
from visualization import plot_demand, plot_supply, plot_flows

def solve_transportation_problem(supply_file: str, demand_file: str, 
                                 costs_file: str, method: str) -> None:

    supply = read_from_csv(supply_file, "supplier", "supply")
    demand = read_from_csv(demand_file, "customer", "demand")
    costs = read_from_csv(costs_file, ["supplier", "customer"], "cost")

    plot_supply(supply)
    plot_demand(demand)

    flows = {}
    if method == "greedy":
        flows = greedy_solve(supply, demand, costs)
    elif method == "pyomo":
        flows = pyomo_solve(supply, demand, costs)

    plot_flows(flows, supply, demand)

    return flows
