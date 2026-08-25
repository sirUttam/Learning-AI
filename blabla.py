hellos = ["uttam", "kumar", "singh", "is", "a", "good", "boy"]

names =[]

for i, hello in enumerate(hellos, start=4):
    res = {
        "index": i,
        "name": hello
    }
    names.append(res)

print(names)

