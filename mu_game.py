__author__ = 'Tatiana'
# Implementation of a logic game from Douglas R. Hofstadter's "Godel, Escher, Bach."
# Taken from chapter 1 of the 20th anniversary edition (ISBN 0-465-02656-7).
# Starting from MI, try to make MU. Apply only one of four axiomatic rules from the system.

import sys


def welcome_message():
    print("\nWelcome to the MU game. Goal: Make MU by applying rules to MI."
          "\nTo see available rules, type RULES. To see your current strings, type SHOW. "
          "To quit, type QUIT.")


def print_rules():
    print("\nRule 1: If you possess a string whose last letter is I, you can add on a U at the end."
          "\nRule 2: Suppose you have Mx. Then you may add Mxx to your collection."
          "\nRule 3: If III occurs in one of the strings in your collection, "
          "you may make a new string with U in place of III."
          "\nRule 4: If UU occurs inside one of your strings, you can drop it.\n")


def print_list():
    for string in string_list:
        print(string.upper())


def rule_one(string):
    return string + 'u'


def rule_two(string):
    return string + string[1:len(str(string))]


def rule_three(string):
    return string.replace('iii', 'u', 1)


def rule_four(string):
    return string.replace('uu', '', 1)


def get_string():
    new_string = input("Which string? ")
    if new_string in string_list:
        return new_string.lower()
    else:
        get_string()

string_list = ['mi']
welcome_message()

while 'mu' not in string_list:
    action = input("Rule 1, Rule 2, Rule 3, Rule 4, [R]ules, [S]how, [Q]uit? ").lower()

    if action == "rules" or action == 'r':
        print_rules()
    elif action == "show" or action == 's':
        print_list()
    elif action == 'quit' or action == 'q':
        sys.exit()
    if action in '1234':
        my_string = get_string()
        if action == '1' and my_string:
            if my_string[len(my_string) - 1] == 'i':
                string_list.append(rule_one(my_string))
                print(rule_one(my_string) + ' added!')
            else:
                print("That string does not end in I!")
        elif action == '2' and my_string:
            string_list.append(rule_two(my_string))
            print(rule_two(my_string) + ' added!')
        elif action == '3' and my_string:
            if 'iii' in my_string:
                string_list.append(rule_three(my_string))
                print(rule_three(my_string) + ' added!')
            else:
                print("That string does not contain III!")
        elif action == '4' and my_string:
            if 'uu' in my_string:
                string_list.append(rule_four(my_string))
                print(rule_four(my_string) + ' added!')
            else:
                print("That string does not contain UU!")
