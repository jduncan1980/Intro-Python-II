def move_parser(next_move):
  
    if next_move == 'help':
        print('Move to another room: n, s, e, or w\nquit game: q\n')  
    elif next_move == 'n' and hasattr(player.location, 'n_to'):
        player.location = player.location.n_to
    elif next_move == 'n' and not hasattr(player.location, 'n_to'):
        next_move = input("Can't go that way, try again...")
    elif next_move == 's' and hasattr(player.location, 's_to'):
        player.location = player.location.s_to
    elif next_move == 's' and not hasattr(player.location, 's_to'):
        next_move = input("Can't go that way, try again...")   
    elif next_move == 'e' and hasattr(player.location, 'e_to'):
        player.location = player.location.e_to
    elif next_move == 'e' and not hasattr(player.location, 'e_to'):
        next_move = input("Can't go that way, try again...")   
    elif next_move == 'w' and hasattr(player.location, 'w_to'):
        player.location = player.location.w_to
    elif next_move == 'w' and not hasattr(player.location, 'w_to'):
        next_move = input("Can't go that way, try again...")
    elif next_move == 'q':
        quit()