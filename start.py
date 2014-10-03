import fixtures
from club import Club, get_clubs_objects, get_club_rank
import player

# create players
def create_players():
    """
    Create the list of player objects
    :return: List of player objects
    """
    player_list = player.get_players_list()
    return player_list


def calc_player_scores(player_list, clubs_list):
    """
    Goes through all player and clubs and adjusts their prediction
    based on whether their next game is at home and their next
    opponent's rank
    :param player_list: The list of player objects
    :param clubs_list: The list of club objects
    :return: The player_list with updated players
    """

    for p in player_list:
        for cl in clubs_list:
            if p.club == cl.name:
                if cl.is_next_match_home:
                    p.home_prediction += cl.next_opp_rank * 1.25
                    p.prediction = p.home_prediction
                else:
                    p.away_prediction += cl.next_opp_rank
                    p.prediction = p.away_prediction

    return player_list


def start(week_num):
    # Week Number
    week_number = week_num

    # Fixtures #
    home_teams, away_teams = fixtures.get_fixtures(week_number)

    # Create clubs #
    clubs_list = get_clubs_objects()

    # Set club fixture_is_home #
    for c in clubs_list:
        if(c.name in home_teams):
            # Set home fixture #
            c.is_next_match_home = True
        else:
            # Set away fixture #
            c.is_next_match_home = False

    # Set next opp and rank #
    for club in clubs_list:
        if club.is_next_match_home:
            # Club is home team #
            index_of_club_in_home_team_list = home_teams.index(club.name)
            next_opp = away_teams[index_of_club_in_home_team_list]
            club.next_opp_team_name = next_opp
            # Set next opp rank #
            club.next_opp_rank = get_club_rank(clubs_list, next_opp)
        else:
            # Club is away team #
            index_of_club_in_away_team_list = away_teams.index(club.name)
            next_opp = home_teams[index_of_club_in_away_team_list]
            club.next_opp_team_name = next_opp
            # Set next opp rank #
            club.next_opp_rank = get_club_rank(clubs_list, next_opp)

    # Create players #
    player_list = create_players()

    # Calculate player scores #
    player_list = calc_player_scores(player_list, clubs_list)

    # Output highest predictions #
    import operator
    player_list.sort(key=operator.attrgetter("prediction"), reverse=True)

    # Output Markdown Table #
    print("| Player Name | Club | Position | Prediction |")
    print("|---|---|----|----|")

    for p in player_list:
        try:
            print("| " + p.name + " | " + p.club + " | " + p.position + " |" + str(p.prediction) + " |")
        except Exception, e:
            pass
