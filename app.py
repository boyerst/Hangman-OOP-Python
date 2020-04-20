from data.wordbank import wordbank
import sys
import random





print(random.choice(wordbank))

  





game_play = True


class Word():

  def __init__(self, chosen_word):

    self.chosen_word = chosen_word

    self.num_letters = (len(chosen_word))

    # self.guessed = False
    self.guessed = []

    self.remaining_guesses = 8

    self.correct = 0





#   def print_word(self):
#     display_letters = " ".join([letter if letter in self.guessed else "_" in self.chosen_word])
#     print(display_letters)




