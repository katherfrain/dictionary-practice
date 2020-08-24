phonebook_dict = {
    "Alice": "813-445-9021",
    "Bill": "950-731-2455",
    "Elizabeth": '342-110-7531'
}
print(phonebook_dict["Elizabeth"])
phonebook_dict["Kareem"] = "455-617-9124"
phonebook_dict["Alice"] = "Number not found"
phonebook_dict["Bob"] = "968-489-2154"
print("*" * 20)

for key in phonebook_dict:
    print(f"{key}: {phonebook_dict[key]}\n")