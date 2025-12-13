from typing import Dict, Tuple

from item import Item
from coil_tier import CoilTier
from energy_tier import EnergyTier
from crafting_machine import CraftingMachine

class CraftingNode:
    def __init__(self, tuple : Tuple[str, Dict]):
        self.name : str = tuple[0]
        self.crafting_machine : list[CraftingMachine] = tuple[1].get("crafting_machine")
        self.energy_consumption : int = tuple[1].get("energy_consumption")
        self.crafting_time : int = tuple[1].get("crafting_time")
        self.tier_specific : list[EnergyTier] = tuple[1].get("tier_specific")
        self.coil_tier : list[CoilTier] = tuple[1].get("coil_tier")


        self.inputs : Dict[Item, int] = tuple[1].get("inputs")
        self.outputs : Dict[Item, int] = tuple[1].get("outputs")




