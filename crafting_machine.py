
from enum import Enum
from typing import Optional

from energy_tier import EnergyTier
from coil_tier import CoilTier

class CraftingMachine(Enum):
    GREENHOUSE = 0
    CHEMICAL_REACTOR = 1
    LARGE_CHEMICAL_REACTOR = 2
    COMPRESSOR = 3
    MACERATOR = 4
    PYROLYSE_OVEN = 5
    DISTILLATION_TOWER = 6
    COAL_LIQUEFACTION_TOWER = 7
    CRACKER = 8


    def overclock(self):
        match self:
            case CraftingMachine.GREENHOUSE:
                return True
            case CraftingMachine.CHEMICAL_REACTOR:
                return False
            case CraftingMachine.LARGE_CHEMICAL_REACTOR:
                return True
            case CraftingMachine.COMPRESSOR:
                return False
            case CraftingMachine.MACERATOR:
                return False
            case CraftingMachine.PYROLYSE_OVEN:
                return False
            case CraftingMachine.DISTILLATION_TOWER:
                return False
            case CraftingMachine.COAL_LIQUEFACTION_TOWER:
                return False
            case CraftingMachine.CRACKER:
                return False
   
    def crafting_speed(self, 
                       crafting_node, 
                       energy_tier : EnergyTier,
                       coil_tier : Optional[CoilTier]) -> float:
        if energy_tier not in crafting_node.energy_tier:
            return ValueError("wrong energy tier provided for recipee " + crafting_node.name + " : " + energy_tier)
       
        oveclock_modifier = 2
        if self.overclock():
             oveclock_modifier = 4
            
        coil_modifier = 1.0
        if coil_tier and crafting_node.coil_tier:
            coil_modifier = coil_tier / max(1.0, min([coil.speedup() for coil in crafting_node.coil_tier]))
       
        if crafting_node.tier_specific.empty():
            return (oveclock_modifier ** (-energy_tier)) * crafting_node.crafting_time * coil_modifier
        else:
            return (oveclock_modifier ** (min(crafting_node.tier_specific) - energy_tier)) * crafting_node.crafting_time * coil_modifier
   
    def energy_needed(self, 
                      crafting_node,
                      energy_tier : EnergyTier, 
                      coil_tier: Optional[CoilTier]) -> int:
        
        if energy_tier not in crafting_node.energy_tier:
            return ValueError("wrong energy tier provided for recipee " + crafting_node.name + " : " + energy_tier)
       
        coil_modifier = 1.0
        if coil_tier and crafting_node.coil_tier:
            coil_modifier = coil_tier.energy_consumption()
       
        if crafting_node.tier_specific.empty():
            return (4 ** energy_tier) * crafting_node.crafting_time * coil_modifier
        else:
            return (4 ** (energy_tier - min(crafting_node.tier_specific))) * crafting_node.crafting_time * coil_modifier
