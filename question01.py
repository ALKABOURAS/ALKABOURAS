import re

f=open("weather.txt", mode="r", encoding="utf8")
content=f.read()
f.close()
reg=3
match reg:
    case 1:
        "[0-9]"
    case 2:
        "[0-9]+\.?[0-9]?"
    case 3:
        ""
pattern=re.compile(reg)  # <-- Εδώ βάζουμε το RE
result=pattern.findall(content)
print(result)
print(len(result))
