'''
    Dice Bag System
    Anthony Castillo
    12/18/2022
'''

from bagOfDice_Imp import BagOfDice

def main():
    bag1 = BagOfDice()
    bag1.standardDiceSet()
    print('Current dice in the bag: ', str(bag1))
    print(bag1.rollDice())
    print(bag1.rollDice(20))
    print('The last dice roll was ', bag1.getPreviousRoll())
    print('First roll ', bag1.rollDice(20, 4))
    print('The last dice roll was ', bag1.getPreviousRoll())
    print('Second roll ', bag1.rollDice(7, 20))
    print('The last dice roll was ', bag1.getPreviousRoll())
    print('All of the dice results that have been rolled: ', bag1.getHistory())
    print(bag1.help())
    print(bag1.removeDice(6))
    #print(bag1.removeDice(6)) # Gives an error if there is no dice in the bag with the same number of faces.
    print(bag1.emptyBag())
    print(str(bag1))
    bag1.standardDiceSet()
    print(str(bag1))
# end main()

main()