import re

class HardCodedCredentials:
    PATTERNS = [
        (re.compile(r"\b(password|passwd|secret_key|api_key|secret)\S*=\S*['\"].+['\"]", re.IGNORECASE), "Potential hardcoded secret (e.g., password, API key)."),
        (re.compile(r"\b(aws_access_key|aws_access_secret|AKIA|ASIA|AIZA)\S*=\S*['\"].+['\"]", re.IGNORECASE), "Potential hardcoded secret (e.g., password, API key).")
    ]