class Player:
  def __init__(self, game, token):
    self._token = token
    self._game = game
    self._my_turn = False

  def make_play(self, i, j):
    self._game.make_move(i,j,self.get_token())
  
  def get_my_turn(self):
    return self._my_turn

  def set_my_turn(self, turn):
    self._my_turn = turn

  def get_token(self):
    return self._token

  def set_token(self, token):
    self._token = token

  def verify_range_input(self, number):
    if (number >= 0) and (number <= 2):
      return True
    else:
      return False

  def get_player_input(self):
    try:
      i = int(input("Digite o numero da linha: "))
      j = int(input("Digite o numero da coluna: "))
      i = i-1
      j = j-1
      if self.verify_range_input(i) and self.verify_range_input(j):
        return i,j
      else:
        print("O valor deve ser entre 1 e 3")
        input("Aperte ENTER para continuar!")
        return self.get_player_input()
    except:
      print("Entrada Inválida!")
      input("Aperte ENTER para continuar!")
      return self.get_player_input()