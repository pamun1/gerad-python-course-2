from solver.greedy_solver import GreedySolver
from solver.pyomo_solver import PyomoSolver
from visualizer.plot_visualizer import PlotVisualizer
from transportation_problem import TransportationProblem


supply_file = "data/supply_medium.csv"
demand_file = "data/demand_medium.csv"
costs_file = "data/costs_medium.csv"

tp1 = TransportationProblem(supply_file, demand_file, costs_file, GreedySolver(), PlotVisualizer())
flows_greedy = tp1.solve()

tp2 = TransportationProblem(supply_file, demand_file, costs_file, PyomoSolver("cbc"), PlotVisualizer())
flows_pyomo = tp2.solve()
