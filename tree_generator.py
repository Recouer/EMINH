from typing import Dict, Set, Callable, Optional
from collections import defaultdict
import copy

from energy_tier import EnergyTier
from coil_tier import CoilTier
from item import Item
from crafting_machine import CraftingMachine
from crafting_node import CraftingNode

class CraftingMachineNode:
    def __init__(self, 
                 crafting_node: CraftingNode,
                 crafting_machine : CraftingMachine,
                 number_of_machines : int,
                 energy_tier: EnergyTier,
                 coil_tier: CoilTier,):
        
        if crafting_machine not in crafting_node.crafting_machine:
            return KeyError("crafting machine not in available crafting nodes.")

        self.crafting_machine: CraftingMachine = crafting_machine
        self.crafting_node: CraftingNode = crafting_node
        self.number_of_machines :  int = number_of_machines
        self.energy_tier : EnergyTier = energy_tier
        self.coil_tier : CoilTier = coil_tier
    
    def energy_consumption(self):
        return self.number_of_machines * self.crafting_node.crafting_machine

class TreeGenerator:
    def __init__(self, recipee_dict : Dict[str, Dict]):
        self.all_recipee : Dict[str, Dict] = recipee_dict

        self.outputs : Dict[Item, int] = dict()
        self.inputs : Set[Item] = dict()
        
        self.name_correspondance : Dict[str, CraftingNode] = dict()

        self.output_correspondance : defaultdict[Item, Set[CraftingNode]] = defaultdict(set)
        self.input_correspondance : defaultdict[Item, Set[CraftingNode]] = defaultdict(set)
        self.__preprocess_tree()
   
    def __preprocess_tree(self):
        for recipee_data in self.all_recipee.items():
            crafting_node = CraftingNode(recipee_data)
            for output in crafting_node.outputs.keys():
                self.output_correspondance[output].add(crafting_node)
            for input in crafting_node.inputs.keys():
                self.input_correspondance[input].add(crafting_node)

    def equalize(self,
                 crafting_node_name : str,
                 number_of_machines : int,
                 energy_tier : EnergyTier,
                 default_coil_tier : CoilTier,
                 ):
        
        if crafting_node_name not in self.name_correspondance.keys():
            return IndexError("name not found")

        
        


    def generate_roots(self, 
                       recipee_name : str, 
                       filter : Callable[[CraftingNode], bool]):
        pass


    def generate_tree(self,
                      recipee_name : str,
                      inputs : Optional[list[Item]],
                      filter : Callable[[CraftingNode], bool]):
        
        craft = copy.deepcopy(self.input_correspondance)
        for recipee_node_list in craft.values():
            recipee_node_list = {node for node in recipee_node_list if filter(recipee_node_list)}
            for node in recipee_node_list:
                self.name_correspondance[node.name] = node 
        
        if inputs:
            for input in inputs:
                self.outputs[input] = 0

        new_output = set(self.name_correspondance[recipee_name].outputs)
        used_set = set(self.name_correspondance[recipee_name].outputs)

        while new_output:
            for item in new_output:
                self.outputs[item] = 0
            for item in new_output:
                used_set.add(item)

            iterator = copy.deepcopy(new_output)
            new_output.clear()

            for item in iterator:
                for crafting_node in craft.get(item, []):
                    is_craftable = [item for item in crafting_node.inputs if item in self.outputs.keys()]
                    if all(is_craftable):
                        [new_output.add(output) for output in crafting_node.outputs if output not in used_set]



