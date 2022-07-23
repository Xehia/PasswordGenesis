# Ask for a victim's information
name = input("What is your victim's name? ")
surname = input("What is your victim's surname? ")
dob = input("What is your victim's date of birth? (GGMMYYYY) > ")

dob_g = int(dob[0:2])
dob_m = int(dob[2:4])
dob_y = int(dob[4:8])

specialCharacters = "!?@#$%^&*()_+"

def check_date(dob):
    if int(dob_g) > 31 or int(dob_m) > 12 or int(dob_y) > 2022 or len(dob) != 8:
        print("Invalid date of birth")
        exit()
    else:
        return True

def main():
    check_date(dob)

    passwords = []
    # Generate a password combining the victim's name, surname and date of birth
    for char in specialCharacters:
        passwords.append(name + dob[4:8] + char)
        passwords.append(name + dob[6:8] + char)
        passwords.append(surname + dob[4:8] + char)
        passwords.append(surname + dob[6:8] + char)
        passwords.append(name + surname + dob[4:8] + char)
        passwords.append(name + surname + dob[6:8] + char)
        passwords.append(surname + name + dob[4:8] + char)
        passwords.append(surname + name + dob[6:8] + char)


    # Save the password to a file
    with open(f"{name}.txt", "w") as file:
        for password in passwords:
            file.write(password)
            if password != passwords[-1]:
                file.write("\n")
    
    print(f"Generated {len(passwords)} passwords for {name} {surname} in {name}.txt")

main()