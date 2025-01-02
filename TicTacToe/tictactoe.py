from random import randint
import time
from rich.traceback import install
from rich.console import Console
from win_model import position_display, player_wins, computer_wins

install()
console = Console()



# ...........................................Board Display......................................................
def game_board() -> None:
  console.print(position_display[0], position_display[1], position_display[2], sep=' | ', style='bold green')
  console.print('----------', style='bold yellow')
  console.print(position_display[3], position_display[4], position_display[5], sep=' | ', style='bold red')
  console.print('----------', style='bold yellow')
  console.print(position_display[6], position_display[7], position_display[8], sep=' | ', style='bold blue')


def player_turn(player) -> None:
  '''Triggers the player to play.'''
  player_symbol = 'x'
  console.print(f'{player} thinking...\n')
  
  player_pos = input('Enter a position (1 - 9): ')
  
  if player_pos.isdigit() and 0 < int(player_pos) < 10:
    for num in range(9):
      if int(player_pos) == num + 1:
        position_display[num] = player_symbol
        time.sleep(0.5)
        console.print()
        game_board()
  else:
      console.print()
      console.print('Invalid choice. Enter a number (1-9).', style='bold red')
      time.sleep(1)
      console.print()
      player_turn(player)
    
          
def computer_turn() -> None:
  '''Triggers the computer to play.'''
  computer_symbol = 'o'
  computer_pos = randint(0, 8)
  
  if position_display[computer_pos] == '-':
    position_display[computer_pos] = computer_symbol
    time.sleep(1)
    console.print()
    print('Computer thinking...')
    console.print()
    time.sleep(0.5)
    game_board()  
  else:
      computer_turn()
 
  
def play_again():
    print()
    answer = input('Do you want to play again? (y/n): ').lower()
    if answer == 'y':
      for num in range(9):
        position_display[num] = '-'
      print()
      main()
    elif not answer.isalpha():
      console.print('\nInvalid input! Enter y or n.', style='bold red')
      play_again()
        
 
def main():
  # .........................................Game Welcome Text.........................................
  console.print()
  console.print('----------------------------- TIC TAC TOE ----------------------------', style='bold red')
  console.print()

  game_board()
  console.print()
  player_name = input('Enter your name: ').title()
  
  game_on = True
  while game_on:
    console.print()
    if '-' in position_display:
      player_turn(player=player_name)
      if player_wins():
        time.sleep(0.5)
        console.print()
        console.print(f'{player_name} wins🎉 Congratulations🎉', '\nGame over...')
        break
      
    if '-' in position_display:
      computer_turn()
      if computer_wins():
        time.sleep(0.5)
        console.print()
        console.print(f'Computer wins🎉', '\nGame over...')
        break
      
    else:
      time.sleep(0.5)
      console.print()
      console.print(f"It's a Draw. \nGame over...")
      game_on = False
   
  play_again()
      
if __name__ == '__main__':
  main()
  
                                  
  