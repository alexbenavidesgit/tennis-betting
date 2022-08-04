import csv
import pandas as pd
from datetime import datetime


MAINDIR = "./"

# Read and Prepare Tables
atp2022 = pd.read_csv('Data/atp_matches_2022.csv', encoding = 'UTF-8')
challenger2022 = pd.read_csv('Data/atp_matches_qual_chall_2022.csv', encoding = 'UTF-8')
Futures2022 = pd.read_csv('Data/atp_matches_futures_2022.csv', encoding = 'UTF-8')

atp2022 = pd.DataFrame(atp2022)
challenger2022 = pd.DataFrame(challenger2022)
futures2022 = pd.DataFrame(Futures2022)

allMatches = pd.concat([atp2022, challenger2022, futures2022])


player = input().title()

# Collecting Wins from Inputed Player
resultW = allMatches.loc[allMatches["winner_name"] == player, ["loser_name", "loser_rank", 'score', 'tourney_date','loser_ioc']]
# Formatting Table
resultW = resultW.reset_index(drop = True)
resultW = pd.DataFrame(resultW)
resultW[['tourney_date']] = resultW[['tourney_date']].applymap(str).applymap(lambda s: "{}/{}/{}".format(s[4:6],s[6:], s[0:4]))
resultW.columns = ['Opp_Name', 'Opp_Ranking', 'Score', 'Date', 'Nationality']

# Collecting Wins Stats
countW = len(resultW)
avgOppRankW = int(resultW["Opp_Ranking"].mean(skipna=True))

# Analyzing Wins
wins_top_500 = resultW.apply(lambda x : True
            if x['Opp_Ranking'] <= 500 else False, axis = 1)
num_wins_top_500 = len(wins_top_500[wins_top_500 == True].index)

wins_b_500_700 = resultW.apply(lambda x : True
            if x['Opp_Ranking'] >= 500 and x['Opp_Ranking'] <= 700 else False, axis = 1)
num_wins_b_500_700 = len(wins_b_500_700[wins_b_500_700 == True].index)

wins_b_700_900 = resultW.apply(lambda x : True
            if x['Opp_Ranking'] >=700 and x['Opp_Ranking'] <= 900 else False, axis = 1)
num_wins_b_700_900 = len(wins_b_700_900[wins_b_700_900 == True].index)

# Assign Points
score = (num_wins_top_500 * 3.5) + (num_wins_b_500_700 * 2) + (num_wins_b_700_900 * 1)



# --------------------------------------------------------------------------------------
# Collecting Losses from Inputed Player
resultL = allMatches.loc[allMatches["loser_name"] == player, ["winner_name", "winner_rank", 'score', 'tourney_date', 'winner_ioc']]
# Formatting Table
resultL = resultL.reset_index(drop = True)
resultL = pd.DataFrame(resultL)
resultL[['tourney_date']] = resultL[['tourney_date']].applymap(str).applymap(lambda s: "{}/{}/{}".format(s[4:6],s[6:], s[0:4]))
resultL.columns = ['Opp_Name', 'Opp_Ranking', 'Score', 'Date', 'Nationality']
# Collecting Loss Stats
countL = len(resultL)
avgOppRankL = int(resultL["Opp_Ranking"].mean(skipna=True))
record = 'W-L Record' + ':' + str(countW) + '-' + str(countL)


# print(player + "'s" + " " + "Wins")
# print(resultW)
# print("-------------------------------------------------------------------")
# print(player + "'s" + " " + "Losses")
# print(resultL)
print("-------------------------------------------------------------------")
print(record)
print("-------------------------------------------------------------------")
print("Avg. Opponent Rank (Wins):" + " " + str(avgOppRankW))
print("Avg. Opponent Rank (Losses):" + " " + str(avgOppRankL))
print("-------------------------------------------------------------------")
print("# of Wins (Top 500):" + " " + str(num_wins_top_500))
print("# of Wins (500-700):" + " " + str(num_wins_b_500_700))
print("# of Wins (700-900):" + " " + str(num_wins_b_700_900))
print("-------------------------------------------------------------------")
print(player + "'s " + 'FerSure Score is: ' + str(score))
