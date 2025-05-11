import re

class DangerousFunctions:
    PATTERNS = [
        (re.compile(r"\beval\s*\("), "Potential use of 'eval()', which can be dangerous if used with untrusted input."),
        (re.compile(r"\bexec\s*\("), "Potential use of 'exec()', which can execute arbitrary Python code."),
    ]