import csv
import pandas as pd

MAINDIR = "./"

atp2022 = pd.read_csv('atp_matches_2022.csv', encoding = 'UTF-8')
challenger2022 = pd.read_csv('atp_matches_qual_chall_2022.csv', encoding = 'UTF-8')
Futures2022 = pd.read_csv('atp_matches_futures_2022.csv', encoding = 'UTF-8')


atp2022 = pd.DataFrame(atp2022)
challenger2022 = pd.DataFrame(challenger2022)
futures2022 = pd.DataFrame(Futures2022)

allMatches = pd.concat([atp2022, challenger2022, futures2022])

player = input().title()

result = allMatches.loc[allMatches["winner_name"] == player, ["loser_name", "loser_rank"]]
result = result.reset_index(drop = True)
result.columns = result.columns.str.replace('_', ' ')
result.columns = result.columns.str.title()


pd.DataFrame(result)
