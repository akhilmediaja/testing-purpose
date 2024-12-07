def get_full_name(fisrt_name, last_name):
    full_name = fisrt_name.title() + " " + last_name.title()
    return full_name

print()
print(get_full_name(input("enter first name : "), input("enter last name : ")))