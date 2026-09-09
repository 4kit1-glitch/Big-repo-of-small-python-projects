import pyperclip

txt = pyperclip.paste()

lines_text = txt.split("\n")

new_text = ""

for i, line in enumerate(lines_text):
    line = "* " + line
    lines_text[i] = line

txt = "\n".join(lines_text)

pyperclip.copy(txt)