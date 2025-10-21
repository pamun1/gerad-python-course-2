from entity import Supplier, Customer

class Cost:    
    def __init__(self, supplier: Supplier, customer: Customer, 
                 value: float) -> None:
        self.__supplier = supplier
        self.__customer = customer
        self.__value = value

    @property
    def supplier(self) -> Supplier:
        return self.__supplier
    
    @property
    def customer(self) -> Customer:
        return self.__customer
    
    @property
    def value(self) -> float:
        return self.__value

    def __repr__(self):
        return (f"Cost(supplier={self.supplier!r}, customer={self.customer!r}, value={self.value!r})")

    def __str__(self):
        return f"Cost({self.supplier.name} -> {self.customer.name}: {self.value})"
