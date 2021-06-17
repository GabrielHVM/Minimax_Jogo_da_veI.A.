white = " "
class Minimax:
  def __init__(self,game,token):
    self._game = game
    self._token = token
    self._current_token = token
    self._my_turn = False
    self.map_score = {
      "DRAW":0,
      "X":1,
      "O":-1
    } 
  def make_play(self, i ,j):
    self._game.make_move(i,j,self.get_token())

  def get_my_turn(self):
    return self._my_turn

  def set_my_turn(self, turn):
    self._my_turn = turn

  def get_token(self):
    return self._token

  def set_token(self, token):
    self._token = token

  def best_moviment(self):
    player = self.get_token()
    empty_spaces = self._game.get_empty_places()
    best_value = None
    best_moviment = None
    for possibility in empty_spaces:
      line_of_possibility = possibility[0]
      column_of_possibility = possibility[1]
      #print(f"Possivel jogada = {line_of_possibility, column_of_possibility}")
      self._game.make_move(line_of_possibility, column_of_possibility, player)
      #self._game.make_move(line_of_possibility, column_of_possibility, self._get_current_token())
      #self.make_play(line_of_possibility, column_of_possibility)
      value_of_nodes = self.run_possibilities(player)
      self._game.make_move(line_of_possibility, column_of_possibility, white)
      if best_value is None:
        best_value = value_of_nodes
        best_moviment = possibility
      elif player == "X":
        if value_of_nodes > best_value:
          best_value = self.max_value(value_of_nodes, best_value)
          best_moviment = possibility
      elif player == "O":
        if value_of_nodes < best_value:
          best_value = self.min_value(value_of_nodes, best_value)
          best_moviment = possibility
    return best_moviment[0], best_moviment[1]

  def _get_current_token(self):
    return self._current_token
  
  def _set_current_token(self, token):
    self._current_token = token

  def change_player(self, player):
    if player == "X":
      return "O"
    elif player == "O":
      return "X"

  def max_value(self,value,possible_best_value):
    if value > possible_best_value:
      return value
    else:
      return possible_best_value
  
  def min_value(self, value, possible_best_value):
    if value < possible_best_value:
      return value
    else:
      return possible_best_value


  def run_possibilities(self,player):
    token_winner = self._game.check_winner()
    if token_winner:
      return self.map_score[token_winner]
    
    #print(f"Jogador antes = {player}")
    #self._set_current_token(self.change_player(self._get_current_token()))
    player = self.change_player(player)
    #print(f"Jogador depois = {player}")
    #input()
    empty_spaces = self._game.get_empty_places()
    best_value = None
    for possibilities in empty_spaces:
      line_of_possibilities = possibilities[0]
      column_of_possibilities = possibilities[1]
      #self._game.make_move(line_of_possibilities, column_of_possibilities, self._get_current_token())
      self._game.make_move(line_of_possibilities, column_of_possibilities, player)
      #print("#################")
      #self._game.print_board()
      #print(f"melhor valor = {best_value}")
      #print("#################")
      value = self.run_possibilities(player)
      self._game.make_move(line_of_possibilities, column_of_possibilities, white)

      if best_value is None:
        best_value = value
      elif player == "X":
        best_value = self.max_value(value, best_value)
      elif player == "O":
        best_value = self.min_value(value, best_value)
    return best_value

    
    