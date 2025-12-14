from enum import Enum

from unit_system import EnergyPerProduction

class Item(Enum):
    WOOD = 0
    SAPPLING = 1
    FERTILIZER = 2
    PLANT_BALL = 3
    BIO_CHAFF = 4
    WATER = 5
    FERMENTED_BIOMASS = 6
    METHANE_GAS = 7
    CARBON_DIOXIDE = 8
    AMMONIA = 9
    METHANOL = 10
    ETHANOL = 11
    ACETIC_ACID = 12
    NITROGEN_GAS = 13
    CREOSOTE = 14
    CHARCOAL = 15
    HEAVY_OIL = 16
    WOOD_TAR = 17
    ASHES = 18
    HYDROGEN = 19
    COAL_TAR = 20
    SYNGAS = 21
    RAW_AROMATIC_MIX = 22
    AROMATIC_FEEDSTOCK = 23
    BENZENE = 24
    STEAM = 25
    RHENIUM = 26
    REFORMED_AROMATIC_FEEDSTOCK = 27
    REFORMATE_GAS = 28
    CRACKED_REFORMATE_GAS = 29
    DIMETHYLBENZENE = 30
    TOLUENE = 31
    PHENOL = 32
    SULFURIC_GAS = 33
    SULFURIC_NAPHTA = 34
    SULFURIC_LIGHT_FUEL = 35
    SULFURIC_HEAVY_FUEL = 36
    REFINERY_GAS = 37
    NAPHTA = 38
    LIGHT_FUEL = 39
    HEAVY_FUEL = 40
    HYDROGEN_SULFIDE = 41
    SEVERELY_STEAM_CRACKED_HEAVY_FUEL = 42
    SEVERELY_HYDRO_CRACKED_HEAVY_FUEL = 43
    LIGHTLY_STEAM_CRACKED_HEAVY_FUEL = 44
    LIGHTLY_HYDRO_CRACKED_HEAVY_FUEL = 45
    SEVERELY_STEAM_CRACKED_LIGHT_FUEL = 46
    SEVERELY_HYDRO_CRACKED_LIGHT_FUEL = 47
    LIGHTLY_STEAM_CRACKED_LIGHT_FUEL = 48
    LIGHTLY_HYDRO_CRACKED_LIGHT_FUEL = 49
    SEVERELY_STEAM_CRACKED_NAPHTA = 50
    SEVERELY_HYDRO_CRACKED_NAPHTA = 51
    LIGHTLY_STEAM_CRACKED_NAPHTA = 52
    LIGHTLY_HYDRO_CRACKED_NAPHTA = 53
    SEVERELY_STEAM_CRACKED_REFINERY_GAS = 54
    SEVERELY_HYDRO_CRACKED_REFINERY_GAS = 55
    LIGHTLY_STEAM_CRACKED_REFINERY_GAS = 56
    LIGHTLY_HYDRO_CRACKED_REFINERY_GAS = 57
    ETHYLENE = 58
    ETHANE = 59
    PROPENE = 60
    PROPANE = 61
    BUTADIENE = 62
    BUTENE = 63
    CARBON = 64
    BUTANE = 65
    OCTANE = 66
    HELIUM = 67
    GASOLINE = 68
    NITROUS_OXIDE = 69
    ETHYL_THERBUTYL_ETHER = 70
    HIGH_OCTANE_GASOLINE = 71
    RAW_GASOLINE = 72
    ACETONE = 73
    CUMENE = 74
    OXYGEN = 75
    PHOSPHORIC_ACID = 76
    LPG = 77
    
    def name(self) -> str:
        match self:
            case Item.WOOD: return "WOOD"
            case Item.SAPPLING: return "SAPPLING"
            case Item.FERTILIZER: return "FERTILIZER"
            case Item.PLANT_BALL: return "PLANT_BALL"
            case Item.BIO_CHAFF: return "BIO_CHAFF"
            case Item.WATER: return "WATER"
            case Item.FERMENTED_BIOMASS: return "FERMENTED_BIOMASS"
            case Item.METHANE_GAS: return "METHANE_GAS"
            case Item.CARBON_DIOXIDE: return "CARBON_DIOXIDE"
            case Item.AMMONIA: return "AMMONIA"
            case Item.METHANOL: return "METHANOL"
            case Item.ETHANOL: return "ETHANOL"
            case Item.ACETIC_ACID: return "ACETIC_ACID"
            case Item.NITROGEN_GAS: return "NITROGEN_GAS"
            case Item.CREOSOTE: return "CREOSOTE"
            case Item.CHARCOAL: return "CHARCOAL"
            case Item.HEAVY_OIL: return "HEAVY_OIL"
            case Item.WOOD_TAR: return "WOOD_TAR"
            case Item.ASHES: return "ASHES"
            case Item.HYDROGEN: return "HYDROGEN"
            case Item.COAL_TAR: return "COAL_TAR"
            case Item.SYNGAS: return "SYNGAS"
            case Item.RAW_AROMATIC_MIX: return "RAW_AROMATIC_MIX"
            case Item.AROMATIC_FEEDSTOCK: return "AROMATIC_FEEDSTOCK"
            case Item.BENZENE: return "BENZENE"
            case Item.STEAM: return "STEAM"
            case Item.RHENIUM: return "RHENIUM"
            case Item.REFORMED_AROMATIC_FEEDSTOCK: return "REFORMED_AROMATIC_FEEDSTOCK"
            case Item.REFORMATE_GAS: return "REFORMATE_GAS"
            case Item.CRACKED_REFORMATE_GAS: return "CRACKED_REFORMATE_GAS"
            case Item.DIMETHYLBENZENE: return "DIMETHYLBENZENE"
            case Item.TOLUENE: return "TOLUENE"
            case Item.PHENOL: return "PHENOL"
            case Item.SULFURIC_GAS: return "SULFURIC_GAS"
            case Item.SULFURIC_NAPHTA: return "SULFURIC_NAPHTA"
            case Item.SULFURIC_LIGHT_FUEL: return "SULFURIC_LIGHT_FUEL"
            case Item.SULFURIC_HEAVY_FUEL: return "SULFURIC_HEAVY_FUEL"
            case Item.REFINERY_GAS: return "REFINERY_GAS"
            case Item.NAPHTA: return "NAPHTA"
            case Item.LIGHT_FUEL: return "LIGHT_FUEL"
            case Item.HEAVY_FUEL: return "HEAVY_FUEL"
            case Item.HYDROGEN_SULFIDE: return "HYDROGEN_SULFIDE"
            case Item.SEVERELY_STEAM_CRACKED_HEAVY_FUEL: return "SEVERELY_STEAM_CRACKED_HEAVY_FUEL"
            case Item.SEVERELY_HYDRO_CRACKED_HEAVY_FUEL: return "SEVERELY_HYDRO_CRACKED_HEAVY_FUEL"
            case Item.LIGHTLY_STEAM_CRACKED_HEAVY_FUEL: return "LIGHTLY_STEAM_CRACKED_HEAVY_FUEL"
            case Item.LIGHTLY_HYDRO_CRACKED_HEAVY_FUEL: return "LIGHTLY_HYDRO_CRACKED_HEAVY_FUEL"
            case Item.SEVERELY_STEAM_CRACKED_LIGHT_FUEL: return "SEVERELY_STEAM_CRACKED_LIGHT_FUEL"
            case Item.SEVERELY_HYDRO_CRACKED_LIGHT_FUEL: return "SEVERELY_HYDRO_CRACKED_LIGHT_FUEL"
            case Item.LIGHTLY_STEAM_CRACKED_LIGHT_FUEL: return "LIGHTLY_STEAM_CRACKED_LIGHT_FUEL"
            case Item.LIGHTLY_HYDRO_CRACKED_LIGHT_FUEL: return "LIGHTLY_HYDRO_CRACKED_LIGHT_FUEL"
            case Item.SEVERELY_STEAM_CRACKED_NAPHTA: return "SEVERELY_STEAM_CRACKED_NAPHTA"
            case Item.SEVERELY_HYDRO_CRACKED_NAPHTA: return "SEVERELY_HYDRO_CRACKED_NAPHTA"
            case Item.LIGHTLY_STEAM_CRACKED_NAPHTA: return "LIGHTLY_STEAM_CRACKED_NAPHTA"
            case Item.LIGHTLY_HYDRO_CRACKED_NAPHTA: return "LIGHTLY_HYDRO_CRACKED_NAPHTA"
            case Item.SEVERELY_STEAM_CRACKED_REFINERY_GAS: return "SEVERELY_STEAM_CRACKED_REFINERY_GAS"
            case Item.SEVERELY_HYDRO_CRACKED_REFINERY_GAS: return "SEVERELY_HYDRO_CRACKED_REFINERY_GAS"
            case Item.LIGHTLY_STEAM_CRACKED_REFINERY_GAS: return "LIGHTLY_STEAM_CRACKED_REFINERY_GAS"
            case Item.LIGHTLY_HYDRO_CRACKED_REFINERY_GAS: return "LIGHTLY_HYDRO_CRACKED_REFINERY_GAS"
            case Item.ETHYLENE: return "ETHYLENE"
            case Item.ETHANE: return "ETHANE"
            case Item.PROPENE: return "PROPENE"
            case Item.PROPANE: return "PROPANE"
            case Item.BUTADIENE: return "BUTADIENE"
            case Item.BUTENE: return "BUTENE"
            case Item.CARBON: return "CARBON"
            case Item.BUTANE: return "BUTANE"
            case Item.OCTANE: return "OCTANE"
            case Item.HELIUM: return "HELIUM"
            case Item.GASOLINE: return "GASOLINE"
            case Item.NITROUS_OXIDE: return "NITROUS_OXIDE"
            case Item.ETHYL_THERBUTYL_ETHER: return "ETHYL_THERBUTYL_ETHER"
            case Item.HIGH_OCTANE_GASOLINE: return "HIGH_OCTANE_GASOLINE"
            case Item.RAW_GASOLINE: return "RAW_GASOLINE"
            case Item.ACETONE: return "ACETONE"
            case Item.CUMENE: return "CUMENE"
            case Item.OXYGEN: return "OXYGEN"
            case Item.PHOSPHORIC_ACID: return "PHOSPHORIC_ACID"
            case Item.LPG: return "LPG"


    def is_fuel(self) -> bool:
        match self:
            case Item.BUTANE:
                return True
            case Item.BUTENE:
                return True
            case Item.SULFURIC_GAS:
                return True
            case Item.REFINERY_GAS:
                return True
            case Item.PROPANE:
                return True
            case Item.PROPENE:
                return True
            case Item.LPG:
                return True
            case Item.METHANE_GAS:
                return True
            case Item.BUTADIENE:
                return True
            case Item.BENZENE:
                return True
            case Item.PHENOL:
                return True
            case Item.SYNGAS:
                return True
            case Item.ETHYLENE:
                return True
            case Item.ETHANE:
                return True
            case Item.REFORMATE_GAS:
                return True
            
            case Item.ETHANOL:
                return True
            case Item.LIGHT_FUEL:
                return True
            case Item.NAPHTA:
                return True
            case Item.METHANOL:
                return True
            case Item.HIGH_OCTANE_GASOLINE:
                return True
            case Item.OCTANE:
                return True
        return False
   
    def energy_per_mb(self) -> EnergyPerProduction:
        match self:
            case Item.BUTANE:               return EnergyPerProduction(296)
            case Item.BUTENE:               return EnergyPerProduction(256)
            case Item.SULFURIC_GAS:         return EnergyPerProduction(25)
            case Item.REFINERY_GAS:         return EnergyPerProduction(160)
            case Item.PROPANE:              return EnergyPerProduction(232)
            case Item.PROPENE:              return EnergyPerProduction(192)
            case Item.LPG:                  return EnergyPerProduction(320)
            case Item.METHANE_GAS:          return EnergyPerProduction(112)
            case Item.BUTADIENE:            return EnergyPerProduction(204)
            case Item.BENZENE:              return EnergyPerProduction(352)
            case Item.PHENOL:               return EnergyPerProduction(288)
            case Item.SYNGAS:               return EnergyPerProduction(128)
            case Item.ETHYLENE:             return EnergyPerProduction(128)
            case Item.ETHANE:               return EnergyPerProduction(168)
            case Item.REFORMATE_GAS:        return EnergyPerProduction(384)
            case Item.ETHANOL:              return EnergyPerProduction(192)
            case Item.LIGHT_FUEL:           return EnergyPerProduction(320)
            case Item.NAPHTA:               return EnergyPerProduction(320)
            case Item.METHANOL:             return EnergyPerProduction(64)
            case Item.HIGH_OCTANE_GASOLINE: return EnergyPerProduction(3200)
            case Item.OCTANE:               return EnergyPerProduction(80)
        
        return EnergyPerProduction(0)
