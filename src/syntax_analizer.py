import re

predictive_table = {
    "S": [{"input": re.compile("function"), "production": ["F", "N", "PM"]}],
    "F": [{"input": re.compile("function"), "production": ["function"]}],
    "PM": [{"input": re.compile("\("), "production": ["PA", "PL", "PC"]}],
    "PA": [{"input": re.compile("\("), "production": ["("]}],
    "PC": [{"input": re.compile("\)"), "production": [")"]}],
    "PL": [{"input": re.compile("var"), "production": ["V", "X", "LT"]}],
    "V": [{"input": re.compile("var"), "production": ["var"]}],
    "X": [{"input": re.compile("[a-z]"), "production": ["N", ":", "T"]}],
    "N": [{"input": re.compile("[a-z]"), "production": ["L", "RN"]}],
    "RN": [
        {"input": re.compile("[a-z]"), "production": ["L", "RN"]},
        {"input": re.compile(":"), "production": []},
        {"input": re.compile("\("), "production": []},
    ],
    "L": [
        {
            "input": re.compile("[a-z]"),
            "production": ["same"],
        }
    ],
    "T": [
        {
            "input": re.compile("boolean"),
            "production": ["boolean"],
        },
        {
            "input": re.compile("string"),
            "production": ["string"],
        },
    ],
    "LT": [
        {"input": re.compile("\)"), "production": []},
        {"input": re.compile(";"), "production": ["P", "X", "LT"]},
    ],
    "P": [{"input": re.compile(";"), "production": [";"]}],
}


def separate(input):
    parts = re.findall(r"\w+|\S", input)
    return parts


def analize(input):
    stack = ["$", "S"]
    history = ""
    input = separate(input)
    for i in range(len(input)):
        while True:
            history += f"{stack}\n"
            if len(stack) == 0:
                return False
            if len(input) == 0:
                return False
            if stack[-1] == input[0]:
                stack.pop()
                input.pop(0)
                break
            if stack[-1] in predictive_table:
                for production in predictive_table[stack[-1]]:
                    if production["input"].match(input[0]):
                        stack.pop()
                        for i in range(len(production["production"]) - 1, -1, -1):
                            if production["production"][i] != "same":
                                stack.append(production["production"][i])
                            else:
                                stack.append(input[0])
                        break
                else:
                    return False
            else:
                return False
    history += f"{stack}"
    print(history)

    if stack[-1] == "$" and len(input) == 0:
        return True, history
    return False, history
