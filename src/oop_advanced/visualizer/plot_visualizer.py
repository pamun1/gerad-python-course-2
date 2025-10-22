from matplotlib import pyplot as plt
from problem_data import ProblemData
from flow_matrix import FlowMatrix
from visualizer.visualizer import Visualizer


class PlotVisualizer(Visualizer):

    def __init__(self):
        pass
    
    def visualize_supply(self, data: ProblemData) -> None:
        supply_list = [s.supply for s in data.suppliers]
        supplier_names = [s.name for s in data.suppliers]
        plt.bar(supplier_names, supply_list, color="orange", 
                label="Supply")
        plt.xlabel("Supplier")
        plt.ylabel("Units")
        plt.title("Supply")
        plt.legend()
        plt.show()

    def visualize_demand(self, data: ProblemData) -> None:
        demand_list = [c.demand for c in data.customers]
        customer_names = [c.name for c in data.customers]
        plt.bar(customer_names, demand_list, color="blue",
            label="Demand")
        plt.xlabel("Customer")
        plt.ylabel("Units")
        plt.title("Demand")
        plt.legend()
        plt.show()

    def visualize_flows(self, flows: FlowMatrix) -> None:

        flow_matrix = flows.to_matrix()

        plt.imshow(flow_matrix)
        plt.colorbar(label="Units shipped")
        plt.title("Shipment Flows")
        plt.xticks(ticks=range(len(flows.customer_names)), labels=list(flows.customer_names))
        plt.yticks(ticks=range(len(flows.supplier_names)), labels=list(flows.supplier_names))
        plt.show()
