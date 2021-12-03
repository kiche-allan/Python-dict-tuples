# dictionaries are used to store information that come as key value pairs


customer = {
    "name": "Allan Kiche",
    "age": 30,
    "is_verified": True
}
#  get value
print(customer.get("name1", "Jan 2021"))

Phone = input ("Phone:")
digits_mapping ={
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output =""
for ch in Phone:
     output += digits_mapping.get(ch, "!") + " "
print(output)