import pandas as pd
from entity import Customer, Supplier
from cost import Cost


class ProblemData:
    def __init__(self, costs: list[Cost]):
        
        self.__suppliers_by_name = {}
        self.__customers_by_name = {}
        self.__cost_by_sup_cust = {}

        for cost in costs:
            self.add_cost(cost)

    @staticmethod
    def get_dict_from_csv(file: str, index: str | list[str], col: str):
        data_df = pd.read_csv(file)
        data_dict = data_df.set_index(index).to_dict()[col]
        return data_dict

    @classmethod
    def from_csvs(cls, supply_path: str, demand_path: str, cost_path: str) -> "ProblemData":
        supply_dict = cls.get_dict_from_csv(supply_path, "supplier", "supply")
        demand_dict = cls.get_dict_from_csv(demand_path, "customer", "demand")
        costs_dict = cls.get_dict_from_csv(cost_path, ["supplier", "customer"], "cost")

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

        return cls(costs)

    def add_cost(self, cost: Cost) -> None:
        self.__suppliers_by_name[cost.supplier.name] = cost.supplier
        self.__customers_by_name[cost.customer.name] = cost.customer
        self.__cost_by_sup_cust[cost.supplier.name, cost.customer.name] = cost

    @property
    def suppliers(self) -> list[Supplier]:
        return list(self.__suppliers_by_name.values())
    
    @property
    def customers(self) -> list[Customer]:
        return list(self.__customers_by_name.values())
    
    @property
    def costs(self) -> list[Cost]:        
        return list(self.__cost_by_sup_cust.values())
    
    @property
    def supplier_names(self) -> list[str]:
        return list(self.__suppliers_by_name.keys())
    
    @property
    def customer_names(self) -> list[str]:
        return list(self.__customers_by_name.keys())
    
    @property
    def nb_suppliers(self) -> int:
        return len(self.__suppliers_by_name)
    
    @property
    def nb_customers(self) -> int:
        return len(self.__customers_by_name)
    
    def get_supplier(self, supplier_name: str) -> Supplier:
        return self.__suppliers_by_name[supplier_name]
    
    def get_customer(self, customer_name: str) -> Customer:
        return self.__customers_by_name[customer_name]

    def get_cost(self, supplier_name: str, customer_name: str) -> Cost:
        return self.__cost_by_sup_cust[supplier_name, customer_name]
