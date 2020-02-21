
import random

with open('words.txt', 'r') as f:
  words = f.readlines()

# class Words:

#   def __init__(self, word):
#     self.word = word 

#   def __str__(self):
#     word = print(random.choice(words))

class Game:
  def __init__(self):
  # self.play_game = 
    self.player = Player()

  def print_word(self):
    word = random.chice(words)
    # s = set 
    # while len(s)>0:
    #     s.remove(random.choice(list(s)))
  
  def start_game(self, word):
    self.word = print_word

  # def play(self):



class Player:
  def __init__(self, name):
    self.name = name
    self.score = 0 
    self.guess = guess
  
  def __str__(self):
    name = input('What is your name?')
    return f'{self.name}'
  
  def start_game(self, game):
    choice = input('Hello, {self.name}. Are you ready to play?' (y)/(n))
    if choice == 'y': start_game


  def guess_letter(self):
    guess = input('What letter would you like to guess?')


game = Game()
# game.play()





# Can I use this to add exceptions for word length??

# class Word:
#   def __init__(self):
#     print('init method')
  
#   def __enter__(self):
#     print('entering word file')

#   def __exit__(self, exc_info):
#     print('exit words.txt')

#   with open('words.txt', 'r') as f:
#     words = f.read()