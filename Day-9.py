definition = {
    "bug":"an error in program",
    "Function":"a piece of code"
}

# print(definition)

#adding 
definition["loop"] = "a piece of code running multiple times"
# print(definition)

#editing
definition["loop"] = "keyword to run a code multiple times"

# print(definition)

for key in definition:
    print(key)
    print(definition[key])

#wiping out dictionary
definition = {}