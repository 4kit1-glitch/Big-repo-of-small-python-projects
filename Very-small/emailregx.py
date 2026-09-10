import re
import pyperclip

email_re = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    \.[a-zA-Z]{2,4}
)''', re.VERBOSE)

text = str(pyperclip.paste())
match = email_re.findall(text)

text = "\n".join(match)

if len(match) > 0:
    pyperclip.copy(text)
    print("copied to clipboard")
    print(text)
else:
    print("no match found")
