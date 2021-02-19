def common_print(kind, data):
    print(f"{kind}: {data}")

def print_list(data, kind):
    interpolation = f"My name is {data[0]} and my mang inasal rice record is: {data[1]}"
    common_print(kind, interpolation)

def print_struct(data):
    interpolation = f"My name is {data['name']} and my mang inasal rice record is: {data['record']}"
    common_print("dictionary", interpolation)

print_list(("Normz",3,), "tuple")
print_list(["Normz",3], "list")
print_list(list({3, "Normz"}), "set")
print_struct({"name": "Normz", "record": 3})
