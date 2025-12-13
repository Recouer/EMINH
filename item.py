from enum import Enum

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
   
    def fuel_per_mb(self) -> int:
        match self:
            case Item.BUTANE:
                return 296
            case Item.BUTENE:
                return 256
            case Item.SULFURIC_GAS:
                return 25
            case Item.REFINERY_GAS:
                return 160
            case Item.PROPANE:
                return 232
            case Item.PROPENE:
                return 192
            case Item.LPG:
                return 320
            case Item.METHANE_GAS:
                return 112
            case Item.BUTADIENE:
                return 204
            case Item.BENZENE:
                return 352
            case Item.PHENOL:
                return 288
            case Item.SYNGAS:
                return 128
            case Item.ETHYLENE:
                return 128
            case Item.ETHANE:
                return 168
            case Item.REFORMATE_GAS:
                return 384
            
            case Item.ETHANOL:
                return 192
            case Item.LIGHT_FUEL:
                return 320
            case Item.NAPHTA:
                return 320
            case Item.METHANOL:
                return 64
            case Item.HIGH_OCTANE_GASOLINE:
                return 3200
            case Item.OCTANE:
                return 80
        
        return 0
