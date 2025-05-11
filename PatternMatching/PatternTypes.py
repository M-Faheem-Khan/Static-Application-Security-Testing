from enum import Enum
from patterns.DangerousFunctions import DangerousFunctions
from patterns.HardCodedCredentials import HardCodedCredentials
from patterns.InsecureServerDefaults import InsecureServerDefaults

class PatternTypes(Enum):
    ALL = 0
    DANGEROUS_FUNCTIONS = 1
    HARDCODED_CREDENTIALS = 2
    INSECURE_SERVER_DEFAULTS = 3


    def getPatterns(self, patternType):
        patterns = []
        if patternType == PatternTypes.ALL:
            patterns = DangerousFunctions.PATTERNS + HardCodedCredentials.PATTERNS + InsecureServerDefaults.PATTERNS

        elif patternType == PatternTypes.DANGEROUS_FUNCTIONS:
            patterns = DangerousFunctions.PATTERNS

        elif patternType == PatternTypes.HARDCODED_CREDENTIALS:
            patterns = HardCodedCredentials.PATTERNS

        elif patternType == PatternTypes.INSECURE_SERVER_DEFAULTS:
            patterns = InsecureServerDefaults.PATTERNS
        
        return patterns

# EOF