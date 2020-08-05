from menu import Menu
from alphabet import Rotor

word = ""
menu = Menu()
scrambler = []
for i in range(menu.rotorNum):
    scrambler.append(Rotor())
for rotor in scrambler:
    for letter in menu.message:
        word += rotor.get_letter(rotor.get_substitute(rotor.get_index(letter.upper())))
    menu.message = word
    word = ""
print(menu.message)

