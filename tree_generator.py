from typing import Dict, Set, Callable, Optional
from collections import defaultdict
import copy

import pygraphviz as pgv
from unit_system import Production, ProductionPerTick, Second, Tick, Energy, EnergyPerTick, Constant


from energy_tier import EnergyTier
from coil_tier import CoilTier
from item import Item
from crafting_machine import CraftingMachine
from crafting_node import CraftingNode


class debug:
    def __init__(self, dict: Dict, name : str):
        self.dict = dict
        self.name = name
    
    def __getitem__(self, object):
        # print(f"{self.name} : getting object {object} with value {self.dict[object].value}")
        return self.dict[object]
    
    def __setitem__(self, object, value):
        # print(f"{self.name} : setting object {object} which had value {self.dict[object].value} with value {value.value}" )
        self.dict[object] = value

class TreeGenerator:
    def __init__(self, recipee_dict : Dict[str, Dict]):
        self.all_recipee : Dict[str, Dict] = recipee_dict

        self.outputs : Dict[Item, ProductionPerTick] = dict()
        self.consumed : defaultdict[Item, ProductionPerTick] = defaultdict(ProductionPerTick)
        self.inputs : Set[Item] = dict()
        
        self.name_correspondance : Dict[str, CraftingNode] = dict()
        self.graph = pgv.AGraph(directed=True)
        
        self.energy_consumption : Dict[CraftingNode, EnergyPerTick] = dict()
        self.number_of_machines : defaultdict[CraftingMachine, int] = defaultdict()

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
                 recipee_name : str,
                 number_of_machines : int,
                 energy_tier : EnergyTier,
                 default_coil_tier : CoilTier,
                 input_corr : defaultdict[Item, set[CraftingNode]],
                 output_corr : defaultdict[Item, set[CraftingNode]],
                 inputs : list[Item],
                 filter : Callable[[CraftingNode], bool],
                 ):
        
        if recipee_name not in self.name_correspondance.keys():
            raise KeyError("name not found")

        for input in inputs:
            self.outputs[input] = ProductionPerTick(100000000)
        
        craft = copy.deepcopy(input_corr)
        for recipee_node_list in craft.values():
            recipee_node_list = {node for node in recipee_node_list if filter(node)}
            for node in recipee_node_list:
                self.name_correspondance[node.name] = node

        new_output = set(self.name_correspondance[recipee_name].outputs)
        used_set = set(self.name_correspondance[recipee_name].outputs)
        for input in inputs:
            used_set.add(input)

        [energy, machines] = self.name_correspondance[recipee_name].compute_throughput(
            debug(self.outputs, "output"),
            debug(self.consumed, "consumed"),
            energy_tier,
            default_coil_tier,
            number_of_machines,
        )
        self.energy_consumption[self.name_correspondance[recipee_name]] = energy
        self.number_of_machines[self.name_correspondance[recipee_name].crafting_machine[0]] = machines


        while new_output:
            self.graph.add_nodes_from([output.name() for output in new_output])

            for item in new_output: 
                used_set.add(item)

            iterator = copy.deepcopy(new_output)
            new_output.clear()

            used_node : Set[CraftingNode] = set()

            for item in iterator:
                for crafting_node in craft.get(item, []):

                    is_craftable = [item in self.outputs.keys() for item in crafting_node.inputs]
                    if all(is_craftable) and filter(crafting_node):
                        # add a node in the graph for visualisation
                        for output in crafting_node.outputs: 
                            if output not in used_set:
                                new_output.add(output)
                        if crafting_node.name != recipee_name and crafting_node not in used_node:
                            [energy, machines] = crafting_node.compute_throughput(
                                debug(self.outputs, "output"),
                                debug(self.consumed, "consumed"),
                                energy_tier,
                                default_coil_tier,
                                input_corr,
                            )
                            self.energy_consumption[crafting_node] = energy
                            self.number_of_machines[crafting_node.crafting_machine[0]] = machines
                            used_node.add(crafting_node)
                            


    def generate_roots(self, 
                       recipee_name : str, 
                       filter : Callable[[CraftingNode], bool]):
        pass

    def draw_graph(self):
        self.graph.layout(prog="dot")
        self.graph.draw("test.png")
    
    def draw_another_graph(self, 
                           output_corr : defaultdict[Item, set[CraftingNode]], 
                           input_corr : defaultdict[Item, set[CraftingNode]]):

        graph : pgv.AGraph = pgv.AGraph(directed=True)
        for [output, nodes] in output_corr.items():
            for node in nodes:
                graph.add_node(node.name)

        for [output, output_nodes] in output_corr.items():
            for node in input_corr[output]:
                for outnode in output_nodes:
                    graph.add_edge(outnode.name, node.name)
        
        graph.layout(prog="dot")
        graph.draw("test2.png")

    def yet_another_graph(self, 
                           inputs : Optional[list[Item]],
                           output_corr : defaultdict[Item, set[CraftingNode]], 
                           input_corr : defaultdict[Item, set[CraftingNode]]):
        
        graph : pgv.AGraph = pgv.AGraph(directed=True)
        for [output, nodes] in output_corr.items():
            output_value = self.outputs[output]
            if output in inputs:
                output_value = Constant(-100000000) + output_value
            input_value = self.consumed[output]
            graph.add_node(output.name(), label=f"{output.name()} {round((output_value - input_value).value, 2)}")
            for node in nodes:
                graph.add_node(node.name)

        for [output, nodes] in output_corr.items():
            for node in nodes:
                graph.add_edge(node.name, output.name())

        for [input, nodes] in input_corr.items():
            for node in nodes:
                graph.add_edge(input.name(), node.name)
        
        graph.layout(prog="dot")
        graph.draw("test3.png")

    def generate_tree(self,
                      recipee_name : str,
                      inputs : Optional[list[Item]],
                      filter : Callable[[CraftingNode], bool]) -> tuple[defaultdict[Item, set[CraftingNode]]]:
        
        input_corr : defaultdict[Item, Set[CraftingNode]] = defaultdict(set)
        output_corr : defaultdict[Item, Set[CraftingNode]] = defaultdict(set)

        craft = copy.deepcopy(self.input_correspondance)
        for recipee_node_list in craft.values():
            recipee_node_list = {node for node in recipee_node_list if filter(node)}
            for node in recipee_node_list:
                self.name_correspondance[node.name] = node 
        
        if inputs:
            for input in inputs:
                self.outputs[input] = ProductionPerTick(0)

        new_output = set(self.name_correspondance[recipee_name].outputs)
        used_set = set(self.name_correspondance[recipee_name].outputs)
        
        
        self.graph.add_node(recipee_name)
        self.graph.add_nodes_from([output.name() for output in new_output])
        for output in self.name_correspondance[recipee_name].outputs:
            self.graph.add_edge(self.name_correspondance[recipee_name].name, output.name())
        for input in inputs:
            self.graph.add_node(input.name())


        while new_output:
            self.graph.add_nodes_from([output.name() for output in new_output])

            for item in new_output:
                self.outputs[item] = ProductionPerTick(0)
            for item in new_output:
                used_set.add(item)

            iterator = copy.deepcopy(new_output)
            new_output.clear()

            for item in iterator:
                for crafting_node in craft.get(item, []):
                    is_craftable = [item in self.outputs.keys() for item in crafting_node.inputs]
                    if all(is_craftable) and filter(crafting_node):
                        # add a node in the graph for visualisation
                        self.graph.add_node(crafting_node.name)
                        for input in crafting_node.inputs.keys():
                            input_corr[input].add(crafting_node)
                            self.graph.add_edge(input.name(), crafting_node.name)

                        for output in crafting_node.outputs.keys():
                            output_corr[output].add(crafting_node)
                            self.graph.add_edge(crafting_node.name, output.name())
                        
                        [new_output.add(output) for output in crafting_node.outputs if output not in used_set]

        return [input_corr, output_corr]

    def get_energy(self):
        total_power : EnergyPerTick = EnergyPerTick(0)

        for output in self.outputs.keys():
            if output.is_fuel():
                total_power += output.energy_per_mb() * self.outputs[output]
                print(output.name(), " : ", 
                      self.outputs[output], " : ", 
                      output.energy_per_mb(), " : ", 
                      (output.energy_per_mb() * self.outputs[output]))
        
        print("energy generation is", total_power)
    
    def get_consumption(self):
        total_power : EnergyPerTick = EnergyPerTick(0)

        for _, energy_consumption in self.energy_consumption.items():
            total_power += energy_consumption
        
        print("energy consumption is : ", total_power.value)


