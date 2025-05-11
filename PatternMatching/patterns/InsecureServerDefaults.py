import re

class InsecureServerDefaults:
    PATTERNS = [
        (re.compile(r"\bDEBUG\s*=\s*True", re.IGNORECASE), "Debugging flag 'DEBUG = True' might be enabled in a production environment."),
    ]