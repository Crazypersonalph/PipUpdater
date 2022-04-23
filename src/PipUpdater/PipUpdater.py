import subprocess

packages = subprocess.run(["pip", "list", "command"], capture_output=True, text=True)
amount_of_packages = packages.stdout.count("\n") - 3
print("You have {} packages installed.".format(amount_of_packages))
print("This can only be used to upgrade all of your packages at once.")
print("I would not recommend using this tool if you have anything mission critical, otherwise, some programs may break")

def input_warning():
    warning = input("Are you sure you want to upgrade all of your packages? (y/n)")
    if warning == "y":
        # Need to actually make it upgrade packages
        big_string = " ".join(packages.stdout.split())
        packs_1 = big_string.split(' ', 1)[1]
        packs_2 = packs_1.split(' ', 1)[1]
        packs_3 = packs_2.split(' ', 1)[1]
        packs_4 = packs_3.split(' ', 1)[1]
        print(packs_4)

    elif warning == "n":
        print("Exiting...")
        exit()

    else:
        print("Please enter a valid input.\n")
        return input_warning()

input_warning()
