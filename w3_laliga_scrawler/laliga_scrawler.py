"""
This file is to get registered player from each club
source:
  https://www.laliga.com/laliga-easports/clubes
"""

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

LALIGA_URL = "https://www.laliga.com/laliga-easports/clubes"
DOMAIN = "https://www.laliga.com"
POSITIONS = ['PORTERO', 'DEFENSA', 'CENTROCAMPISTA', 'DELANTERO']


def main():
    df = pd.DataFrame()
    team_dict = find_team_and_link_from_laliga(LALIGA_URL)
    

    # bilbao_url = "https://www.laliga.com/clubes/athletic-club/plantilla"
    # cadiz_url = "https://www.laliga.com/clubes/cadiz-cf/plantilla"

    # cadiz_players = find_player_containers_from_team(cadiz_url)
    # bilbao_players = find_player_containers_from_team(bilbao_url)
    # print(len(cadiz_players))

    # x = find_player_info_from_player_container(bilbao_players[0])

    print(x)


def find_team_and_link_from_laliga(laliga_url) -> dict:
    """
    From laliga website, find team name and squad URL for each team
    Return: A dict of team name: team URL
    """
    team_dict = {}

    response = requests.get(laliga_url, timeout=30)

    soup = BeautifulSoup(response.text)
    link_divs = soup.find_all(
        'div',
        class_ = re.compile("styled__ItemContainer.+")
    )

    for div in link_divs:
        team_div = div.find('div', class_ = "content-container")
        team = team_div.find('p').text
        team_link = div.find('a', class_ = "link")['href']
        if team:
            team_dict[team] = DOMAIN + team_link + '/plantilla'

    return team_dict


def find_player_containers_from_team(team_link: str) -> list:
    """
    From given team link, find player containers
    Return: A list of player containers
    """
    player_containers = []

    response = requests.get(team_link, timeout = 30)
    soup = BeautifulSoup(response.text)

    # Find all by SquadPositionContainer
    squad_pos_containers = soup.find_all(
        'div',
        class_ = re.compile("styled__SquadPositionContainer.+")
    )

    for squad_pos_container in squad_pos_containers:
        containers = squad_pos_container.find_all(
            'div',
            class_ = re.compile("styled__PlayerInfoContainer.+")
        )
        player_containers.extend(containers)

    return player_containers


def find_player_info_from_player_container(soup: BeautifulSoup) -> tuple:
    """
    Pass in a player_container soup, get a list of player names
    Return: a tuple of player name and position
    """
    text_containers = soup.find_all('p', class_ = re.compile("styled__TextRegularStyled.+"))

    player_name = text_containers[0].text
    player_position = text_containers[1].text

    print(f"{player_name=}")
    print(f"{player_position=}")

    if player_position.upper() not in POSITIONS:
        print(f"{player_name} is not a player.")
        return None
    else:
        return (player_name, player_position)


if __name__ == "__main__":
    main()
