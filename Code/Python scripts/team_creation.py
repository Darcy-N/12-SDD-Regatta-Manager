import random, os

# This function deals with the team creation. It allows the user to enter teams one by one, 

def create_team_list():  
    team_list = []
    while True:

        print("To add a team, type the name and press enter \nTo delete an entered team, type d, press enter, type the team that you wish to delete, then press enter \nTo enter a list of teams, type b, press enter, paste in the list of teams, then press enter \nTo finish entering teams or exit the program, type q and press enter")
        entered_action = input("Action: ")
        if entered_action.lower() in('q','quit'):
            confirm_action = input("Are you sure you want to quit? (y/n): ")
            if confirm_action.lower() in('y', 'yes'):
                break
        elif entered_action == 'd':
            team = input("Enter the name of the team to delete: ")
            if team in team_list:
                team_list.remove(team)
                print(f"Current team list: {team_list}")
            else:
                print("Team not found in the list")
        elif entered_action in team_list:
            print("Team already exists in the list, enter a unique team name")
        elif entered_action == "":
            print("Entry cannot be empty")
        elif entered_action == 'b':
            bulk_teams = input("Enter the team names separated by new lines: ")
            bulk_teams = bulk_teams.splitlines()
            for team in bulk_teams:
                if team in team_list:
                    print(f"Team '{team}' already exists in the list, enter a unique team name")
                else:
                    team_list.append(team)
            print(f"Current team list: {team_list}")
        else:
            team_list.append(entered_action)
            os.system('clear')
            print(f"Current team list: {team_list}")
    return team_list

completed_team_list = create_team_list()

def random_pairing(input_list):
    random.shuffle(input_list)
    paired_list = [(input_list[i], input_list[i+1]) for i in range(0, len(input_list)-1, 2)]
    if len(input_list) % 2 == 1:
        paired_list.append((input_list[-1], "BYE"))
    return paired_list

random_paired_list = random_pairing(completed_team_list)