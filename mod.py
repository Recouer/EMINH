from typing import Dict, Set
from collections import defaultdict
# import graphviz
# pyqtgraph :: used for UI in the future
# add the coil speedup


from energy_tier import EnergyTier
from coil_tier import CoilTier
from item import Item
from crafting_machine import CraftingMachine
from tree_generator import TreeGenerator

recipee_dict = {
    "greenhouse_2" : {
        "crafting_machine" : [ CraftingMachine.GREENHOUSE ],
        "energy_consumption" : 16,
        "crafting_time" : 600,
        "inputs" : {
            Item.FERTILIZER : 16,
        },
        "outputs" : {
            Item.WOOD : 64,
            Item.SAPPLING : 8,
        },
        "tier_specific" : [],
        "coil_tier" : None,
    },
    "compressor_sappling" : {
        "crafting_machine" : [ CraftingMachine.COMPRESSOR ],
        "energy_consumption" : 2,
        "crafting_time" : 15,
        "inputs" : {
            Item.SAPPLING : 1
        },
        "outputs" : {
            Item.PLANT_BALL : 1
        },
        "tier_specific" : [],
        "coil_tier" : None,
    },
    "low_tier_sappling_macerator" : {
        "crafting_machine" : [ CraftingMachine.MACERATOR ],
        "energy_consumption" : 4,
        "crafting_time" : 10,
        "inputs" : {
            Item.PLANT_BALL : 2
        },
        "outputs" : {
            Item.BIO_CHAFF : 2
        },
        "tier_specific" : [
            EnergyTier.LV, EnergyTier.MV
        ],
        "coil_tier" : None,
    },
    "HV_sappling_macerator" : {
        "crafting_machine" : [ CraftingMachine.MACERATOR ],
        "energy_consumption" : 64,
        "crafting_time" : 2.5,
        "inputs" : {
            Item.PLANT_BALL : 2
        },
        "outputs" : {
            Item.BIO_CHAFF : 2.75
        },
        "tier_specific" : [
            EnergyTier.HV, EnergyTier.EV, EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "pyrolyse_fermented_biomass" : {
        "crafting_machine" : [ CraftingMachine.PYROLYSE_OVEN ],
        "energy_consumption" : 10,
        "crafting_time" : 10,
        "inputs" : {
            Item.BIO_CHAFF : 1,
            Item.WATER : 1500,
        },
        "outputs" : {
            Item.FERMENTED_BIOMASS : 1500,
        },
        "tier_specific" : [
        ],
        "coil_tier" : CoilTier.CUPRONICKEL,
    },
    "fermented_biomass_distillation" : {
        "crafting_machine" : [ CraftingMachine.DISTILLATION_TOWER ],
        "energy_consumption" : 180,
        "crafting_time" : 3.75,
        "inputs" : {
            Item.FERMENTED_BIOMASS : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 600,
            Item.CARBON_DIOXIDE : 400,
            Item.AMMONIA : 100,
            Item.METHANOL : 150,
            Item.ETHANOL : 150,
            Item.WATER : 375,
            Item.ACETIC_ACID : 25,
            Item.FERTILIZER : 1,
        },
        "tier_specific" : [
            EnergyTier.HV, EnergyTier.EV, EnergyTier.IV
        ],
        "coil_tier" : None,
    },
    "log_pyrolise_creosote" : {
        "crafting_machine" : [ CraftingMachine.PYROLYSE_OVEN ],
        "energy_consumption" : 64,
        "crafting_time" : 32,
        "inputs" : {
            Item.WOOD : 16,
            Item.NITROGEN_GAS : 1000,
        },
        "outputs" : {
            Item.CHARCOAL : 20,
            Item.CREOSOTE : 4000,
        },
        "tier_specific" : [
            EnergyTier.MV, EnergyTier.HV, EnergyTier.EV, EnergyTier.IV,
        ],
        "coil_tier" : CoilTier.CUPRONICKEL,
    },
    "log_pyrolise_heavy_oil" : {
        "crafting_machine" : [ CraftingMachine.PYROLYSE_OVEN ],
        "energy_consumption" : 192,
        "crafting_time" : 16,
        "inputs" : {
            Item.WOOD : 16,
        },
        "outputs" : {
            Item.ASHES : 4,
            Item.HEAVY_OIL : 200,
        },
        "tier_specific" : [
            EnergyTier.HV, EnergyTier.EV, EnergyTier.IV,
        ],
        "coil_tier" : CoilTier.CUPRONICKEL,
    },
    "log_pyrolise_wood_tar" : {
        "crafting_machine" : [ CraftingMachine.PYROLYSE_OVEN ],
        "energy_consumption" : 64,
        "crafting_time" : 32,
        "inputs" : {
            Item.WOOD : 16,
            Item.NITROGEN_GAS : 1000,
        },
        "outputs" : {
            Item.CHARCOAL : 20,
            Item.WOOD_TAR : 1500,
        },
        "tier_specific" : [
            EnergyTier.MV, EnergyTier.HV, EnergyTier.EV, EnergyTier.IV,
        ],
        "coil_tier" : CoilTier.CUPRONICKEL,
    },
    "charcoal_coal_liquefaction" : {
        "crafting_machine" : [ CraftingMachine.COAL_LIQUEFACTION_TOWER ],
        "energy_consumption" : 60,
        "crafting_time" : 50,
        "inputs" : {
            Item.CHARCOAL : 40,
            Item.CREOSOTE : 4000,
            Item.HYDROGEN : 1,
        },
        "outputs" : {
            Item.COAL_TAR : 500,
            Item.SYNGAS : 4400,
            Item.RAW_AROMATIC_MIX : 4000,
        },
        "tier_specific" : [
            EnergyTier.MV, EnergyTier.HV, EnergyTier.EV, EnergyTier.IV,
        ],
        "coil_tier" : CoilTier.CUPRONICKEL,
    },
    "AroFeed_chemical" : {
        "crafting_machine" : [ 
            CraftingMachine.LARGE_CHEMICAL_REACTOR, 
            CraftingMachine.CHEMICAL_REACTOR, 
        ],
        "energy_consumption" : 30,
        "crafting_time" : 30,
        "inputs" : {
            Item.RAW_AROMATIC_MIX : 4000,
            Item.BENZENE : 525,
            Item.STEAM : 1000,
        },
        "outputs" : {
            Item.AROMATIC_FEEDSTOCK : 2000,
        },
        "tier_specific" : [
        ],
        "coil_tier" : None,
    },
    "RefAroFeed_chemical" : {
        "crafting_machine" : [ 
            CraftingMachine.LARGE_CHEMICAL_REACTOR,
            CraftingMachine.CHEMICAL_REACTOR,
        ],
        "energy_consumption" : 120,
        "crafting_time" : 18,
        "inputs" : {
            Item.AROMATIC_FEEDSTOCK : 2000,
            Item.RHENIUM : 1,
        },
        "outputs" : {
            Item.REFORMED_AROMATIC_FEEDSTOCK : 2000,
        },
        "tier_specific" : [
            EnergyTier.MV, 
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "reformate_cracker" : {
        "crafting_machine" : [ 
            CraftingMachine.CRACKER
         ],
        "energy_consumption" : 120,
        "crafting_time" : 30,
        "inputs" : {
            Item.REFORMED_AROMATIC_FEEDSTOCK : 2000,
            Item.STEAM : 4000,
        },
        "outputs" : {
            Item.REFORMATE_GAS : 8000,
            Item.CRACKED_REFORMATE_GAS : 1000,
        },
        "tier_specific" : [
            EnergyTier.MV, 
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "woodTar_distillery" : {
        "crafting_machine" : [ 
            CraftingMachine.DISTILLATION_TOWER 
        ],
        "energy_consumption" : 256,
        "crafting_time" : 2,
        "inputs" : {
            Item.WOOD_TAR : 1000,
        },
        "outputs" : {
            Item.DIMETHYLBENZENE : 200,
            Item.TOLUENE : 75,
            Item.BENZENE : 350,
            Item.PHENOL : 75,
            Item.CREOSOTE : 300,
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },












    "heavyOil_distillation" : {
        "crafting_machine" : [ CraftingMachine.DISTILLATION_TOWER ],
        "energy_consumption" : 288,
        "crafting_time" : 1,
        "inputs" : {
            Item.HEAVY_OIL : 100,
        },
        "outputs" : {
            Item.SULFURIC_GAS : 60,
            Item.SULFURIC_NAPHTA : 15,
            Item.SULFURIC_LIGHT_FUEL : 45,
            Item.SULFURIC_HEAVY_FUEL : 250,
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "HeavyFuel_chemical" : {
        "crafting_machine" : [ 
            CraftingMachine.LARGE_CHEMICAL_REACTOR,
            CraftingMachine.CHEMICAL_REACTOR,
        ],
        "energy_consumption" : 30,
        "crafting_time" : 8,
        "inputs" : {
            Item.SULFURIC_HEAVY_FUEL : 8000,
            Item.HYDROGEN : 2000,
        },
        "outputs" : {
            Item.HYDROGEN_SULFIDE : 1000,
            Item.HEAVY_FUEL : 8000,
        },
        "tier_specific" : [
        ],
        "coil_tier" : None,
    },
    "lightFuel_chemical" : {
        "crafting_machine" : [
            CraftingMachine.LARGE_CHEMICAL_REACTOR,
            CraftingMachine.CHEMICAL_REACTOR,
        ],
        "energy_consumption" : 30,
        "crafting_time" : 8,
        "inputs" : {
            Item.SULFURIC_LIGHT_FUEL : 12000,
            Item.HYDROGEN : 2000,
        },
        "outputs" : {
            Item.LIGHT_FUEL : 12000,
            Item.HYDROGEN_SULFIDE : 1000,
        },
        "tier_specific" : [
        ],
        "coil_tier" : None,
    },
    "naphta_chemical" : {
        "crafting_machine" : [
            CraftingMachine.LARGE_CHEMICAL_REACTOR,
            CraftingMachine.CHEMICAL_REACTOR,
        ],
        "energy_consumption" : 30,
        "crafting_time" : 8,
        "inputs" : {
            Item.SULFURIC_NAPHTA : 12000,
            Item.HYDROGEN : 2000,
        },
        "outputs" : {
            Item.NAPHTA : 12000,
            Item.HYDROGEN_SULFIDE : 1000,
        },
        "tier_specific" : [
        ],
        "coil_tier" : None,
    },
    "sulfuricGas_chemical" : {
        "crafting_machine" : [
            CraftingMachine.LARGE_CHEMICAL_REACTOR,
            CraftingMachine.CHEMICAL_REACTOR,
        ],
        "energy_consumption" : 30,
        "crafting_time" : 8,
        "inputs" : {
            Item.SULFURIC_GAS : 16000,
            Item.HYDROGEN : 2000,
        },
        "outputs" : {
            Item.REFINERY_GAS : 16000,
            Item.HYDROGEN_SULFIDE : 1000,
        },
        "tier_specific" : [
        ],
        "coil_tier" : None,
    },




    "heavyFuel_cracker_steamSevere" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 480,
        "crafting_time" : 8,
        "inputs" : {
            Item.HEAVY_FUEL : 1000,
            Item.STEAM : 1000,
        },
        "outputs" : {
            Item.SEVERELY_STEAM_CRACKED_HEAVY_FUEL : 1000
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "heavyFuel_cracker_steamLight" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 240,
        "crafting_time" : 4,
        "inputs" : {
            Item.HEAVY_FUEL : 1000,
            Item.STEAM : 1000,
        },
        "outputs" : {
            Item.LIGHTLY_STEAM_CRACKED_HEAVY_FUEL : 1000
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "heavyFuel_cracker_hydroSevere" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 240,
        "crafting_time" : 8,
        "inputs" : {
            Item.HEAVY_FUEL : 1000,
            Item.HYDROGEN : 6000,
        },
        "outputs" : {
            Item.SEVERELY_HYDRO_CRACKED_HEAVY_FUEL : 1000
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "heavyFuel_cracker_hydroLight" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 120,
        "crafting_time" : 4,
        "inputs" : {
            Item.HEAVY_FUEL : 1000,
            Item.HYDROGEN : 2000,
        },
        "outputs" : {
            Item.LIGHTLY_HYDRO_CRACKED_HEAVY_FUEL : 1000
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },



    "LightFuel_cracker_steamSevere" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 480,
        "crafting_time" : 8,
        "inputs" : {
            Item.LIGHT_FUEL : 1000,
            Item.STEAM : 1000,
        },
        "outputs" : {
            Item.SEVERELY_STEAM_CRACKED_LIGHT_FUEL : 1000
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "LightFuel_cracker_steamLight" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 240,
        "crafting_time" : 4,
        "inputs" : {
            Item.LIGHT_FUEL : 1000,
            Item.STEAM : 1000,
        },
        "outputs" : {
            Item.LIGHTLY_STEAM_CRACKED_LIGHT_FUEL : 1000
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "LightFuel_cracker_hydroSevere" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 240,
        "crafting_time" : 8,
        "inputs" : {
            Item.LIGHT_FUEL : 1000,
            Item.HYDROGEN : 6000,
        },
        "outputs" : {
            Item.SEVERELY_HYDRO_CRACKED_LIGHT_FUEL : 1000
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "LightFuel_cracker_hydroLight" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 120,
        "crafting_time" : 4,
        "inputs" : {
            Item.LIGHT_FUEL : 1000,
            Item.HYDROGEN : 2000,
        },
        "outputs" : {
            Item.LIGHTLY_HYDRO_CRACKED_LIGHT_FUEL : 1000
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },



    "naphta_cracker_steamSevere" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 480,
        "crafting_time" : 8,
        "inputs" : {
            Item.NAPHTA : 1000,
            Item.STEAM : 1000,
        },
        "outputs" : {
            Item.SEVERELY_STEAM_CRACKED_NAPHTA : 1000
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "naphta_cracker_steamLight" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 240,
        "crafting_time" : 4,
        "inputs" : {
            Item.NAPHTA : 1000,
            Item.STEAM : 1000,
        },
        "outputs" : {
            Item.LIGHTLY_STEAM_CRACKED_NAPHTA : 1000
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "naphta_cracker_hydroSevere" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 240,
        "crafting_time" : 8,
        "inputs" : {
            Item.NAPHTA : 1000,
            Item.HYDROGEN : 6000,
        },
        "outputs" : {
            Item.SEVERELY_HYDRO_CRACKED_NAPHTA : 1000
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "naphta_cracker_hydroLight" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 120,
        "crafting_time" : 4,
        "inputs" : {
            Item.NAPHTA : 1000,
            Item.HYDROGEN : 2000,
        },
        "outputs" : {
            Item.LIGHTLY_HYDRO_CRACKED_NAPHTA : 1000
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },



    "refineryGas_cracker_steamSevere" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 480,
        "crafting_time" : 8,
        "inputs" : {
            Item.REFINERY_GAS : 1000,
            Item.STEAM : 1000,
        },
        "outputs" : {
            Item.SEVERELY_STEAM_CRACKED_REFINERY_GAS : 1000
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "refineryGas_cracker_steamLight" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 240,
        "crafting_time" : 4,
        "inputs" : {
            Item.REFINERY_GAS : 1000,
            Item.STEAM : 1000,
        },
        "outputs" : {
            Item.LIGHTLY_STEAM_CRACKED_REFINERY_GAS : 1000
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "refineryGas_cracker_hydroSevere" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 240,
        "crafting_time" : 8,
        "inputs" : {
            Item.REFINERY_GAS : 1000,
            Item.HYDROGEN : 6000,
        },
        "outputs" : {
            Item.SEVERELY_HYDRO_CRACKED_REFINERY_GAS : 1000
        },
        "tier_specific" : [
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "refineryGas_cracker_hydroLight" : {
        "crafting_machine" : [
            CraftingMachine.CRACKER,
        ],
        "energy_consumption" : 120,
        "crafting_time" : 4,
        "inputs" : {
            Item.REFINERY_GAS : 1000,
            Item.HYDROGEN : 2000,
        },
        "outputs" : {
            Item.LIGHTLY_HYDRO_CRACKED_REFINERY_GAS : 1000
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV, 
            EnergyTier.EV, 
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },


    "SSCHF_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.SEVERELY_STEAM_CRACKED_HEAVY_FUEL : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 150,
            Item.ETHYLENE : 150,
            Item.ETHANE : 15,
            Item.PROPENE : 100,
            Item.PROPANE : 10,
            Item.BUTADIENE : 50,
            Item.BUTENE : 80,
            Item.BENZENE : 400,
            Item.TOLUENE : 80,
            Item.NAPHTA : 125,
            Item.LIGHT_FUEL : 100,
            Item.CARBON : 0.3,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "SHCHF_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.SEVERELY_HYDRO_CRACKED_HEAVY_FUEL : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 175,
            Item.ETHANE : 175,
            Item.PROPANE : 300,
            Item.BUTANE : 300,
            Item.NAPHTA : 250,
            Item.LIGHT_FUEL : 200,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },

    "LSCHF_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.LIGHTLY_STEAM_CRACKED_HEAVY_FUEL : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 50,
            Item.ETHYLENE : 50,
            Item.ETHANE : 5,
            Item.PROPENE : 30,
            Item.PROPANE : 3,
            Item.BUTADIENE : 15,
            Item.BUTENE : 25,
            Item.BENZENE : 125,
            Item.TOLUENE : 25,
            Item.NAPHTA : 50,
            Item.LIGHT_FUEL : 300,
            Item.CARBON : 0.3,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "LHCHF_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.LIGHTLY_HYDRO_CRACKED_HEAVY_FUEL : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 75,
            Item.ETHANE : 75,
            Item.PROPANE : 100,
            Item.BUTANE : 100,
            Item.NAPHTA : 100,
            Item.LIGHT_FUEL : 600,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },


    "SSCLF_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.SEVERELY_STEAM_CRACKED_LIGHT_FUEL : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 250,
            Item.ETHYLENE : 250,
            Item.ETHANE : 50,
            Item.PROPENE : 250,
            Item.PROPANE : 50,
            Item.BUTADIENE : 50,
            Item.BUTENE : 65,
            Item.BENZENE : 150,
            Item.TOLUENE : 30,
            Item.NAPHTA : 100,
            Item.HEAVY_FUEL : 50,
            Item.CARBON : 0.3,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "SHCLF_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.SEVERELY_HYDRO_CRACKED_LIGHT_FUEL : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 1500,
            Item.ETHANE : 1500,
            Item.PROPANE : 125,
            Item.BUTANE : 125,
            Item.OCTANE : 20,
            Item.NAPHTA : 200,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },

    "LSCLF_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.LIGHTLY_STEAM_CRACKED_LIGHT_FUEL : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 50,
            Item.ETHYLENE : 50,
            Item.ETHANE : 10,
            Item.PROPENE : 150,
            Item.PROPANE : 20,
            Item.BUTADIENE : 60,
            Item.BUTENE : 75,
            Item.BENZENE : 200,
            Item.TOLUENE : 40,
            Item.NAPHTA : 400,
            Item.HEAVY_FUEL : 150,
            Item.CARBON : 0.11,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "LHCLF_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.LIGHTLY_HYDRO_CRACKED_LIGHT_FUEL : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 125,
            Item.ETHANE : 125,
            Item.PROPANE : 200,
            Item.BUTANE : 150,
            Item.NAPHTA : 100,
            Item.NAPHTA : 800,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },


    "SSCN_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.SEVERELY_STEAM_CRACKED_NAPHTA : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 500,
            Item.ETHYLENE : 500,
            Item.ETHANE : 65,
            Item.PROPENE : 300,
            Item.PROPANE : 15,
            Item.BUTADIENE : 50,
            Item.BUTENE : 50,
            Item.BENZENE : 100,
            Item.TOLUENE : 20,
            Item.LIGHT_FUEL : 50,
            Item.HEAVY_FUEL : 25,
            Item.CARBON : 0.33,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "SHCN_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.SEVERELY_HYDRO_CRACKED_NAPHTA : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 1500,
            Item.ETHANE : 1500,
            Item.PROPANE : 125,
            Item.BUTANE : 125,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },

    "LSCN_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.LIGHTLY_STEAM_CRACKED_NAPHTA : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 200,
            Item.ETHYLENE : 200,
            Item.ETHANE : 35,
            Item.PROPENE : 200,
            Item.PROPANE : 15,
            Item.BUTADIENE : 150,
            Item.BUTENE : 80,
            Item.BENZENE : 150,
            Item.TOLUENE : 40,
            Item.LIGHT_FUEL : 150,
            Item.HEAVY_FUEL : 75,
            Item.CARBON : 0.11,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "LHCN_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.LIGHTLY_HYDRO_CRACKED_NAPHTA : 1000,
        },
        "outputs" : {
            Item.METHANE_GAS : 250,
            Item.ETHANE : 250,
            Item.PROPANE : 300,
            Item.BUTANE : 800,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },


    "SSCG_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.SEVERELY_STEAM_CRACKED_REFINERY_GAS : 1000,
        },
        "outputs" : {
            Item.HELIUM : 20,
            Item.METHANE_GAS : 1018,
            Item.ETHYLENE : 92,
            Item.ETHANE : 45,
            Item.PROPENE : 8,
            Item.CARBON : 0.11,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "SHCG_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.SEVERELY_HYDRO_CRACKED_REFINERY_GAS : 1000,
        },
        "outputs" : {
            Item.HELIUM : 20,
            Item.HYDROGEN : 4340,
            Item.METHANE_GAS : 1400,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },

    "LSCG_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.LIGHTLY_STEAM_CRACKED_REFINERY_GAS : 1000,
        },
        "outputs" : {
            Item.HELIUM : 20,
            Item.METHANE_GAS : 1026,
            Item.ETHYLENE : 85,
            Item.ETHANE : 8,
            Item.PROPENE : 45,
            Item.CARBON : 0.11,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    "LHCG_distillation" : {
        "crafting_machine" : [
            CraftingMachine.DISTILLATION_TOWER
        ],
        "energy_consumption" : 120,
        "crafting_time" : 6,
        "inputs" : {
            Item.LIGHTLY_HYDRO_CRACKED_REFINERY_GAS : 1000,
        },
        "outputs" : {
            Item.HELIUM : 20,
            Item.HYDROGEN : 1340,
            Item.METHANE_GAS : 1400,
        },
        "tier_specific" : [
            EnergyTier.MV,
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    
    
    "highOctan_chemical" : {
        "crafting_machine" : [
            CraftingMachine.LARGE_CHEMICAL_REACTOR,
            CraftingMachine.CHEMICAL_REACTOR,
        ],
        "energy_consumption" : 1920,
        "crafting_time" : 2.5,
        "inputs" : {
            Item.GASOLINE : 20_000,
            Item.OCTANE : 2000,
            Item.NITROUS_OXIDE : 2000,
            Item.TOLUENE : 1000,
            Item.ETHYL_THERBUTYL_ETHER : 1000,
        },
        "outputs" : {
            Item.HIGH_OCTANE_GASOLINE : 32_000,
        },
        "tier_specific" : [
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    
    
    "ETE_chemical" : {
        "crafting_machine" : [
            CraftingMachine.LARGE_CHEMICAL_REACTOR,
            CraftingMachine.CHEMICAL_REACTOR,
        ],
        "energy_consumption" : 480,
        "crafting_time" : 20,
        "inputs" : {
            Item.ETHANOL : 1000,
            Item.BUTENE : 1000,
        },
        "outputs" : {
            Item.ETHYL_THERBUTYL_ETHER : 1000,
        },
        "tier_specific" : [
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    
    
    "gasoline_chemical" : {
        "crafting_machine" : [
            CraftingMachine.LARGE_CHEMICAL_REACTOR,
            CraftingMachine.CHEMICAL_REACTOR,
        ],
        "energy_consumption" : 480,
        "crafting_time" : 0.5,
        "inputs" : {
            Item.RAW_GASOLINE : 10_000,
            Item.TOLUENE : 1000,
        },
        "outputs" : {
            Item.GASOLINE : 11_000,
        },
        "tier_specific" : [
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    
    
    "rawGasoline_chemical" : {
        "crafting_machine" : [
            CraftingMachine.LARGE_CHEMICAL_REACTOR,
            CraftingMachine.CHEMICAL_REACTOR,
        ],
        "energy_consumption" : 480,
        "crafting_time" : 5,
        "inputs" : {
            Item.NAPHTA : 16_000,
            Item.REFINERY_GAS : 2000,
            Item.METHANOL : 1000,
            Item.ACETONE : 1000,
        },
        "outputs" : {
            Item.RAW_GASOLINE : 20_000,
        },
        "tier_specific" : [
            EnergyTier.HV,
            EnergyTier.EV,
            EnergyTier.IV,
        ],
        "coil_tier" : None,
    },
    
    
    "acetone_chemical" : {
        "crafting_machine" : [
            CraftingMachine.LARGE_CHEMICAL_REACTOR,
            CraftingMachine.CHEMICAL_REACTOR,
        ],
        "energy_consumption" : 480,
        "crafting_time" : 20,
        "inputs" : {
            Item.ACETIC_ACID : 3_000,
        },
        "outputs" : {
            Item.ACETONE : 2_000,
            Item.OXYGEN : 1_000
        },
        "tier_specific" : [
        ],
        "coil_tier" : None,
    },
}


tree = TreeGenerator(recipee_dict)
tree.generate_tree(
    "greenhouse_2",
    [Item.NITROGEN_GAS, 
     Item.STEAM, 
     Item.RHENIUM, 
     Item.WATER, 
     Item.HYDROGEN,
    ],
    lambda x : x.name != "log_pyrolise_heavy_oil",
)
tree.draw_graph()