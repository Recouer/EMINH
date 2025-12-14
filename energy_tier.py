from enum import Enum

class EnergyTier(Enum):
    LV = 0
    MV = 1
    HV = 2
    EV = 3
    IV = 4

    def name(self):
        match self:
            case EnergyTier.LV: return "LV"
            case EnergyTier.MV: return "MV"
            case EnergyTier.HV: return "HV"
            case EnergyTier.EV: return "EV"
            case EnergyTier.IV: return "IV"
    
    def __add__(self, other) -> int:
        return self.value + other.value
        
    def __sub__(self, other) -> int:
        return self.value - other.value
    
    def __lt__(self, other) -> bool:
        return self.value < other.value
    
    def __gt__(self, other) -> bool:
        return self.value > other.value
