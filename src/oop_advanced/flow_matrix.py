from entity import Supplier, Customer


class FlowMatrix:
    """
    Stores all Flow objects and provides access to flow by Supplier and Customer.
    Allows adding/modifying flows. Uses nested dict for efficient conversion to nested lists.
    Maintains __supplier_names and __customer_names for easy conversion.
    """
    def __init__(self) -> None:
        # Nested dict: supplier_name -> customer_name -> quantity
        self.__flows: dict[str, dict[str, float]] = {}
        self.__supplier_names: set[str] = set()
        self.__customer_names: set[str] = set()

    def add_flow(self, supplier: Supplier, customer: Customer, quantity: float) -> None:
    
        # Add the flow to flow dictionary
        if supplier.name not in self.__flows:
            self.__flows[supplier.name] = {}            
        self.__flows[supplier.name][customer.name] = quantity

        # Store the supplier name and the customer name
        self.__supplier_names.add(supplier.name)
        self.__customer_names.add(customer.name)

    def get_flow(self, supplier: Supplier, customer: Customer) -> float:
        return self.__flows[supplier.name][customer.name]

    def to_matrix(self) -> list[list[float]]:

        ordered_supplier_names = sorted(self.__supplier_names)
        ordered_customer_names = sorted(self.__customer_names)

        matrix = []
        for s in ordered_supplier_names:
            row = []
            for c in ordered_customer_names:
                row.append(self.__flows[s][c])
            matrix.append(row)

        return matrix
    
    @property
    def supplier_names(self) -> list[str]:
        sorted_supplier_names = sorted(self.__supplier_names)
        return sorted_supplier_names

    @property
    def customer_names(self) -> list[str]:
        sorted_customer_names = sorted(self.__customer_names)
        return sorted_customer_names
    
    def __getitem__(self, key):
        supplier, customer = key
        return self.__flows[supplier.name][customer.name]

    def __setitem__(self, key, value):
        supplier, customer = key
        self.add_flow(supplier, customer, value)
