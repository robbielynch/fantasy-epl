__author__ = 'Robbie'

__author__ = 'Robbie Lynch'

from bs4 import BeautifulSoup
import urllib2


def get_soup_object():
    """
    Create and return the soup containing all player data
    :return: soup object
    """

    ppi_url = "http://www.premierleague.com/en-gb/players/ea-sports-player-performance-index.html?paramSearchTerm=&paramClubId=&paramSeason=2014-2015&paramPosition=&paramEaBreakdownType=ACCUMULATIVE&paramGameWeek=1&paramItemsPerPage=500&paramSelectedPageIndex=1"

    usock = urllib2.urlopen(ppi_url)
    html = usock.read()
    usock.close()

    soup = BeautifulSoup(html)

    return soup



def sort_list_of_objects_by_attribute(my_list, attribute, reverse=True):
    """
    Generic function to sort a list of object by attribute
    :param my_list: List to sort
    :param attribute: Name of the attribute to sort
    :param reverse: boolean, sort in reverse order
    :return: the sorted list
    """
    import operator
    my_list.sort(key=operator.attrgetter(attribute), reverse=reverse)



def extract_soup(html):
    return BeautifulSoup(html)


def get_next_opp_rank(opp_name, club_list):
    """
    Gets the club opposition teams ranking
    :param opp_name: string, opposition club name
    :param club_list: list of club objects
    :return: int, the oppositions club rank
    """
    opp_club_rank = 1
    for c in club_list:
        if c.name == opp_name:
            opp_club_rank = c.rank

    return opp_club_rank



