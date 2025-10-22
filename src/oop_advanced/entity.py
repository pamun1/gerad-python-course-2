class Entity:
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def __repr__(self):
        return f"Entity({self.name!r})"

    def __str__(self):
        return f"Entity {self.name}"
    
    def __add__(self, other: "Entity") -> "Entity":
        # Combine names of two entities
        return Entity(self.name + "|" + other.name)


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
    def remaining_supply(self, value: int | float) -> None:
        if value < 0:
            raise ValueError(f"remaining_supply must be non-negative.")
        self.__remaining_supply = float(value)

    def __repr__(self):
        return f"Supplier({self.name!r}, {self.supply!r}, {self.remaining_supply!r})"

    def __str__(self):
        return f"Supplier {self.name}: {self.remaining_supply} / {self.supply} units"
    
    def __add__(self, other: "Supplier") -> "Supplier":
        # Combine names and supplies of two suppliers
        return Supplier(self.name + "|" + other.name, self.supply + other.supply)
    

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
    def remaining_demand(self, value: int | float) -> None:
        if value < 0:
            raise ValueError(f"remaining_demand must be non-negative.")
        self.__remaining_demand = float(value)

    def __repr__(self):
        return f"Customer({self.name!r}, {self.demand!r}, {self.remaining_demand!r})"

    def __str__(self):
        return f"Customer {self.name}: {self.remaining_demand} / {self.demand} units"
    
    def __add__(self, other: "Customer") -> "Customer":
        # Combine names and supplies of two customers
        return Customer(self.name + "|" + other.name, self.demand + other.demand)
