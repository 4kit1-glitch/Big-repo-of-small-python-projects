import re

def perform_strip(text: str, pattern) -> str:
    if pattern is None:
        strip_pattern = re.compile(r'^\s+|\s+$')
        return strip_pattern.sub("", text)
    charset = re.escape(pattern)
    strip_pattern = re.compile(rf'^[{charset}]+|[{charset}]+$')

    return strip_pattern.sub("", text)

def restrip(text: str, pattern= None):
    return perform_strip(text, pattern)




print(restrip("-----------------.............hello...........-----------", ".-"))

print(restrip("cabacbabababababhellobat", "ab"))