import random


def create_return_match(match_schedule):
    for current_round in match_schedule:
        for current_match in current_round:
            team = current_match.pop(1)
            current_match.insert(0, team)
        random.shuffle(current_round)
    return match_schedule


# Create a list of teams
teams = list(range(4))

# Check if the number of teams is even
if len(teams) % 2 != 0:
    print("The number of teams must be even.")
    exit()

# Shuffle the teams
random.shuffle(teams)

num_of_rounds = len(teams) - 1
num_of_matches_per_round = len(teams) // 2

match_schedule = []

# Create rounds
for i in range(num_of_rounds):
    round_matches = []

    # Create matches per round
    for j in range(num_of_matches_per_round):
        if i % 2 == 0:
            match = [teams[j], teams[-(j+1)]]
        else:
            match = [teams[-(j+1)], teams[j]]

        # Add match to round
        round_matches.append(match)

    # Shuffle matches per round
    random.shuffle(round_matches)

    # Add round to match_schedule
    match_schedule.append(round_matches)

    # Rearrange teams to create new round
    team_to_move = teams.pop(num_of_rounds)
    teams.insert(2, team_to_move)

print("First Leg")
for round_matches in match_schedule:
    print(round_matches)

return_matches = create_return_match(match_schedule)
print("Second Leg")
for round_matches in return_matches:
    print(round_matches)
