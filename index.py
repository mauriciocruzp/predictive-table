import re

regex = re.compile(r"^[a-z]+$")

if regex.match("a2_A"):
    print("match")
