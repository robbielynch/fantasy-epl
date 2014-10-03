__author__ = 'Robbie'

import fantasy_epl

class Player(object):

    name = ""
    club = ""
    position = ""
    rank = 0
    home_avg = 0
    away_avg = 0
    ppi = 0
    home_prediction = 0
    away_prediction = 0
    prediction = 0


    def __init__(self, rank, name, club, position, home_avg, away_avg, ppi):
        self.rank = rank
        self.name = name
        self.club = club
        self.position = position
        self.home_avg = home_avg
        self.away_avg = away_avg
        self.ppi = ppi
        self.calc_prediction()

    def calc_prediction(self):
        home_prediction = (self.home_avg * 1.15) + (self.away_avg)
        away_prediction = (self.home_avg * 0.85) + (self.away_avg)
        self.home_prediction = home_prediction
        self.away_prediction = away_prediction








def get_players_list():
    soup = fantasy_epl.get_soup_object()
    resultset = soup.find('table', {'class':"players-table"}).find("tbody").find_all("tr")

    player_rank = []
    player_names = []
    player_club = []
    player_pos = []
    player_home_avg = []
    player_away_avg = []
    player_ppi = []

    for row in resultset:
        cells = row.find_all("td")
        #p rank
        rank = cells[0].get_text().encode('ascii','ignore')
        player_rank.append(int(rank))
        #p name
        player_name = cells[3].get_text().encode('ascii','ignore')
        player_names.append(player_name)
        #p club
        club = cells[4].get_text().encode('ascii','ignore')
        club = normalise_player_clubs(club)
        player_club.append(club)
        #p position
        pos = cells[5].get_text().encode('ascii','ignore')
        player_pos.append(pos)
        #home avg
        home_avg = cells[10].get_text().encode('ascii','ignore')
        player_home_avg.append(int(home_avg))
        #away avg
        away_avg = cells[12].get_text().encode('ascii','ignore')
        player_away_avg.append(int(away_avg))
        #total ppi
        ppi = cells[13].get_text().encode('ascii','ignore').strip(' \t\n\r')
        player_ppi.append(int(ppi))


    ## Create player objects
    players = []

    for i, rank in enumerate(player_rank):
        p = Player(player_rank[i],player_names[i],player_club[i],player_pos[i],
                   player_home_avg[i],player_away_avg[i],player_ppi[i])
        players.append(p)

    return players


def normalise_player_clubs(club_name):
    if club_name == "ARS":
        return "Arsenal"
    elif club_name == "CHE":
        return "Chelsea"
    elif club_name == "SOU":
        return "Southampton"
    elif club_name == "LIV":
        return "Liverpool"
    elif club_name == "SWA":
        return "Swansea City"
    elif club_name == "MCI":
        return "Manchester City"
    elif club_name == "WHU":
        return "West Ham United"
    elif club_name == "WBA":
        return "West Bromwich Albion"
    elif club_name == "MUN":
        return "Manchester United"
    elif club_name == "CRY":
        return "Crystal Palace"
    elif club_name == "EVE":
        return "Everton"
    elif club_name == "AVL":
        return "Aston Villa"
    elif club_name == "STK":
        return "Stoke City"
    elif club_name == "TOT":
        return "Tottenham Hotspur"
    elif club_name == "HUL":
        return "Hull City"
    elif club_name == "NEW":
        return "Newcastle United"
    elif club_name == "QPR":
        return "Queens Park Rangers"
    elif club_name == "BUR":
        return "Burnley"
    elif club_name == "LEI":
        return "Leicester City"
    elif club_name == "SUN":
        return "Sunderland"
