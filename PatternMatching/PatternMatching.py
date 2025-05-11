import os, re
from Utils import Utils
from PatternTypes import PatternTypes

class PatternMatching:
    def Match(self, type=None, src=None, patternType=None):
        """        
        Args:
            type (str): SIMPLE, COMPLEX
                * SIMPLE: Search for strings & regex patterns
                * COMPLEX: Syntax-Aware searching
            src (str): Path to scan
            matchFor (PatternType): Match for specific type for vulnerability(ALL, SQLI, XSS, CRYPTO).
                * ALL: Includes SQLI, XSS, CRYPTO
                * SQL: Search for SQLI
                * XSS: Search for Cross Site Scripting
                * CRYPTO: Weak Cryptographic 
        """
        # Validate all parameters are given
        if type == None:
            Utils().print_error(
                className=self.__class__.__name__,
                classMethod=self.Match.__name__,
                error=f"parameter(type:{type}) is missing.",
                usage=self.Match.__doc__
            )
            exit(1)
        
        elif src == None:
            Utils().print_error(
                className=self.__class__.__name__,
                classMethod=self.Match.__name__,
                error=f"parameter(src:{src}) is missing.",
                usage=self.Match.__doc__
            )
            exit(1)

        elif patternType == None or patternType not in PatternTypes:
            Utils().print_error(
                className=self.__class__.__name__,
                classMethod=self.Match.__name__,
                error=f"parameter(patternType:{patternType}) is missing.",
                usage=self.Match.__doc__
            )
            exit(1)

        if type == "SIMPLE":
            # self.__simple__(src, patternType)
            self.Simple().scan(src, patternType)
        
        elif type == "COMPLEX":
            self.__complex__()
        else:
            Utils().print_error(
                className=self.__class__.__name__,
                classMethod=self.Match.__name__,
                error="parameter(patternType) not recognized.",
                usage=self.Match.__doc__
            )
            exit(1)

    class Simple:
        findings = []
        max_scan_file_size = 10

        def __init__(self):
            self.findings = []

        def scan(self, src, patternType):
            """        
            Args:
                src (str): Path to scan
                patternType (PatternType): Match for specific type for vulnerability(ALL, SQLI, XSS, CRYPTO).
                    * ALL: Includes SQLI, XSS, CRYPTO
                    * SQL: Search for SQLI
                    * XSS: Search for Cross Site Scripting
                    * CRYPTO: Weak Cryptographic 
            """
            VULNERABILITY_PATTERNS = PatternTypes(patternType).getPatterns(patternType)
            for pattern in VULNERABILITY_PATTERNS:
                print(pattern)

            if os.path.isfile(src):
                self.scan_file(src, VULNERABILITY_PATTERNS)
            else:
                for dir_path, _, file_names in os.walk(src):
                    for file_name in file_names:
                        file_path = os.path.join(dir_path, file_name)
                        self.scan_file(file_path, VULNERABILITY_PATTERNS)
            
            Utils().print_findings(self.findings)
        
        def scan_file(self, src, VULNERABILITY_PATTERNS):
            print(f"Scanning: {src}")
            file_size_mb = os.path.getsize(src) / (1024 * 1024)
            if file_size_mb < self.max_scan_file_size:
                with open(src) as f:
                    for line_number, line_content in enumerate(f, 1):
                        for pattern, description in VULNERABILITY_PATTERNS:
                            if pattern.search(line_content):
                                self.findings.append({
                                    "line_number": line_number,
                                    "line_content": line_content.strip(),
                                    "description": description,
                                    "pattern_matched": pattern.pattern,
                                    "file_path": src
                                })
            else:
                print(f"Error: only scan files less than {self.max_scan_file_size}")


    def __complex__(self): pass
