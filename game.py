
import random


class Game:
  def __init__(self):
    self.player = Player('Player1')
    # self.blanks = self.start_game()
    self.word = self.choose_word()
    # self.guess = guess
    self.guesses_left = 8
    self.blanks = []
    
    

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
    print("start_game was called")
    choice = input (f'Hello, {self.player.name}. Are you ready to play? (y)/(n)')
    if choice == 'y':
      self.blanks = list('_'*len(self.word.strip()))
      self.blanks = ' '.join(self.blanks)
      print((f'Game has started. Your word is:{self.blanks}'))
      return self.play_game()
    elif choice == 'n':
      print('See you later...')
      return  
  # needs to stop running function is answer is 'n'

  def play_game(self):
    print("play_game was called")
    while self.guesses_left > 0 and not len(''.join(self.blanks)) == 0:
      self.guess()
      if len("".join(self.blanks)) == 0:
        print("You Win!")
      else:
        self.guesses_left -= 1
        if self.guesses_left < 0:
          print("Game Over!")
    #   print('Both conditions met')
    return

      
  def guess(self):
    choice = input('What letter would you like to guess?')
    if len(choice) > 1:
      print ('Please choose one letter!')
    return self.reveal_letters(choice)

  # def reveal_letters(self, letter, guesses):
  #   if letter in guesses:
  #     return letter
  #   else:
  #     return "_"
  # [reveal_letters(letter, current_guesses)
  #   for letter in self.blanks]
          

    
  def reveal_letters(self, letter):
    print("reveal letters was called")
    if letter in self.blanks:
      while letter in self.blanks:
        i = self.blanks.index(letter)
        self.blanks[i] = letter
        self.blanks[i] = ""
        return self.blanks   


class Player:
  def __init__(self, name):
    self.name = name
    self.score = 0
  
  # def name_entry(self, name):
  #   name = input('What is your name?')
  #   print (f'{self.name}')
  #   return f'{self.name}'
  
game = Game()
game.start_game()
# game.reveal_letters()




