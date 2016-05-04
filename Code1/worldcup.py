from datetime import datetime
import os
import sys


def read_game_info(filename):
    '''
    INPUT: string
    OUTPUT: tuple of string, string, string, int, int

    Given the filename of a game, return the time, team names and score for the
    game. Return these values:

        time: string representing time of game
        team1: first team name
        team2: second team name
        score1: score of first team
        score2: score of second team
    '''
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line.strip())

    time = data[0]
    team1 = data[3].split('-')[0].strip()
    team2 = data[3].split('-')[1].strip()
    score1 = int(data[4].split('-')[0])
    score2 = int(data[4].split('-')[1])

    return (time, team1, team2, score1, score2)


def display_game(time, team, other, team_score, other_score):
    '''
    INPUT: string, string, string, int, int
    OUTPUT: string

    Given the time, names of the teams and score, return a one line string
    presentation of the results.
    '''

    disp_game_string = "{time}: {team1} ({score1}) - {team2} ({score2})" \
                        .format(time=time, team1=team, score1=team_score,
                                        team2=other, score2=other_score)
    return disp_game_string

def display_summary(team, data, detailed=False):
    '''
    INPUT: string, list of tuples, bool
    OUTPUT: string

    Given the data (list of tuples of game data), return a string containing
    the summary of results for the given team. This includes # games played,
    # wins, # losses, # ties, and # goals scored.

    If detailed is True, also include in the string all the games for the given
    team.
    '''

    wins=losses=ties=total_goals=total_games = 0
    for row in data:
        if row[1]==team and row[3]>row[4]:
            wins+=1
            total_goals+=row[3]
            total_games+=1
        elif row[2]==team and row[4]>row[3]:
            wins+=1
            total_goals+=row[4]
            total_games+=1
        elif row[1]==team and row[3]<row[4]:
            losses+=1
            total_goals+=row[3]
            total_games+=1
        elif row[2]==team and row[4]<row[3]:
            losses+=1
            total_goals+=row[4]
            total_games+=1
        elif (row[1] == team or row[2]==team) and row[3]==row[4]:
            ties+=1
            total_goals+=row[3]
            total_games+=1
        else:
            pass

    if detailed:
        addition = "\n"+"\n".join(data)
    else:
        addition = ""



    summary_string = "{team} played a total of {tot_games} games.\n"\
                     "{wins} win(s), {losses} loss(es), {ties} tie(s),"\
                     " {tot_goals} total goal(s){detail}" \
                      .format(team=team, tot_games=total_games, wins=wins,
                              losses=losses, ties=ties, tot_goals=total_goals,
                              detail=addition)

    return summary_string

def run(directory, team):
    '''
    INPUT: string, string
    OUTPUT: None

    Given the directory where the data is stored and the team name of interest,
    read the data from the directory and display the summary of results for the
    given team.
    '''
    data = []
    for filename in os.listdir(directory):
        data.append(read_game_info(os.path.join(directory, filename)))
    print display_summary(team, data, detailed=True)


def main():
    '''
    INPUT: None
    OUTPUT: None

    Get the directory name and team name from the arguments given. If arguments
    are valid, display the summary of results. Otherwise, exit the program.
    '''
    error_message = "Usage: python worldcup.py directory team\n" \
                    "       e.g. python worldcup.py worldcup USA"
    if len(sys.argv) != 3:
        print error_message
        exit()
    directory = sys.argv[1]
    if not os.path.exists(directory):
        print "{0} is not a valid directory.".format(directory)
        print error_message
        exit()
    team = sys.argv[2]
    run(directory, team)


if __name__ == '__main__':
    main()
