__author__ = 'Robbie'

__author__ = 'Robbie Lynch'

from bs4 import BeautifulSoup
from data import sample_html
from player import Player
from club import Club
import urllib2


def get_soup_object():

    # ppi_url = "http://www.premierleague.com/en-gb/players/ea-sports-player-performance-index.html?paramSearchTerm=&paramClubId=&paramSeason=2014-2015&paramPosition=&paramEaBreakdownType=ACCUMULATIVE&paramGameWeek=1&paramItemsPerPage=500&paramSelectedPageIndex=1"
    #
    # usock = urllib2.urlopen(ppi_url)
    # html = usock.read()
    # usock.close()

    soup = BeautifulSoup(sample_html)

    return soup


def print_home_and_away_predictions(players):
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


def sort_list_of_objects_by_attribute(my_list, attribute, reverse=True):
    import operator
    my_list.sort(key=operator.attrgetter(attribute), reverse=reverse)



def extract_soup(html):
    return BeautifulSoup(html)


def get_next_opp_rank(opp_name, clubs):
    opp_club_rank = 1
    for c in clubs:
        if(c.name == opp_name):
            opp_club_rank = c.rank

    return opp_club_rank




#ppi_table = get_ppi_table()


