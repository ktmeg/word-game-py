
with open ('words.txt') as words:
  lines = words 

class Game:
  def __init__(self):
  # self.play_game = 
    self.player = Player("Kat")

  
  print(words.closed) 

  def play(self):
    pass

class Word:
  def __init__(self):
    print('init method')
  
  def __enter__(self):
    print('entering word file')

  def __exit__(self, exc_info):
    print('exit words.txt')

with open('words.txt', 'w') as f:
  words = f.read()

  
class Player:
  def __init__(self, name):
    self.name = name
    self.score = score 
    self.guess = guess

  def __str__(self):
    return f'{self.name}'
  
  pass




game = Game()
# game.play()