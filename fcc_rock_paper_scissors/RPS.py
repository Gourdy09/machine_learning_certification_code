# method that uses the most frequent patterns to counter

steps = {}

def player(prev_play, opponent_history=[]):
    # add previous move to history
    if prev_play != "":
        opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 6:
        pattern = join(opponent_history[-6:]) # store last six moves as pattern

        # Check if the pattern of the last 7 moves (6 moves + the last one) already exists in 'steps'
        # If so, increment its count, otherwise add it with a count of 1
        if join(opponent_history[-(6 + 1):]) in steps.keys():
            steps[join(opponent_history[-(6 + 1):])] += 1
        else:
            steps[join(opponent_history[-(6 + 1):])] = 1

        # Define possible future patterns
        possible = [pattern + "R", pattern + "P", pattern + "S"]

        # add new patterns with count 0 to 'steps'
        for i in possible:
            if not i in steps.keys():
                steps[i] = 0

        # get most frequent pattern
        predict = max(possible, key=lambda key: steps[key])

        # get last character and do counter
        if predict[-1] == "P":
            guess = "S"  # If opponent is likely to play Paper: play Scissors
        if predict[-1] == "R":
            guess = "P"  # If opponent is likely to play Rock: play Paper
        if predict[-1] == "S":
            guess = "R"  # If opponent is likely to play Scissors: play Rock

    return guess


def join(moves):
    return "".join(moves)
