# tennis-betting
Picking tennis winners

Developer Onboarding 
Device Onboarding - Mac
Open Terminal
Paste in the following -> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Follow steps after. You need to put everything in the correct path
Download VSCode + the following extensions
CSV to Table 
Rainbow CSV
Install git 
$ brew install git
Clone repo
$ git clone https://github.com/JeffSackmann/tennis_atp.git
$ git clone https://github.com/alexbenavidesgit/tennis-betting.git
Make your own branch -> $ git checkout -b “name-of-branch”
Install Python
$ brew install python
$ brew unlink python && brew link python
Install virtual env
$ python3 -m pip install virtualenv
Activate venv
$ cd “location of tennis-betting repo”
$ virtualenv venv
$ source venv/bin/activate
$ pip install <package>
Download packages ONLY inside venv to avoid destroying your laptop
$ deactivate
ONLY deactivate whenever you’re done using venv
Install Jupyter Notebook inside virtual env
$ pip install notebook
$ jupyter notebook
Ponte Pilas 

Device Onboarding - Windows
Download GIT
Download VSCode + the following extensions
CSV to Table 
Rainbow 
Do you download these in VCCode?
Clone repo 
$ git clone https://github.com/JeffSackmann/tennis_atp.git
Put this in a separate folder.
so that you don’t make a cagadero
$ git clone https://github.com/alexbenavidesgit/tennis-betting.git
Make your own branch -> $ git checkout -b “name-of-branch”
Install Python
Install virtual env
Activate venv
Ponte Pilas

Git Repos 
Tennis related
1.Historical tennis results
https://github.com/JeffSackmann/tennis_atp.git
Python scripts to predict results
https://github.com/edouardthom/ATPBetting


APIs
Betting odds
https://www.lsports.eu/oddservice/?gclid=Cj0KCQjwuaiXBhCCARIsAKZLt3neCAqKDmAPkVYiyJJt_cZ2nUuBsKW7gtw65gMldn8ZE1PJwWDsbqoaAqExEALw_wcB
https://oddsmatrix.com/sports/tennis/?gclid=Cj0KCQjwuaiXBhCCARIsAKZLt3m0eVsPeFFzH7aWDhFAPxs0lwmq-EOZ71XcoOx7fY7wKBFqj6vLJaoaApU7EALw_wcB

Ideas
H2H
Website?
Get odds
Build DB of previous odds
What round the match took place
How many future semis or finals
Locations of tournament


FerSure Algorithm (futures & challenger matchups )

Collect wins & losses 
Figure out a system that assigns a score for each recent win depending on rankings (can also drill in and assess the level of the players that they have beat)
e.g Player A has beat 3 guys ranked in the top 600. Now lets look into who those 3 guys are and who they’ve beat. 
Eventually maybe we can collect every player Player A & Player B has played in the last 3 months, wins & losses, and look into how good or bad those results were. 
Eventually we need to also collect data from NCAA and have a check before we assess a player - just in case we get the goaty college guy with no rankings 
Also need to check junior ITF junior rankings (only relevant if top 200)
Qualifying W/L record in futures and challengers (if you have a guy that has played 30 futures and losses in qualies everytime - we can put a Checko B. mark 
Create a metric that takes into account how many tournaments it took for a player to reach their ranking
You could have a guy ranked 750 whose played 30 futures and a guy ranked 1000 whose played 3 in fucking florida 
Id give some sort of edge to the guy whose played 3 fer sure fer sure 

*** We could do a test run where we manually create a JSON with lets say 50 upcoming matches and then we run our algo on da historical data and see how it performs
	* for sure. We could use those as unit test.
	* imagine, if we had unit test or something to see how our specific algo does vs next 50 matches. It would be SICK. that means we can try so much random shit and see how it does





Comments Sections:




## Ideas
- Explore https://developer.sportradar.com/ for free api

## Guide for atp_odds_*.csv files

Notes for Tennis Data

All data is in csv format, ready for use within standard spreadsheet applications. 

Key to results data:

ATP = Tournament number (men)
WTA = Tournament number (women)
Location = Venue of tournament
Tournament = Name of tounament (including sponsor if relevant)
Data = Date of match (note: prior to 2003 the date shown for all matches played in a single tournament is the start date)
Series = Name of ATP tennis series (Grand Slam, Masters, International or International Gold)
Tier = Tier (tournament ranking) of WTA tennis series.
Court = Type of court (outdoors or indoors)
Surface = Type of surface (clay, hard, carpet or grass)
Round = Round of match
Best of = Maximum number of sets playable in match
Winner = Match winner
Loser = Match loser
WRank = ATP Entry ranking of the match winner as of the start of the tournament
LRank = ATP Entry ranking of the match loser as of the start of the tournament
WPts = ATP Entry points of the match winner as of the start of the tournament
LPts = ATP Entry points of the match loser as of the start of the tournament
W1 = Number of games won in 1st set by match winner
L1 = Number of games won in 1st set by match loser
W2 = Number of games won in 2nd set by match winner
L2 = Number of games won in 2nd set by match loser
W3 = Number of games won in 3rd set by match winner
L3 = Number of games won in 3rd set by match loser
W4 = Number of games won in 4th set by match winner
L4 = Number of games won in 4th set by match loser
W5 = Number of games won in 5th set by match winner
L5 = Number of games won in 5th set by match loser
Wsets = Number of sets won by match winner
Lsets = Number of sets won by match loser
Comment = Comment on the match (Completed, won through retirement of loser, or via Walkover)


Key to match betting odds data:

B365W = Bet365 odds of match winner
B365L = Bet365 odds of match loser
B&WW = Bet&Win odds of match winner
B&WL = Bet&Win odds of match loser
CBW = Centrebet odds of match winner
CBL = Centrebet odds of match loser
EXW = Expekt odds of match winner
EXL = Expekt odds of match loser
LBW = Ladbrokes odds of match winner
LBL = Ladbrokes odds of match loser
GBW = Gamebookers odds of match winner
GBL = Gamebookers odds of match loser
IWW = Interwetten odds of match winner
IWL = Interwetten odds of match loser
PSW = Pinnacles Sports odds of match winner
PSL = Pinnacles Sports odds of match loser
SBW = Sportingbet odds of match winner
SBL = Sportingbet odds of match loser
SJW = Stan James odds of match winner
SJL = Stan James odds of match loser
UBW = Unibet odds of match winner
UBL = Unibet odds of match loser

MaxW= Maximum odds of match winner (as shown by Oddsportal.com)
MaxL= Maximum odds of match loser (as shown by Oddsportal.com)
AvgW= Average odds of match winner (as shown by Oddsportal.com)
AvgL= Average odds of match loser (as shown by Oddsportal.com)


Tennis-Data would like to acknowledge the following sources which are currently utilised in the compilation of Tennis-Data's results and odds files.

Results:
Xscores - http://www.xscores.com/
ATPtennis.com - http://www.atptennis.com/
ATP Tour Rankings and Results Page - http://www.stevegtennis.com/
Livescore - http://www.livescore.net/

Rankings:
ATPtennis.com - http://www.atptennis.com/
ATP Tour Rankings and Results Page - http://www.stevegtennis.com/
WTA TOur Rankings - http://www.sonyericssonwtatour.com

Betting odds for matches generally represent the most recent before play starts, as reported by oddsportal.com and the individual bookmakers.