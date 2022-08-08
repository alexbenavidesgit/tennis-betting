# need to add dependencies 
# need to import object from data_collection page


def firstLayerResults(player, result, results_data):
    
    if (player == ""):
        player = input()
    
    if result == "Wins":
        result_ = "winner_name"
        result__ = "loser_name"
        rank = "loser_rank"
    else:
        result_ = "loser_name"
        result__ = "winner_name"
        rank = "winner_rank"
        
    results = allMatches.loc[allMatches[result_] == player, [result__, rank, 'score', 'tourney_date','loser_ioc']]
    # Formatting Table
    results = results.reset_index(drop = True)
    results = pd.DataFrame(results)
    results[['tourney_date']] = results[['tourney_date']].applymap(str).applymap(lambda s: "{}/{}/{}".format(s[4:6],s[6:], s[0:4]))
    results.columns = ['Opp_Name', 'Opp_Ranking', 'Score', 'Date', 'Nationality']

    ranking_min = 100
    ranking_max = 200
    trash = 1
    
    try:
        results_data['100-200'][result]
    except TypeError:
        i = 0
        while i < (len(results_data) - 1):
            results.apply(lambda x : results_data[str(ranking_min) + '-' + str(ranking_max)].append(x["Opp_Name"])
                if (x["Opp_Ranking"] >= ranking_min and x['Opp_Ranking'] <= ranking_max) else trash == trash + 1, axis = 1)
            ranking_min += 100
            ranking_max += 100
            i += 1
    else:
        i = 0
        while i < (len(results_data) - 1):
            results.apply(lambda x : results_data[str(ranking_min) + '-' + str(ranking_max)][result].append(x["Opp_Name"])
                if (x["Opp_Ranking"] >= ranking_min and x['Opp_Ranking'] <= ranking_max) else trash == trash + 1, axis = 1)
            result_count = len(results_data[str(ranking_min) + '-' + str(ranking_max)][result]) 
            if (ranking_min == 100 and result_count > 0 and result == "Wins"):
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 25 * result_count
                secondary_points_tracker['100-200'].clear()
            elif (ranking_min == 100 and result_count > 0 and result == "Losses"):
                    points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 0.1 * result_count
                    secondary_points_tracker['100-200'].clear()
            if ranking_min == 200 and result_count > 0 and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 20 * result_count
                secondary_points_tracker['200-300'].clear()
            elif ranking_min == 200 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 0.3 * result_count
                secondary_points_tracker['200-300'].clear()
            if ranking_min == 300 and result_count > 0 and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 12 * result_count
                secondary_points_tracker['300-400'].clear()
            elif ranking_min == 100 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 0.5 * result_count
                secondary_points_tracker['300-400'].clear()
            if ranking_min == 400 and result_count > 0 and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 10 * result_count
                secondary_points_tracker['400-500'].clear()
            elif ranking_min == 400 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 0.7 * result_count
                secondary_points_tracker['400-500'].clear()
            if ranking_min == 500 and result_count > 0 and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 8 * result_count
                secondary_points_tracker['500-600'].clear()
            elif ranking_min == 500 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 1 * result_count
                secondary_points_tracker['500-600'].clear()         
            if ranking_min == 600 and result_count > 0 and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 7 * result_count
                secondary_points_tracker['600-700'].clear()
            elif ranking_min == 600 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 1 * result_count
                secondary_points_tracker['600-700'].clear()
            if ranking_min == 700 and result_count > 0 and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 6 * result_count
                secondary_points_tracker['700-800'].clear()
            elif ranking_min == 700 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 2 * result_count
                secondary_points_tracker['700-800'].clear()        
            if ranking_min == 800 and result_count > 0 and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 5 * result_count
                secondary_points_tracker['800-900'].clear()
            elif ranking_min == 800 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 3 * result_count
                secondary_points_tracker['800-900'].clear()
            if ranking_min == 900 and result_count > 0 and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 4 * result_count
                secondary_points_tracker['900-1000'].clear()
            elif ranking_min == 900 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 4 * result_count
                secondary_points_tracker['900-1000'].clear()
            if ranking_min == 1000 and result_count > 0 and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 3 * result_count
                secondary_points_tracker['1000-1100'].clear()
            elif ranking_min == 1100 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 5 * result_count
                secondary_points_tracker['1000-1100'].clear()
            if ranking_min == 1100 and result_count and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 2 * result_count
                secondary_points_tracker['1100-1200'].clear()
            elif ranking_min == 1100 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 6 * result_count
                secondary_points_tracker['1100-1200'].clear()
            if ranking_min == 1200 and result_count and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 1 * result_count
                secondary_points_tracker['1200-1300'].clear()
            elif ranking_min == 1200 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 7 * result_count
                secondary_points_tracker['1200-1300'].clear()
            if ranking_min == 1300 and result_count and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 0.7 * result_count
                secondary_points_tracker['1300-1400'].clear()
            elif ranking_min == 1300 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 8 * result_count
                secondary_points_tracker['1300-1400'].clear()
            if ranking_min == 1400 and result_count and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 0.5 * result_count
                secondary_points_tracker['1400-1500'].clear()
            elif ranking_min == 1400 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 10 * result_count
                secondary_points_tracker['1400-1500'].clear()
            if ranking_min == 1500 and result_count and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 0.3 * result_count
                secondary_points_tracker['1500-1600'].clear()
            elif ranking_min == 1500 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 12 * result_count
                secondary_points_tracker['1500-1600'].clear()
            if ranking_min == 1600 and result_count and result == "Wins":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPoints"] = 0.1 * result_count
                secondary_points_tracker['1600-1700'].clear()
            elif ranking_min == 1600 and result_count > 0 and result == "Losses":
                points_tracker[str(ranking_min) + "-" + str(ranking_max)]["firstLayerPointsL"] = 14 * result_count
                secondary_points_tracker['1600-1700'].clear()
        
            ranking_min += 100
            ranking_max += 100
            i += 1
        

def secondLayerResults(result):
    ranking_min = 100
    ranking_max = 200
    
    i = 0
    while i < (len(points_tracker) - 1):
        first_layerResultsList = points_tracker[str(ranking_min) + '-' + str(ranking_max)][result]
        for x in first_layerResultsList:
            secondLayerAnalysis(x, result)     
        ranking_min += 100
        ranking_max += 100
        i += 1


def secondLayerAnalysis(player, result):
    firstLayerResults(player, result, secondary_points_tracker)
    a = 100
    b = 200
    
    i = 0
    while i < (len(secondary_points_tracker) - 1):
        result_count = len(secondary_points_tracker[str(a) + "-" + str(b)])
        if (a == 100 and result_count > 0):
            points_tracker[str(a) + "-" + str(b)]["SecodLayerPoints"] = 20 * result_count
            secondary_points_tracker['100-200'].clear()
        if a == 200 and result_count > 0:
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 15 * result_count
            secondary_points_tracker['200-300'].clear()
        if a == 300 and result_count > 0:
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 13 * result_count
            secondary_points_tracker['300-400'].clear()
        if a == 400 and result_count > 0:
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 11 * result_count
            secondary_points_tracker['400-500'].clear()
        if a == 500 and result_count > 0:
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 9 * result_count
            secondary_points_tracker['500-600'].clear()
        if a == 600 and result_count > 0:
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 7 * result_count
            secondary_points_tracker['600-700'].clear()
        if a == 700 and result_count > 0:
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 6 * result_count
            secondary_points_tracker['700-800'].clear()
        if a == 800 and result_count > 0:
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 5 * result_count
            secondary_points_tracker['800-900'].clear()
        if a == 900 and result_count > 0:
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 4 * result_count
            secondary_points_tracker['900-1000'].clear()
        if a == 1000 and result_count > 0:
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 3 * result_count
            secondary_points_tracker['1000-1100'].clear()
        if a == 1100 and result_count:
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 2 * result_count
            secondary_points_tracker['1100-1200'].clear()
        if a == 1200 and result_count:
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 1.5 * result_count
            secondary_points_tracker['1200-1300'].clear()
        if a == 1300 and result_count:
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 1 * result_count
            secondary_points_tracker['1300-1400'].clear()
        if (a == 1400 and result_count):
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 0.5 * result_count
            secondary_points_tracker['1400-1500'].clear()
        if (a == 1500 and result_count):
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 0.25 * result_count
            s
            econdary_points_tracker['1500-1600'].clear()
        if (a == 1600 and result_count):
            points_tracker[str(a) + "-" + str(b)]["SecondLayerPoints"] = 0.125 * result_count
            secondary_points_tracker['1600-1700'].clear()
        a += 100
        b += 100
        i += 1