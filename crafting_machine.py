
from enum import Enum
from typing import Optional

from energy_tier import EnergyTier
from coil_tier import CoilTier

from unit_system import Production, ProductionPerTick, Second, Tick, Energy, EnergyPerTick, Constant

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
   
    def crafting_time(self, 
                       crafting_node, 
                       energy_tier : EnergyTier,
                       coil_tier : Optional[CoilTier]) -> Second:

        min_tier = EnergyTier.LV
        if crafting_node.tier_specific:
            min_tier = min(crafting_node.tier_specific)
            if energy_tier not in crafting_node.tier_specific:
                raise ValueError("wrong energy tier provided for recipee " + crafting_node.name + " : " + energy_tier.name())
       

        oveclock_modifier = 2
        if self.overclock():
             oveclock_modifier = 4

        coil_modifier = 1.0
        if coil_tier and crafting_node.coil_tier:
            coil_modifier = coil_tier.speedup() / max(1.0, crafting_node.coil_tier.speedup())
       
        return Constant(oveclock_modifier ** (min_tier - energy_tier) * coil_modifier) * crafting_node.crafting_time
   
    def energy_needed_modifier(self, 
                      crafting_node,
                      energy_tier : EnergyTier, 
                      coil_tier: Optional[CoilTier]) -> Constant:
        
        min_tier = EnergyTier.LV
        if crafting_node.tier_specific:
            min_tier = min(crafting_node.tier_specific)
            if energy_tier not in crafting_node.tier_specific:
                raise ValueError("wrong energy tier provided for recipee " + crafting_node.name + " : " + energy_tier.name())
       
        coil_modifier = 1.0
        if coil_tier and crafting_node.coil_tier:
            coil_modifier = coil_tier.energy_consumption()
       
        return Constant((4 ** (energy_tier - min_tier)) * coil_modifier)
