from transportation_problem import solve_transportation_problem


supply_file = "data/supply_medium.csv"
demand_file = "data/demand_medium.csv"
costs_file = "data/costs_medium.csv"

flows_greedy = solve_transportation_problem(supply_file, demand_file, costs_file, "greedy")
flows_pyomo = solve_transportation_problem(supply_file, demand_file, costs_file, "pyomo")
