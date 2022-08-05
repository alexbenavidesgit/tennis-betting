# want to pass in the result of the wins_table method in data_collection.py as the parameter of so_Who_You_Been_Beating_Eh
def so_Who_You_Been_Beating_Eh(wins_table):

    wins_tracker = {
        '100-200': [], '200-300': [], '300-400': [], 
        '400-500':[], '500-600':[], '600-700':[],
        '700-800':[], '800-900':[], '900-1000':[],
        '1000-1100':[], '1100-1200':[], '1200-1300':[],
        '1300-1400':[], '1400-1500':[], '1500-1600':[],        
    }

    ranking_min = 100
    ranking_max = 200
    trash = 1
    wins_table_index = 0

    i = 0
    while i < (len(wins_tracker) - 1):
        wins_table.apply(lambda x : wins_tracker[str(ranking_min) + '-' + str(ranking_max)].append(x["Opp_Name"])
            if (x["Opp_Ranking"] >= ranking_min and x['Opp_Ranking'] <= ranking_max) else trash == trash + 1, axis = 1)
        ranking_min += 100
        ranking_max += 100
        wins_table_index += 1
        i += 1

    return wins_tracker
    


# NEXT STEP 1: create new method that takes in a player as a parameter and looks into many other variables like recent good wins, # of tourney played, etc
# then the result of that method would affect the basic fer score a player already has.



