import random

def team_entering():
    team_list = []
    while true:
        temp_team = input("Please enter team name: ")
        team_list.append(temp_team)
        print(f"Current team list: {team_list}")

def low_point_system(finish_order):
    return sum([i for i in range(1, len(finish_order) + 1) if finish_order[i - 1]])

def next_round_pairings(teams):
    pairings = []
    random.shuffle(teams)
    for i in range(0, len(teams), 2):
        pairings.append((teams[i], teams[i + 1]))
    return pairings

def run_race(teamA, teamB):
    teamA_finish = list(map(int, input(f"Enter team {teamA}'s positions: ").split()))
    teamB_finish = list(map(int, input(f"Enter team {teamB}'s positions: ").split()))
    teamA_points = low_point_system(teamA_finish)
    teamB_points = low_point_system(teamB_finish)
    if teamA_points < teamB_points:
        return teamA
    elif teamA_points > teamB_points:
        return teamB
    else:
        for i in range(len(teamA_finish)):
            if teamA_finish[i] < teamB_finish[i]:
                return teamA
            elif teamB_finish[i] < teamA_finish[i]:
                return teamB

def update_team_scores(team_scores, winner, teamA, teamB):
    if winner == teamA:
        team_scores[teamA] += 1
    elif winner == teamB:
        team_scores[teamB] += 1

def main():
    teams = [f"Team {i}" for i in range(1, 10)]
    team_scores = {team: 0 for team in teams}
    while True:
        pairings = next_round_pairings(teams)
        for teamA, teamB in pairings:
            winner = run_race(teamA, teamB)
            update_team_scores(team_scores, winner, teamA, teamB)
        teams.sort(key=lambda x: team_scores[x], reverse=True)
        if input("Would you like to end the Swiss League? (y/n) ").lower() == "y":
            break
    print("Final Standings:")
    for i in range(8):
        print(f"{i + 1}. {teams[i]} ({team_scores[teams[i]]} wins)")

# Inits main function
# if __name__ == "__main__":
#     main()
