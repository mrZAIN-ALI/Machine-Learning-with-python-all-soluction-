user_moves = []
starting_move = last_move = 'S'
detected_bots = [False, False, False, False]
counter_moves = {'P': 'R', 'R': 'S', 'S': 'P'}
quincy_index = -1
move_sequence = [{
    "RR": 0, 
    "RP": 0, 
    "RS": 0, 
    "PR": 0, 
    "PP": 0, 
    "PS": 0, 
    "SR": 0, 
    "SP": 0, 
    "SS": 0, 
}]

def player(opponent_last_move, opponent_moves = []):
    global user_moves, last_move, detected_bots, counter_moves, quincy_index, move_sequence
    
    opponent_moves.append(opponent_last_move)
    user_moves.append(last_move)
    
    # Detecting first bot (Quincy)
    if(len(set(detected_bots)) == 1 and opponent_moves[-5:] == ['R', 'P', 'P', 'S', 'R']):
        detected_bots[0] = True

    if detected_bots[0]:
        if len(opponent_moves) % 1000 == 0:
            detected_bots = [False, False, False, False]
            opponent_moves.clear()

        quincy_moves = ['P', 'S', 'S', 'R', 'P']
        quincy_index = (quincy_index + 1) % 5
        return quincy_moves[quincy_index]

    # Detecting second bot
    if len(set(detected_bots)) == 1 and opponent_moves[-5:] == ['P', 'P', 'R', 'R', 'R']:
        detected_bots[1] = True

    if detected_bots[1]:
        last_two_moves = ''.join(user_moves[-2:])
        if len(last_two_moves) == 2:
            move_sequence[0][last_two_moves] += 1

        next_possible_moves = [
            last_move + 'R', 
            last_move + 'P', 
            last_move + 'S',
        ]
        
        prediction_counts = {k: move_sequence[0][k] for k in next_possible_moves if k in move_sequence[0]}
        predicted_move = max(prediction_counts, key=prediction_counts.get)[-1:]
        
        if len(opponent_moves) % 1000 == 0:
            detected_bots = [False, False, False, False]
            opponent_moves.clear()
            move_sequence = [{
                "RR": 0, 
                "RP": 0, 
                "RS": 0, 
                "PR": 0, 
                "PP": 0, 
                "PS": 0, 
                "SR": 0, 
                "SP": 0, 
                "SS": 0, 
            }]
        
        last_move = counter_moves[predicted_move]
        return last_move

    # Detecting third bot
    if len(set(detected_bots)) == 1 and opponent_moves[-5:] == ['P', 'R', 'R', 'R', 'R']:
        detected_bots[2] = True

    if detected_bots[2]:
        if len(opponent_moves) % 1000 == 0:
            detected_bots = [False, False, False, False]
            opponent_moves.clear()

        last_move = counter_moves[last_move]
        return last_move

    # Detecting fourth bot
    if len(set(detected_bots)) == 1 and opponent_moves[-5:] == ['R', 'R', 'R', 'R', 'R']:
        detected_bots[3] = True

    if detected_bots[3]:
        if len(opponent_moves) == 1000:
            detected_bots = [False, False, False, False]
            opponent_moves.clear()

        recent_moves = user_moves[-10:]
        most_common_move = max(set(recent_moves), key=recent_moves.count)
        last_move = counter_moves[most_common_move]
        return last_move

    last_move = starting_move
    return last_move
