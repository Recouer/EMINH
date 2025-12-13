from enum import Enum

class CoilTier(Enum):
    CUPRONICKEL = 0
    KANTHAL = 1
    NICHROME = 2
    RTM_ALLOY = 3
    HSSG_ALLOY = 4
    NAQUADAH = 5
    TRINIUM = 6
    TRITANIUM = 7

    def energy_consumption(self):
        match self:
            case CoilTier.CUPRONICKEL:
                return 1.0
            case CoilTier.KANTHAL:
                return 0.9
            case CoilTier.NICHROME:
                return 0.8
            case CoilTier.RTM_ALLOY:
                return 0.7
            case CoilTier.HSSG_ALLOY:
                return 0.6
            case CoilTier.NAQUADAH:
                return 0.5
            case CoilTier.TRINIUM:
                return 0.4
            case CoilTier.TRITANIUM:
                return 0.3

    def speedup(self):
        match self:
            case CoilTier.CUPRONICKEL:
                return 0.75
            case CoilTier.KANTHAL:
                return 1.0
            case CoilTier.NICHROME:
                return 1.5
            case CoilTier.RTM_ALLOY:
                return 2.0
            case CoilTier.HSSG_ALLOY:
                return 2.5
            case CoilTier.NAQUADAH:
                return 3.0
            case CoilTier.TRINIUM:
                return 3.5
            case CoilTier.TRITANIUM:
                return 4.0
