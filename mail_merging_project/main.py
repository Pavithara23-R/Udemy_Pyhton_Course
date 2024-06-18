PLACEHOLDER = "[name]"


with open("./Input/Names/invented_names.txt") as names_file:
    names = names_file.readlines()


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_names = name.strip()
        name_letter = letter_content.replace(PLACEHOLDER, stripped_names)
        with open(f"./output/ReadyToSend/letter_for_{stripped_names}.txt", mode="w") as completed_letter:
            completed_letter.write(name_letter)
