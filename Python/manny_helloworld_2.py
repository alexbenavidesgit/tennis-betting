import csv
import pandas as pd

MAINDIR = "./"

atp2022 = pd.read_csv('Data/atp_matches_2022.csv', encoding = 'UTF-8')
challenger2022 = pd.read_csv('Data/atp_matches_qual_chall_2022.csv', encoding = 'UTF-8')
Futures2022 = pd.read_csv('Data/atp_matches_futures_2022.csv', encoding = 'UTF-8')


atp2022 = pd.DataFrame(atp2022)
challenger2022 = pd.DataFrame(challenger2022)
futures2022 = pd.DataFrame(Futures2022)

allMatches = pd.concat([atp2022, challenger2022, futures2022])

player = input().title()

# Collecting Wins
resultW = allMatches.loc[allMatches["winner_name"] == player, ["loser_name", "loser_rank"]]
resultW = resultW.reset_index(drop = True)
resultW.columns = resultW.columns.str.replace('_', ' ')
resultW.columns = resultW.columns.str.title()
resultW = pd.DataFrame(resultW)
countW = len(resultW)
avgOppRankW = int(resultW["Loser Rank"].mean(skipna=True))


# Collecting Losses
resultL = allMatches.loc[allMatches["loser_name"] == player, ["winner_name", "winner_rank"]]
resultL = resultL.reset_index(drop = True)
resultL.columns = resultL.columns.str.replace('_', ' ')
resultL.columns = resultL.columns.str.title()
resultL = pd.DataFrame(resultL)
countL = len(resultL)
avgOppRankL = int(resultL["Winner Rank"].mean(skipna=True))


record = 'W-L Record' + ':' + str(countW) + '-' + str(countL)

print(resultL)
print("-------------------------------")
print(record)
print("-------------------------------")
print("Avg. Opponent Rank (Wins):" + " " + str(avgOppRankW))
print("Avg. Opponent Rank (Losses):" + " " + str(avgOppRankL))

