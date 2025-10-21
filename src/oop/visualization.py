from typing import Optional
import matplotlib.pyplot as plt

from problem_data import ProblemData
from solver import FlowDict


def plot_supply(data: ProblemData):
    supply_list = []
    for supplier in data.suppliers:
        supply_list.append(supplier.supply)    
    plt.bar(data.supplier_names, supply_list, color="orange", label="Supply")
    plt.xlabel("Supplier")
    plt.ylabel("Units")
    plt.title("Supply")
    plt.legend()
    plt.show()


def plot_demand(data: ProblemData):
    demand_list = []
    for customer in data.customers:
        demand_list.append(customer.demand) 
    plt.bar(data.customer_names, demand_list, color="blue",
            label="Demand")
    plt.xlabel("Customer")
    plt.ylabel("Units")
    plt.title("Demand")
    plt.legend()
    plt.show()


def plot_flows(data: ProblemData, flow_by_sup_cust: FlowDict):

    flows_matrix = flow_dict_to_matrix(data, flow_by_sup_cust)

    plt.imshow(flows_matrix)
    plt.colorbar(label="Units shipped")
    plt.title("Shipment Flows")
    plt.xticks(ticks=range(data.nb_customers), labels=list(data.customer_names))
    plt.yticks(ticks=range(data.nb_suppliers), labels=list(data.supplier_names))    
    plt.show()


def flow_dict_to_matrix(data: ProblemData, flows: FlowDict) -> list[list[float]]:

    matrix = []
    for s in data.supplier_names:
        row = []
        for c in data.customer_names:
            row.append(flows[s, c])
        matrix.append(row)

    return matrix