premier_league_2017_2018 =  [["ManchesterCity",(32,4,2)],["Manchester United",(25,6,7)],["Tottenham",(23,8,7)],["Liverpool",(21,12,5)],["C helsea",(21,7,10)],["Arsenal",(19,6,13)],["Burnley",(14,12,12)],["Ever ton",(13,10,15)],["Leicester",(12,11,15)],["Newcastle",(12,8,18)],["Crystal Palace",(11,11,16)],["Bournemouth",(11,11,16)],["West Ham",(10,12,16)],["Watford",(11,8,19)],["Brighton",(9,13,16)],["Hud dersfield",(9,10,19)],["Southampton",(7,15,16)],["Swansea",(8,9,21)] ,["Stoke",(7,12,19)],["West Bromwich",(6,13,19)]]

def line():
    print('-'*60)

def parse_data(team):
    return {
        'Name': team[0].rstrip(),
        'Wins': team[1][0],
        'Draws': team[1][1],
        'Loses': team[1][2],
        'Points': (team[1][0]*3) + team[1][1]
    }

def lose_morethan_draw(teams):
    line()
    print("SHOW LOSES MORE THAN DRAW")
    line()
    for i, t in enumerate(teams):
        team = parse_data(t)
        suck = team['Loses'] - team['Draws']
        if suck > 0:
            print("{:<10} {:>20}".format(team['Name'], suck ))
    line()

lose_morethan_draw(premier_league_2017_2018)
