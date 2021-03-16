import random
from contents import *
import sys
class Game():
     def  __init__(self, word):
         self.word = word
         self.state = 0
         self.animations = HANGMAN_PICS
         self.found_letters = []
     def inc_state(self):
         self.state += 1
     def show(self):
         print(self.animations[self.state])
         output = ""
         for letter in self.word:
             if letter in self.found_letters:
                 output += letter
             else:
                 output += "_"
         print(output)
     def check_letter(self, letter):
         if letter in self.word:
             self.found_letters.append(letter)
             print(f"Letter {letter} is in magic word\n")
             self.show()
         else:
             self.inc_state()
             print(f"letter {letter} is not magic word\n")
             self.show()
     def end_game(self):
         if self.state == 6:
             print("End of the Game")
             return True
         else:
             return False
     def you_win_maybe(self):
         if len(self.found_letters) == len(set(self.word)):
             print("You win")
             return True
         else:
             return False
def continue_game():
    print("Категории:", ", ".join(words_.keys()))
    categeory_input = input("Введите категорию")
    magic_word = random.choice(words_.get(categeory_input))
    game1 = Game(magic_word)
    while (not game1.end_game() and not game1.you_win_maybe()):
        letter_in = input("Enter next letter")
        game1.check_letter(letter_in)
    a = input("Хотите продолжить?").lower().strip()
    if a == "yes":
        continue_game()
    else:
        sys.exit(0)
continue_game()

