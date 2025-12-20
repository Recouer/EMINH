from typing import Dict, Tuple, Union
from collections import defaultdict

from item import Item
from coil_tier import CoilTier
from energy_tier import EnergyTier
from crafting_machine import CraftingMachine

from unit_system import Production, ProductionPerTick, Second, Tick, Energy, EnergyPerTick, Constant

TPS = 20

class CraftingNode:
    def __init__(self, tuple : Tuple[str, Dict]):
        self.name : str = tuple[0]
        self.crafting_machine : list[CraftingMachine] = tuple[1].get("crafting_machine")
        self.energy_consumption : EnergyPerTick = EnergyPerTick(float(tuple[1].get("energy_consumption")))
        self.crafting_time : Second = Second(float(tuple[1].get("crafting_time")))
        self.tier_specific : list[EnergyTier] = tuple[1].get("tier_specific")
        self.coil_tier : list[CoilTier] = tuple[1].get("coil_tier")

        self.inputs : Dict[Item, Production] = dict([[it, Production(float(value))] for [it, value] in tuple[1].get("inputs").items()])
        self.outputs : Dict[Item, Production] = dict([[it, Production(float(value))] for [it, value] in tuple[1].get("outputs").items()])

    def compute_throughput(self,
                             outputs, # : Dict[Item, ProductionPerTick],
                             inputs, # : Dict[Item, ProductionPerTick],
                             energy_tier : EnergyTier,
                             default_coil_tier: CoilTier,
                             input_corr : Union[int, defaultdict[Item, set]],) -> tuple[EnergyPerTick, Constant]:

        if isinstance(input_corr, int):
            for output in self.outputs:
                outputs[output] = Constant(input_corr) * self.outputs[output] / self.crafting_machine[0].crafting_time(self, energy_tier, default_coil_tier)
            for input in self.inputs:
                inputs[input] = Constant(input_corr) * self.inputs[input] / self.crafting_machine[0].crafting_time(self, energy_tier, default_coil_tier)
        
            return [
                self.crafting_machine[0]
                    .energy_needed_modifier(self, energy_tier, default_coil_tier) 
                    * Constant(input_corr)
                    * self.energy_consumption,
                Constant(input_corr)
            ]
        else:
            nb_of_machines : Constant = Constant(1000000)
            for input in self.inputs:

                nb_of_machines = min(
                    nb_of_machines, 
                    ((outputs[input]) * self.crafting_machine[0].crafting_time(self, energy_tier, default_coil_tier)) / (Constant(len(input_corr[input])) * self.inputs[input])
                )
            
            # what happens when one input that isn't critical has multiple output connection ?
            

            for input in self.inputs:
                inputs[input] = inputs[input] + nb_of_machines * self.inputs[input] / self.crafting_machine[0].crafting_time(self, energy_tier, default_coil_tier)

            for output in self.outputs:
                outputs[output] = outputs[output] + nb_of_machines * self.outputs[output] / self.crafting_machine[0].crafting_time(self, energy_tier, default_coil_tier)

            return [
                self.crafting_machine[0].energy_needed_modifier(self, self.min_tier(), default_coil_tier) 
                    * nb_of_machines
                    * self.energy_consumption,
                nb_of_machines
            ]


    def min_tier(self):
        if len(self.tier_specific) == 0:
            return EnergyTier.LV
        else: 
            return min(self.tier_specific)

