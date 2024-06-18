import pandas
#Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dic = {row.letter: row.code for (index, row) in data.iterrows()}
#print(data_dic)

#Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():

    word = input("Enter the word:").upper()
    try:
        output_list = [data_dic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generate_phonetic()
    else:
        print(output_list)
generate_phonetic()