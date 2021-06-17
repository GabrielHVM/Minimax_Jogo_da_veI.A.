white = " "
import os
import sys
from player import Player
from minimax import Minimax
from random import randrange
from time import sleep

class Game:
  def __init__(self):
    self.board = [
      [white, white, white],
      [white, white, white],
      [white, white, white]
    ]
    self.token_winner = ""
  
  def print_board(self):
    print("\n")
    for i in range(3):
      print("|".join(self.board[i]))
      if(i < 2):
        print('------')
  
  def check_play(self, i, j):
    if self.board[i][j] == white:
      return True
    else:
      return False
  
  def clean_board(self):
    for i in range(3):
      for j in range(3):
        self.board[i][j] = white

  def player_vs_player(self):
    #X ever start the game
    player_one = Player(self, "X")
    player_one.set_my_turn(True)
    player_two = Player(self, "O")
    try:
      while not self.check_winner():
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_board()
        if player_one.get_my_turn():
          print(f"Turno do {player_one.get_token()} : ")
          i,j = player_one.get_player_input()
          if self.check_play(i,j):    
            player_one.make_play(i,j)
            player_one.set_my_turn(False)
            player_two.set_my_turn(True)
          else:
            print("Posição já ocupada!")
            input("Aperte ENTER para continuar!")
        elif player_two.get_my_turn():
          print(f"Turno do {player_two.get_token()} : ")
          i,j = player_two.get_player_input()
          if self.check_play(i,j):
            player_two.make_play(i,j)
            player_two.set_my_turn(False)
            player_one.set_my_turn(True)
          else:
            print("Posição já ocupada!")
            input("Aperte ENTER para continuar!")
      if self.get_token_winner() == "DRAW":
        self.game_over("DRAW")
      elif self.get_token_winner() == "X" or self.get_token_winner() == "O":
        self.game_over(self.get_token_winner())
    except Exception as error:
      print("OPS, o jogo crashou! :(")
      print(f"error = {error}")
      sys.exit() 

  def ia_vs_player(self):
    rand = randrange(2)
    ia_player = object
    human_player = object
    if rand == 0:
      ia_player = Minimax(self, "X")
      human_player = Player(self, "O")
      ia_player.set_my_turn(True)
    else:
      ia_player = Minimax(self, "O")
      human_player = Player(self, "X")
      human_player.set_my_turn(True)
    try:
      while not self.check_winner():
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_board()
        if ia_player.get_my_turn():
          print(f"Turno da Inteligencia Artificial!")
          i,j = ia_player.best_moviment()  
          ia_player.make_play(i,j)
          ia_player.set_my_turn(False)
          human_player.set_my_turn(True)
          sleep(0.5)
        elif human_player.get_my_turn():
          print(f"Turno do {human_player.get_token()} : ")
          i,j = human_player.get_player_input()
          if self.check_play(i,j):
            human_player.make_play(i,j)
            human_player.set_my_turn(False)
            ia_player.set_my_turn(True)
          else:
            print("Posição já ocupada!")
            input("Aperte ENTER para continuar!")
      if self.get_token_winner() == "DRAW":
        self.game_over("DRAW")
      elif self.get_token_winner() == "X" or self.get_token_winner() == "O":
        self.game_over(self.get_token_winner())
    except Exception as error:
      print("OPS, o jogo crashou! :(")
      print(f"error = {error}")
      sys.exit() 

  def ia_vs_ia(self):
    #X ever start the game
    ia_player_one = Minimax(self, "X")
    ia_player_one.set_my_turn(True)
    ia_player_two = Minimax(self, "O")
    try:
      while not self.check_winner():
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_board()
        if ia_player_one.get_my_turn():
          i, j = ia_player_one.best_moviment()   
          ia_player_one.make_play(i,j)
          ia_player_one.set_my_turn(False)
          ia_player_two.set_my_turn(True)
          sleep(1)
        elif ia_player_two.get_my_turn():
          i, j = ia_player_two.best_moviment()
          ia_player_two.make_play(i,j)
          ia_player_two.set_my_turn(False)
          ia_player_one.set_my_turn(True)
          sleep(1)
      if self.get_token_winner() == "DRAW":
        self.game_over("DRAW")
      elif self.get_token_winner() == "X" or self.get_token_winner() == "O":
        self.game_over(self.get_token_winner())
    except Exception as error:
      print("OPS, o jogo crashou! :(")
      print(f"error = {error}")
      sys.exit() 

  def game_over(self, winner):
    os.system('cls' if os.name == 'nt' else 'clear')
    self.print_board()
    if winner == "DRAW":
      print("O jogo deu empate Empate!")
    else:
      print(f"{winner} ganhou!")
    play_again = input("Você deseja jogar novamente? (S/N) => ")
    if play_again:
      self.clean_board()
      self.start_new_game()
    else:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("\
                                                                                       \n\
#######################################################################################\n\
#######################################################################################\n\
#####   ###  ##   ###  ##     ###       #      #       # #### ####       #        #####\n\
#####    #  #  # #    #  #    #  #     # #      #     #  #     ##       # #       #####\n\
#####    #  #  # # #  #  #    #   #   #####      #   #   ###   ##      #####      #####\n\
#####  # #  #  # #  # #  #    #  #   #     #      # #    #     ##     #     #     #####\n\
#####  ###   ##  ####  ##     ###   #       #      #     #### #### # #       # #  #####\n\
#######################################################################################\n\
#######################################################################################\n\
                                                            by: GHVM                   \n\
     Obrigado por jogar conosco! Até mais! :)                                          ")
      sys.exit()
  def start_new_game(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\
                                                                                       \n\
#######################################################################################\n\
#######################################################################################\n\
#####   ###  ##   ###  ##     ###       #      #       # #### ####       #        #####\n\
#####    #  #  # #    #  #    #  #     # #      #     #  #     ##       # #       #####\n\
#####    #  #  # # #  #  #    #   #   #####      #   #   ###   ##      #####      #####\n\
#####  # #  #  # #  # #  #    #  #   #     #      # #    #     ##     #     #     #####\n\
#####  ###   ##  ####  ##     ###   #       #      #     #### #### # #       # #  #####\n\
#######################################################################################\n\
#######################################################################################\n\
                                                             by: GHVM                  \n\
     Faça a escolha do modo de jogo:                                                   \n\
       1 - Jogar com o amigo.                                                          \n\
       2 - Jogar com a maquina.                                                        \n\
       3 - Que as máquinas briguem!                                                    \n\
       4 - Sair do jogo! :(                                                             ")
    game_mode = int(input("\
                                                                                       \n\
     -> "))
    if game_mode == 1:
      self.player_vs_player()
    elif game_mode == 2:
      self.ia_vs_player()
    elif game_mode == 3:
      self.ia_vs_ia()
    elif game_mode == 4:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("\
                                                                                       \n\
#######################################################################################\n\
#######################################################################################\n\
#####   ###  ##   ###  ##     ###       #      #       # #### ####       #        #####\n\
#####    #  #  # #    #  #    #  #     # #      #     #  #     ##       # #       #####\n\
#####    #  #  # # #  #  #    #   #   #####      #   #   ###   ##      #####      #####\n\
#####  # #  #  # #  # #  #    #  #   #     #      # #    #     ##     #     #     #####\n\
#####  ###   ##  ####  ##     ###   #       #      #     #### #### # #       # #  #####\n\
#######################################################################################\n\
#######################################################################################\n\
                                                            by: GHVM                   \n\
     Obrigado por jogar conosco! Até mais! :)                                          ")
      sys.exit()
    else:
      print("Escolha inválida!")
      sleep(1.5)
      self.start_new_game

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