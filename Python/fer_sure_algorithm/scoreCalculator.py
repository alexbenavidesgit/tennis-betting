def ferSureScore(points_tracker):
    i = 0
    firstLayerW = []
    secondLayerW = []
    firstLayerL = []
    while i < (len(points_tracker) - 1):
        score1W = list(points_tracker.values())[i]["firstLayerPoints"]
        firstLayerW.append(score1W)
        score2W = list(points_tracker.values())[i]["SecondLayerPoints"]
        secondLayerW.append(score2W)
        score1L = list(points_tracker.values())[i]["firstLayerPointsL"]
        i += 1
    return ((sum(firstLayerW) + sum(secondLayerW)) - sum(firstLayerL))
