__author__ = 'Robbie'

from unittest import TestCase
from fantasy_epl import get_soup_object, extract_soup
from player import Player
from club import Club
import urllib2
import fixtures
import start


class TestFEPL(TestCase):


    def setUp(self):
        self.soup = get_soup_object()


    def test_get_table(self):
        soup = get_soup_object()
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



        print "======================================="
        print "HOME PREDICTIONS"
        print "======================================="
        import operator
        players.sort(key=operator.attrgetter("home_prediction"), reverse=True)

        # output home pred
        for p in players:
            print p.name + "\t\t" + str(p.home_prediction)


        print "\n\n\n\n"
        print "======================================="
        print "AWAY PREDICTIONS"
        print "======================================="
        players.sort(key=operator.attrgetter("away_prediction"), reverse=True)

        # output away pred
        for p in players:
            print p.name + "\t\t" + str(p.away_prediction)


        print "hi"



    def test_get_club_rankings(self):
        club_ranking_table_url = "http://www.premierleague.com/en-gb/players/ea-sports-ppi-club-ranking.html"
        club_table_html = urllib2.urlopen(club_ranking_table_url)
        soup = extract_soup(club_table_html.read())
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

        print "hi"



    def test_get_fixtures(self):
        home, awaay = fixtures.get_fixtures(7)
        print("hi")

    def test_start(self):
        plist = start.start(7)

        print("| Player Name | Club | Position | Prediction |")
        print("|---|---|----|----|")

        for p in plist:
            print("| " + p.name + " | " + p.club + " | " + p.position + " |" + str(p.prediction) + " |")



    def tearDown(self):
        pass

