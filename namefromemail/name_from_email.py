# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

email = input("Give me your email adress: ")

def name_from_email(email):
    name = email.split("@")
    split_name = name[0].split(".")
    split_name.reverse()
    return (' '.join(split_name))

print(name_from_email(email))
