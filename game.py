
import random


class Game:
  def __init__(self):
    self.player = Player('player1')
    self.word = self.choose_word()
    self.blanks = self.start_game()
    self.guesses_left = 8

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

  def start_game(self):
    # self.blanks = self.word
    choice = input (f'Hello, {self.player.name}. Are you ready to play? (y)/(n)')
    if choice == 'y': 
      self.blanks = list('_'*len(self.word.strip()))
      print(self.blanks)
      return "Game has started. Your word is:", f"{self.blanks}"
    elif input == 'n':
      return "See you later..."

  def ask_letter(self, char):
    choice = input('What letter would you like to guess?')
    if choice == len(char) > 1:
      print ('Please choose one letter!')

  def reveal_letters(self, char):
    if char in self.word:
      while char in self.word:
        i = self.word.index(char)
        self.blanks[i] = char
        self.word[i] = ""
      if len("".join(self.word)) == 0:
        return "You Win!"
      else:
        self.guesses_left -= 1
        if self.guesses_left < 0:
          return ("Game Over!")

  # def guesses_left(self):
  #   self.guesses_left -= 1
  #   if self.guesses_left < 0:
  #     return ("Game Over!")


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
