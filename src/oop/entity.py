class Entity:
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def print(self) -> None:
        print(f"Entity: {self.name}")


class Supplier(Entity):
    def __init__(self, name: str, supply: int | float) -> None:
        super().__init__(name)
        self.__supply = float(supply)
        self.__remaining_supply = float(supply)

    @property
    def supply(self) -> float:
        return self.__supply
    
    @property
    def remaining_supply(self) -> float:
        return self.__remaining_supply
    
    @remaining_supply.setter
    def remaining_supply(self, remaining_supply: float) -> None:
        self.__remaining_supply = remaining_supply

    def print(self) -> None:
        print(f"Supplier: {self.name}, {self.supply}")
    

class Customer(Entity):
    def __init__(self, name: str, demand: int | float) -> None:
        super().__init__(name)
        self.__demand = float(demand)
        self.__remaining_demand = float(demand)

    @property
    def demand(self) -> float:
        return self.__demand
    
    @property
    def remaining_demand(self) -> float:
        return self.__remaining_demand
    
    @remaining_demand.setter
    def remaining_demand(self, remaining_demand: float) -> None:
        self.__remaining_demand = remaining_demand

    def print(self) -> None:
        print(f"Customer: {self.name}, {self.demand}")
