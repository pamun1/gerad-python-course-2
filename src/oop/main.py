from solver_greedy import GreedySolver
from solver_pyomo import PyomoSolver
from transportation_problem import TransportationProblem


supply_file = "data/supply_medium.csv"
demand_file = "data/demand_medium.csv"
costs_file = "data/costs_medium.csv"

tp1 = TransportationProblem(supply_file, demand_file, costs_file, GreedySolver())
flows_greedy = tp1.solve()

tp2 = TransportationProblem(supply_file, demand_file, costs_file, PyomoSolver("cbc"))
flows_pyomo = tp2.solve()
