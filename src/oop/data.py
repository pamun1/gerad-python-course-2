import pandas as pd

from cost import Cost
from entity import Supplier, Customer


def get_dict_from_csv(file: str, index: str | list[str], column: str):

    data_df = pd.read_csv(file)
    data_dict = data_df.set_index(index).to_dict()[column]

    return data_dict

def get_costs_from_csvs(supply_path: str, demand_path: str, cost_path: str) -> list[Cost]:
    supply_dict = get_dict_from_csv(supply_path, "supplier", "supply")
    demand_dict = get_dict_from_csv(demand_path, "customer", "demand")
    costs_dict = get_dict_from_csv(cost_path, ["supplier", "customer"], "cost")

    costs = []
    suppliers_by_name = {}
    customers_by_name = {}
    for (sup_name, cust_name), value in costs_dict.items():
        if sup_name not in suppliers_by_name:
            supplier = Supplier(sup_name, supply_dict[sup_name])
            suppliers_by_name[sup_name] = supplier
        else:
            supplier = suppliers_by_name[sup_name]

        if cust_name not in customers_by_name:
            customer = Customer(cust_name, demand_dict[cust_name])
            customers_by_name[cust_name] = customer
        else:
            customer = customers_by_name[cust_name]

        costs.append(Cost(supplier, customer, value))

    return costs

