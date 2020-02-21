
import random

# class Words:

#   def __init__(self, word):
#     self.word = word 

#   def __str__(self):
#     word = print(random.choice(words))

class Game:
  def __init__(self):
    self.player = Player('player1')
    self.word = self.choose_word()
    self.blanks = self.start_game(self.word)

  def choose_word(self):
    with open('words.txt', 'r') as f:
      words = f.readlines()
    self.word = random.choice(words)
    self.word = self.word.lower()
    print (self.word)
    return self.word
    # s = set 
    # while len(s)>0:
    #     s.remove(random.choice(list(s)))

  # def blank_word(self, blanks):
  #   self.blanks = list('_'*len(self.word.strip()))
  #   # print(self.blanks)
  #   # return "Game has started. Your word is:", f"{self.blanks}"
  #   return
  
  def start_game(self, blanks):
    choice = input (f'Hello, {self.player.name}. Are you ready to play? (y)/(n)')
    if choice == 'y': 
      self.blanks = list('_'*len(self.word.strip()))
      print(self.blanks)
      return "Game has started. Your word is:", f"{self.blanks}"
    
  
  
  # def show_word_prompt(self, word):
  #   print("Game has started. Your word is:", f"{blank_word}")
   
  
  def guess_letter(self):
    guess = input('What letter would you like to guess?')


  # def play(self):



class Player:
  def __init__(self, name):
    self.name = name
    self.score = 0 
    # self.guess = guess
  
  def __str__(self):
    name = input('What is your name?')
    return f'{self.name}'
  
game = Game()
game.start_game()






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