CostDict = dict[tuple[str, str], float]
FlowDict = dict[tuple[str, str], float]


def greedy_solve(
        supply_by_sup: dict[str, float],
        demand_by_cust: dict[str, float],
        cost_by_sup_cust: CostDict
        ) -> FlowDict:

    flow_by_sup_cust: FlowDict = {}

    # Copy the dictionaries to prevent their modification
    rem_supply_by_sup = supply_by_sup.copy()
    rem_demand_by_cust = demand_by_cust.copy()

    # A lambda expression could also be used:
    sorted_costs = sorted(cost_by_sup_cust.items(), key=lambda x: x[1])

    for (s, c), cost in sorted_costs:

        supply = rem_supply_by_sup[s]
        demand = rem_demand_by_cust[c]

        quantity = min(supply, demand)

        flow_by_sup_cust[(s, c)] = quantity
        
        rem_supply_by_sup[s] -= quantity
        rem_demand_by_cust[c] -= quantity

    return flow_by_sup_cust