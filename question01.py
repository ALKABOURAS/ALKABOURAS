import re

f=open("weather.txt", mode="r", encoding="utf8")
content=f.read()
f.close()
reg=8
match reg:
    case 1:
        pattern=re.compile ("[0-9]")
    case 2:
        pattern=re.compile("[0-9]+\.?[0-9]?")
    case 3:
        pattern=re.compile("[0-9]+\.?[0-9]?\s[m]+")  # <-- Εδώ βάζουμε το RE
    case 4:
        pattern=re.compile("\((.*?)\)")
    case 5:
        pattern=re.compile("[0-3]?[0-9]\/[01]?[0-9]\/[012]?[0-9]?[0-9][0-9]")
    case 6:
        pattern=re.compile("[0-ω]+\s[0-3]?[0-9]\/[01]?[0-9]\/[012]?[0-9]?[0-9][0-9]")
    case 7:
        pattern=re.compile("[0-ω]*[άήόύώέίϋϊΆΉΌΎΏΈΊ][0-ω]*")
    case 8:
        pattern=re.compile("[Α-ΩΆΉΌΎΏΈΊ][0-ωάήόύώέίϋϊ][0-ωάήόύώέίϋϊ]+")
result=pattern.findall(content)
print(result)
print(len(result))
