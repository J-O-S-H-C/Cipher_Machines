from random import randint
import string

word = ""
letters = list(input())

class Alphabet:
    def __init__(self):
        self.alphabet = string.ascii_uppercase
    def get_index(self, letter):
        return self.alphabet.index(letter)
    def get_letter(self, index):
        return self.alphabet[index]

class Rotor(Alphabet):
    def __init__(self):
        super().__init__()
        self.offset = randint(0,25)
        #make switch if Historic is active
        self.IC = ["D","M","T","W","S","I","L","R","U","Y","Q","N","K","F","E","J","C","A","Z","B","P","G","X","O","H","V"]
    def get_substitute(self, index):
        index += self.offset
        if (index > 25):
            index -= 25
        return index
    def get_predefined(self,index):
        return self.IC[index]

class Menu:
    def __init__(self):
        print("How many rotors?")
        self.rotorNum = int(input())

menu = Menu()
scrambler = []
for i in range(menu.rotorNum):
    scrambler.append(Rotor())
for rotor in scrambler:
    for letter in letters:
        word += rotor.get_letter(rotor.get_substitute(rotor.get_index(letter.upper())))
    letters = word
    word = ""
print(letters)

