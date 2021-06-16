white = " "
class Game:
  def __init__(self):
    self.board = [
      [white, white, white],
      [white, white, white],
      [white, white, white]
    ]
    self.token_winner = ""
  
  def print_board(self):
    for i in range(3):
      print("|".join(self.board[i]))
      if(i < 2):
        print('------')
  
  def check_play(self, i, j):
    if self.board[i][j] == white:
      return True
    else:
      return False
  
  def make_move(self,i,j, token):
    self.board[i][j] = token

  def get_token_winner(self):
    return self.token_winner

  def get_empty_places(self):
    empty_places = []
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == white:
          empty_places.append([i,j])
    return empty_places

  def check_winner(self):
    for i in range(3):
      lines = (self.board[i][0] == self.board[i][1]) and (self.board[i][1] == self.board[i][2]) and (self.board[i][0] != white)
      if lines:
        self.token_winner = self.board[i][0]
        return self.board[i][0]
    for i in range(3):
      columns = (self.board[0][i] == self.board[1][i]) and (self.board[1][i] == self.board[2][i]) and (self.board[0][i] != white)
      if columns:
        self.token_winner = self.board[0][i]
        return self.board[0][i]

    main_diagonal = (self.board[0][0] != white) and (self.board[0][0] == self.board[1][1]) and (self.board[1][1] == self.board[2][2])
    if main_diagonal:
      self.token_winner = self.board[0][0]
      return self.board[0][0]
    secondary_diagonal = (self.board[0][2] != white) and (self.board[0][2] == self.board[1][1]) and (self.board[1][1] == self.board[2][0])
    if secondary_diagonal:
      self.token_winner = self.board[0][2]
      return self.board[0][2]
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == white:
          return False
    self.token_winner = "DRAW"
    return "DRAW"