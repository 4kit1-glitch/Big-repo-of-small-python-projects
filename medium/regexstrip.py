import re

def restrip(text: str, pattern= None):
    if pattern is None:
        pat = re.compile(r'(^\s*)?(\s*$)?')
    else:
        pat = re.compile(rf'^(?:{re.escape(pattern)})+|(?:{re.escape(pattern)}+$)')
    return pat.sub("", text)
