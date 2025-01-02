position_display = [
  '-', '-', '-', 
  '-', '-', '-', 
  '-', '-', '-', 
]


def player_wins() -> bool:
  if position_display[0] == position_display[1] == position_display[2] == 'x':
      return True
  elif position_display[3] == position_display[4] == position_display[5] == 'x':
    return True
  elif position_display[6] == position_display[7] == position_display[8] == 'x':
    return True
  elif position_display[0] == position_display[4] == position_display[8] == 'x':
    return True
  elif position_display[2] == position_display[4] == position_display[6] == 'x':
    return True
  elif position_display[0] == position_display[3] == position_display[6] == 'x':
    return True
  elif position_display[1] == position_display[4] == position_display[7] == 'x':
    return True
  elif position_display[2] == position_display[5] == position_display[8] == 'x':
    return True


def computer_wins() -> bool:
  if position_display[0] == position_display[1] == position_display[2] == 'o':
      return True
  elif position_display[3] == position_display[4] == position_display[5] == 'o':
    return True
  elif position_display[6] == position_display[7] == position_display[8] == 'o':
    return True
  elif position_display[0] == position_display[4] == position_display[8] == 'o':
    return True
  elif position_display[2] == position_display[4] == position_display[6] == 'o':
    return True
  elif position_display[0] == position_display[3] == position_display[6] == 'o':
    return True
  elif position_display[1] == position_display[4] == position_display[7] == 'o':
    return True
  elif position_display[2] == position_display[5] == position_display[8] == 'o':
    return True