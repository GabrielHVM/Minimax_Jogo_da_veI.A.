from game import Game
from player import Player
import os

def main():
  game = Game()
  player_one = Player(game, "X")
  player_one.set_my_turn(True)
  player_two = Player(game, "O")
  try:
    while not game.check_winner():
      os.system('cls' if os.name == 'nt' else 'clear')
      game.print_board()
      if player_one.get_my_turn():
        print("Turno do jogador 1 : ")
        i,j = player_one.get_player_input()
        if game.check_play(i,j):    
          player_one.make_play(i,j)
          player_one.set_my_turn(False)
          player_two.set_my_turn(True)
        else:
          print("Posição já ocupada!")
          input("Aperte ENTER para continuar!")
      elif player_two.get_my_turn():
        print("Turno do jogador 2 : ")
        i,j = player_two.get_player_input()
        if game.check_play(i,j):
          player_two.make_play(i,j)
          player_two.set_my_turn(False)
          player_one.set_my_turn(True)
        else:
          print("Posição já ocupada!")
          input("Aperte ENTER para continuar!")
    if player_one.get_token() == game.get_token_winner():
      print("Jogador numero 1 ganhou!")
    elif player_two.get_token() == game.get_token_winner():
      print("Jogador numero 2 ganhou!")
    elif game.get_token_winner() == "DRAW":
      print("Empate!")
  except KeyboardInterrupt:
    print("Até mais! :)")
if __name__ == "__main__":
  main()