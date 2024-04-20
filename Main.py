import os
os.getcwd()

adjective_1 = input("Enter in an adjective: ")
adjective_2 = input("Enter in another adjective: ")
adjective_3 = input("Enter in another adjective: ")
first_name = input('Enter in a First Name: ')
past_Tense_Verb = input("Enter in a Past Tense Verb: ")
past_Tense_Verb_2 = input("Enter in another Past Tense Verb: ")
plural_noun_1 = input("Enter a Plural Noun: ")
plural_noun_2 = input("Enter another Plural Noun: ")
plural_noun_3 = input("Enter another Plural Noun: ")
large_animal = input("Enter a Large Animal: ")
small_animal = input("Enter a Small Animal: ")
girl_name = input("Enter in a girl's name: ")
number_100 = input("Pick a number 1-100: ")
number = input("Another number 1-100: ")
last_number = input("Lastly another number 1-100: ")

print("I, the", adjective_1, "and", adjective_2, first_name)
print("has", past_Tense_Verb + "'s", adjective_3, past_Tense_Verb_2 + "'s", adjective_2)
print("sister and plans to steal her", adjective_1, plural_noun_1 + "!")
print("What are a", large_animal, "and backpacking", small_animal, "to do?")
print("Before you can help", girl_name + ".", "you'll have to collect the", adjective_3,
      plural_noun_2, "and", adjective_2, plural_noun_3, "that open up the", number_100, "worlds connected to",
      first_name, "lair.")
print("There are", number, plural_noun_2, "and", last_number, plural_noun_1,
      "in the game, along with hundreds of other goodies for you to find.")
print("Press Enter to exit.")
input()
