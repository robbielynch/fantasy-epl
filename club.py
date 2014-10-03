__author__ = 'Robbie'
import fantasy_epl
import urllib2


def get_clubs_objects():
    club_ranking_table_url = "http://www.premierleague.com/en-gb/players/ea-sports-ppi-club-ranking.html"
    club_table_html = urllib2.urlopen(club_ranking_table_url)
    soup = fantasy_epl.extract_soup(club_table_html.read())
    resultset = soup.find('table', {'class':"players-table"}).find_all("tr")

    clubs = []

    for row in resultset:

        cells = row.find_all("td")

        if(cells):
            #rank
            rank = cells[0].get_text().encode('ascii','ignore').strip(' \n\r\t')
            #club name
            name = cells[1].get_text().encode('ascii','ignore').strip()

            #Create club
            c = Club(int(rank), name)
            clubs.append(c)

    return clubs



def get_club_rank(clubs_list, club_name):
    for i, c in enumerate(clubs_list):
        if club_name == c.name:
            return c.rank
    return 1






class Club(object):

    name = ""
    rank = 0
    is_next_match_home = True
    next_opp_rank = 1
    next_opp_team_name = ""
    prediction = 0
    players = []


    def __init__(self, rank, name, is_next_match_home=True, next_opp_rank=1,next_opp_team_name=""):
        self.rank = rank
        self.name = name
        self.is_next_match_home = is_next_match_home
        self.next_opp_rank = next_opp_rank
        self.next_opp_team_name = next_opp_team_name


    def calc_prediction(self):
        if(self.is_next_match_home):
            self.prediction = self.next_opp_rank
        else:
            self.prediction = (self.next_opp_rank / 2)

        return self.prediction
