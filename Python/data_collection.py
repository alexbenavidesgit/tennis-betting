from random import expovariate
import pandas as pd
from datetime import datetime
from pprint import pprint

def input_player():
    player = input().title()
    return player


MAINDIR = "./"

# Read and Prepare Tables
atp2022 = pd.read_csv('Data/atp_matches_2022.csv', encoding = 'UTF-8')
challenger2022 = pd.read_csv('Data/atp_matches_qual_chall_2022.csv', encoding = 'UTF-8')
Futures2022 = pd.read_csv('Data/atp_matches_futures_2022.csv', encoding = 'UTF-8')

atp2022 = pd.DataFrame(atp2022)
challenger2022 = pd.DataFrame(challenger2022)
futures2022 = pd.DataFrame(Futures2022)

allMatches = pd.concat([atp2022, challenger2022, futures2022])

points_tracker = {
    '100-200': {"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0}, 
    '200-300': {"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0}, 
    '300-400': {"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0}, 
    '400-500':{"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0}, 
    '500-600':{"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0}, 
    '600-700':{"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0},
    '700-800':{"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0}, 
    '800-900':{"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0}, 
    '900-1000':{"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0},
    '1000-1100':{"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0}, 
    '1100-1200':{"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0}, 
    '1200-1300':{"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0},
    '1300-1400':{"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0}, 
    '1400-1500':{"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0}, 
    '1500-1600':{"Wins": [],"firstLayerPoints": 0, "SecondLayerPoints": 0, "Losses": [], "firstLayerPointsL": 0, "SecondLayerPointsL": 0},        
    }

secondary_points_tracker = {
        '100-200': [], '200-300': [], '300-400': [], 
        '400-500':[], '500-600':[], '600-700':[],
        '700-800':[], '800-900':[], '900-1000':[],
        '1000-1100':[], '1100-1200':[], '1200-1300':[],
        '1300-1400':[], '1400-1500':[], '1500-1600':[],        
    }

player = ""


# Need to figure out how to export these objects to use in other files