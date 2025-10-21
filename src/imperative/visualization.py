import matplotlib.pyplot as plt
from greedy_solver import FlowDict


def plot_supply(supply_by_sup: dict[str, float]):
    plt.bar(supply_by_sup.keys(), supply_by_sup.values(), color="orange", 
            label="Supply")
    plt.xlabel("Supplier")
    plt.ylabel("Units")
    plt.title("Supply")
    plt.legend()
    plt.show()

def plot_demand(demand_by_cust: dict[str, float]):
    plt.bar(demand_by_cust.keys(), demand_by_cust.values(), color="blue",
            label="Demand")
    plt.xlabel("Customer")
    plt.ylabel("Units")
    plt.title("Demand")
    plt.legend()
    plt.show()    

def plot_flows(flow_by_sup_cust: FlowDict, supply_by_sup: dict[str, float], 
               demand_by_cust: dict[str, float]):

    flows_matrix = flow_dict_to_matrix(flow_by_sup_cust, supply_by_sup, demand_by_cust)

    plt.imshow(flows_matrix)
    plt.colorbar(label="Units shipped")
    plt.title("Shipment Flows")
    plt.xticks(ticks=range(len(demand_by_cust)), labels=list(demand_by_cust.keys()))
    plt.yticks(ticks=range(len(supply_by_sup)), labels=list(supply_by_sup.keys()))
    plt.show()


def flow_dict_to_matrix(flow_by_sup_cust: FlowDict, supply_by_sup: dict[str, float],
                        demand_by_cust: dict[str, float]) -> list[list[float]]:

    matrix = []
    for s in supply_by_sup.keys():
        row = []
        for c in demand_by_cust.keys():
            row.append(flow_by_sup_cust[s, c])
        matrix.append(row)

    return matrix