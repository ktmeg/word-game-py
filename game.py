
import random


class Game:
  def __init__(self):
    self.player = Player('Player1')
    # self.blanks = self.start_game()
    self.word = self.choose_word()
    self.guesses_left = 8git 
    

  def choose_word(self):
    with open('words.txt', 'r') as f:
      words = f.readlines()
    self.word = random.choice(words)
    self.word = self.word.lower()
    # print (self.word)
    return self.word
    # s = set 
    # while len(s)>0:
    #     s.remove(random.choice(list(s)))

  def start_game(self):
    choice = input (f'Hello, {self.player.name}. Are you ready to play? (y)/(n)')
    if choice == 'y':
      self.blanks = list('_'*len(self.word.strip()))
      print((f'Game has started. Your word is:{self.blanks}'))
    elif choice == 'n':
      print('See you later...')
      return choice 
        
  def ask_letter(self, letter):
    self.letter = letter
    choice = input('What letter would you like to guess?')
    if choice == len(letter) > 1:
      print ('Please choose one letter!')
      return choice

  def reveal_letters(self, letter):
    self.letter = letter
    if letter in self.word:
      while letter in self.word:
        i = self.word.index(letter)
        self.blanks[i] = letter
        self.word[i] = ""
      if len("".join(self.word)) == 0:
        print("You Win!")
      else:
        self.guesses_left -= 1
        if self.guesses_left < 0:
          print("Game Over!")

  # def guesses_left(self):
  #   self.guesses_left -= 1
  #   if self.guesses_left < 0:
  #     return ("Game Over!")


class Player:
  def __init__(self, name):
    self.name = name
    self.score = 0
  
  def name_entry(self, name):
    name = input('What is your name?')
    print (f'{self.name}')
    return f'{self.name}'
  
game = Game()
game.start_game()
game.ask_letter()


