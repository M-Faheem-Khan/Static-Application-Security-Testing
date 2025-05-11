from PatternTypes import PatternTypes
from PatternMatching import PatternMatching

def main():
    PatternMatching().Match(
        type = "SIMPLE",
        src = "tests",
        patternType=PatternTypes.ALL
    )

if __name__ == "__main__":
    main()

# EOF