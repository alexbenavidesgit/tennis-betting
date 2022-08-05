import pandas as pd
from datetime import datetime
from pprint import pprint

def input_player():
    player = input().title()
    return player


def wins_table():
# Read and Prepare Tables
    atp2022 = pd.read_csv('Data/atp_matches_2022.csv', encoding = 'UTF-8')
    challenger2022 = pd.read_csv('Data/atp_matches_qual_chall_2022.csv', encoding = 'UTF-8')
    Futures2022 = pd.read_csv('Data/atp_matches_futures_2022.csv', encoding = 'UTF-8')
    atp2022 = pd.DataFrame(atp2022)
    challenger2022 = pd.DataFrame(challenger2022)
    futures2022 = pd.DataFrame(Futures2022)

    allMatches = pd.concat([atp2022, challenger2022, futures2022])

    # Collecting Wins from Inputed Player
    wins_data = allMatches.loc[allMatches["winner_name"] == input_player(), ["loser_name", "loser_rank", 'score', 'tourney_date','loser_ioc']]
    # Formatting Table
    wins_data = wins_data.reset_index(drop = True)
    wins_data = pd.DataFrame(wins_data)
    wins_data[['tourney_date']] = wins_data[['tourney_date']].applymap(str).applymap(lambda s: "{}/{}/{}".format(s[4:6],s[6:], s[0:4]))
    wins_data.columns = ['Opp_Name', 'Opp_Ranking', 'Score', 'Date', 'Nationality']

    return wins_data
