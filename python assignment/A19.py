def new_string(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str ##it will return IS + inputed str(spc)
print(new_string("syntax"))
print(new_string("program"))
