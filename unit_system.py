

TPS = 20

def check_initialisation(value):
        if isinstance(value, Constant) \
            or isinstance(value, Second) \
            or isinstance(value, Tick) \
            or isinstance(value, Production) \
            or isinstance(value, ProductionPerTick) \
            or isinstance(value, Energy) \
            or isinstance(value, EnergyPerTick):

            raise ValueError("wrong type provided : ", type(value))

class Second:
    def __init__(self, value):
        check_initialisation(value)
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, Second):               return Second(self.value + other.value)
        if isinstance(other, Tick):                 return Second(self.value + other.value / TPS)
        raise TypeError("wrong type provided : ", type(other))
    
    def __sub__(self, other):
        if isinstance(other, Second):               return Second(self.value - other.value)
        if isinstance(other, Tick):                 return Second(self.value - other.value / TPS)
        raise TypeError("wrong type provided : ", type(other))
    
    def __mul__(self, other):
        if isinstance(other, ProductionPerTick):    return Production((self.value * TPS) * other.value)
        if isinstance(other, EnergyPerTick):        return Energy((self.value * TPS) * other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __truediv__(self, other):
        if isinstance(other, Tick):                 return Constant((self.value * TPS) / other.value)
        if isinstance(other, Second):               return Constant(self.value / other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __eq__(self, other):
        if isinstance(other, Second):               return self.value == other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __lt__(self, other):
        if isinstance(other, Second):               return self.value < other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __gt__(self, other):
        if isinstance(other, Second):               return self.value > other.value
        raise TypeError("wrong type provided : ", type(other))

class Tick:
    def __init__(self, value):
        check_initialisation(value)
        self.value = value

    def __add__(self, other):
        if isinstance(other, Tick):                 return Tick(self.value + other.value)
        if isinstance(other, Second):               return Tick(self.value + other.value * TPS)
        raise TypeError("wrong type provided : ", type(other))
    
    def __sub__(self, other):
        if isinstance(other, Tick):                 return Tick(self.value - other.value)
        if isinstance(other, Second):               return Tick(self.value - other.value * TPS)
        raise TypeError("wrong type provided : ", type(other))
    
    def __mul__(self, other):
        if isinstance(other, ProductionPerTick):    return Production(self.value * other.value)
        if isinstance(other, EnergyPerTick):        return Energy(self.value * other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __truediv__(self, other):
        if isinstance(other, Tick):                 return Constant(self.value / other.value)
        if isinstance(other, Second):               return Constant(self.value / (other.value * TPS))
        raise TypeError("wrong type provided : ", type(other))
    
    def __eq__(self, other):
        if isinstance(other, Second):               return self.value == other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __lt__(self, other):
        if isinstance(other, Second):               return self.value < other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __gt__(self, other):
        if isinstance(other, Second):               return self.value > other.value
        raise TypeError("wrong type provided : ", type(other))

class Production:
    def __init__(self, value):
        check_initialisation(value)
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, Production):           return Production(self.value + other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __sub__(self, other):
        if isinstance(other, Production):           return Production(self.value - other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __truediv__(self, other):
        if isinstance(other, Tick):                 return ProductionPerTick(self.value / other.value)
        if isinstance(other, Second):               return ProductionPerTick(self.value / (other.value * TPS))
        if isinstance(other, Production):           return Constant(self.value / other.value)
        if isinstance(other, ProductionPerTick):    return Tick(self.value / other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __eq__(self, other):
        if isinstance(other, Production):           return self.value == other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __lt__(self, other):
        if isinstance(other, Production):           return self.value < other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __gt__(self, other):
        if isinstance(other, Production):           return self.value > other.value
        raise TypeError("wrong type provided : ", type(other))
        
class ProductionPerTick:
    def __init__(self, value=0):
        check_initialisation(value)
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, ProductionPerTick):    return ProductionPerTick(self.value + other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __sub__(self, other):
        if isinstance(other, ProductionPerTick):    return ProductionPerTick(self.value - other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __mul__(self, other):
        if isinstance(other, Tick):                 return Production(self.value * other.value)
        if isinstance(other, Second):               return Production(self.value * other.value * TPS)
        raise TypeError("wrong type provided : ", type(other))
    
    def __truediv__(self, other):
        if isinstance(other, ProductionPerTick):    return Constant(self.value / other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __eq__(self, other):
        if isinstance(other, ProductionPerTick):    return self.value == other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __lt__(self, other):
        if isinstance(other, ProductionPerTick):    return self.value < other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __gt__(self, other):
        if isinstance(other, ProductionPerTick):    return self.value > other.value
        raise TypeError("wrong type provided : ", type(other))

class Energy:
    def __init__(self, value):
        check_initialisation(value)
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, Energy):               return Energy(self.value + other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __sub__(self, other):
        if isinstance(other, Energy):               return Energy(self.value - other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __truediv__(self, other):
        if isinstance(other, Tick):                 return EnergyPerTick(self.value / other.value)
        if isinstance(other, Second):               return EnergyPerTick(self.value / (other.value * TPS))
        if isinstance(other, Energy):               return Constant(self.value / other.value)
        if isinstance(other, EnergyPerTick):        return Tick(self.value / other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __eq__(self, other):
        if isinstance(other, Energy):               return self.value == other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __lt__(self, other):
        if isinstance(other, Energy):               return self.value < other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __gt__(self, other):
        if isinstance(other, Energy):               return self.value > other.value
        raise TypeError("wrong type provided : ", type(other))

class EnergyPerTick:
    def __init__(self, value):
        check_initialisation(value)
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, EnergyPerTick):        return EnergyPerTick(self.value + other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __sub__(self, other):
        if isinstance(other, EnergyPerTick):        return EnergyPerTick(self.value - other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __mul__(self, other):
        if isinstance(other, Tick):                 return Production(self.value * other.value)
        if isinstance(other, Second):               return Production(self.value * other.value * TPS)
        raise TypeError("wrong type provided : ", type(other))
    
    def __truediv__(self, other):
        if isinstance(other, EnergyPerTick):        return Constant(self.value / other.value)
        raise TypeError("wrong type provided : ", type(other))
    
    def __eq__(self, other):
        if isinstance(other, EnergyPerTick):        return self.value == other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __lt__(self, other):
        if isinstance(other, EnergyPerTick):        return self.value < other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __gt__(self, other):
        if isinstance(other, EnergyPerTick):        return self.value > other.value
        raise TypeError("wrong type provided : ", type(other))

class Constant:
    def __init__(self, value):
        check_initialisation(value)
        self.value = value

    def __add__(self, other):
        if isinstance(other, Constant):             return Constant(self.value + other.value)
        if isinstance(other, Second):               return Second(self.value + other.value)
        if isinstance(other, Tick):                 return Tick(self.value + other.value)
        if isinstance(other, Production):           return Production(self.value + other.value)
        if isinstance(other, ProductionPerTick):    return ProductionPerTick(self.value + other.value)
        if isinstance(other, Energy):               return Energy(self.value + other.value)
        if isinstance(other, EnergyPerTick):        return EnergyPerTick(self.value + other.value)
        raise TypeError("type not found : ", type(other))
    
    def __sub__(self, other):
        if isinstance(other, Constant):             return Constant(self.value - other.value)
        if isinstance(other, Second):               return Second(self.value - other.value)
        if isinstance(other, Tick):                 return Tick(self.value - other.value)
        if isinstance(other, Production):           return Production(self.value - other.value)
        if isinstance(other, ProductionPerTick):    return ProductionPerTick(self.value - other.value)
        if isinstance(other, Energy):               return Energy(self.value - other.value)
        if isinstance(other, EnergyPerTick):        return EnergyPerTick(self.value - other.value)
        raise TypeError("type not found : ", type(other))
    
    def __mul__(self, other):
        if isinstance(other, Constant):             return Constant(self.value * other.value)
        if isinstance(other, Second):               return Second(self.value * other.value)
        if isinstance(other, Tick):                 return Tick(self.value * other.value)
        if isinstance(other, Production):           return Production(self.value * other.value)
        if isinstance(other, ProductionPerTick):    return ProductionPerTick(self.value * other.value)
        if isinstance(other, Energy):               return Energy(self.value * other.value)
        if isinstance(other, EnergyPerTick):        return EnergyPerTick(self.value * other.value)
        raise TypeError("type not found : ", type(other))
    
    def __truediv__(self, other):
        if isinstance(other, Constant):             return Constant(self.value / other.value)
        if isinstance(other, Second):               return Second(self.value / other.value)
        if isinstance(other, Tick):                 return Tick(self.value / other.value)
        if isinstance(other, Production):           return Production(self.value / other.value)
        if isinstance(other, ProductionPerTick):    return ProductionPerTick(self.value / other.value)
        if isinstance(other, Energy):               return Energy(self.value / other.value)
        if isinstance(other, EnergyPerTick):        return EnergyPerTick(self.value / other.value)
        raise TypeError("type not found : ", type(other))
    
    def __eq__(self, other):
        if isinstance(other, Constant):             return self.value == other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __lt__(self, other):
        if isinstance(other, Constant):             return self.value < other.value
        raise TypeError("wrong type provided : ", type(other))
    
    def __gt__(self, other):
        if isinstance(other, Constant):             return self.value > other.value
        raise TypeError("wrong type provided : ", type(other))


