__author__ = 'Robbie'

from bs4 import BeautifulSoup
from data import sample_html
from player import Player
from club import Club
import urllib2


def normalise_team_name(team_name):
    if team_name == "Man Utd":
        return "Manchester United"
    elif team_name == "Man City":
        return "Manchester City"
    elif team_name == "Swansea":
        return "Swansea City"
    elif team_name == "West Ham":
        return "West Ham United"
    elif team_name == "Leicester":
        return "Leicester City"
    elif team_name == "Spurs":
        return "Tottenham Hotspur"
    elif team_name == "Hull":
        return "Hull City"
    elif team_name == "West Brom":
        return "West Bromwich Albion"
    elif team_name == "Stoke":
        return "Stoke City"
    elif team_name == "Newcastle":
        return "Newcastle United"
    elif team_name == "QPR":
        return "Queens Park Rangers"
    else:
        return team_name


def get_fixtures(week_num):
    # get html
    fix_url = "http://fantasy.premierleague.com/fixtures/" + str(week_num)
    usock = urllib2.urlopen(fix_url)
    html = usock.read()
    usock.close()

    # get soup
    soup = BeautifulSoup(html)

    # get fixture table
    resultset = soup.find('table', {'class':"ismFixtureTable"}).find("tbody").find_all("tr")

    home = []
    away = []

    for row in resultset:
        cells = row.find_all("td")

        h = cells[1].get_text().encode('ascii','ignore').strip()
        a = cells[5].get_text().encode('ascii','ignore').strip()

        # Normalise the team name to match up with other sources
        h = normalise_team_name(h)
        a = normalise_team_name(a)

        home.append(h)
        away.append(a)

    return home, away






