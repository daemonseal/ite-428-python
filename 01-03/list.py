# list (slide153)
#Basic List
teams = ["Chelsea", "Man Utd", "Man City", "Spurs", "Liverpool"]
print(teams)
print(len(teams))
teams = teams + ["Leicester City" , "Arsenal"]
print(teams)
teams[0] = teams[4]
teams[4] = "Chelsea"
print(teams)
del teams[1]
print(teams)
teams.remove("Spurs")
print(teams)
teams2017 = sorted(teams)
print(teams)
print(teams2017)
teams.sort() # teams.sort(reverse=True)  descending order
print(teams)
# Slicing List (like String)
# [start:stop_exclude:step]
# Default start = 0 , stop_exclude = last index , step = 1
Name = ['Adisak', 'Salinla', 'Pasakorn', 'Boon']
teams = ["Liverpool","Chelsea", "Man Utd", "Man City", "Spurs","Arsenal"]
print(teams)
print(teams[1:4])
print(teams[:4])
print(teams[::2])
print(teams[1:4:2])

print(teams[-1:-5:-1])
print(teams[-1:-6:-2])
print(teams[-1::-1])
print(teams[::-1])

# Dimension List (Tuple in List)
team2018 = [(1, "Liverpool"),
(2, "Chelsea"),
(3, "Spurs"),
(4, "Arsenal")
]

print(team2018[2][1])
print(team2018[1][0])
print(team2018[0][0])
print(team2018[3][1])
# Dimension List (Tuple in List)
team2018 = [(1, "Liverpool"),
(2, "Chelsea"),
(3, "Spurs"),
(4, "Arsenal")
]

print(team2018[2][1])
print(team2018[1][0])
print(team2018[0][0])
print(team2018[3][1])

# Dimension List (Tuple in List)
team2018 = [(1, "Liverpool"),
(2, "Chelsea"),
(3, "Spurs"),
(4, "Arsenal")
]
print(team2018[2][1])
print(team2018[1][0])
print(team2018[0][0])
print(team2018[3][1])

# Search Data in List
flowers = ["Sun flower","Ivy","Jusmine","Lily"]
# “in” is Membership Operator
check_flower = "forget me not" in flowers
print(check_flower)
check_flower = "jusmine" in flowers
print(check_flower)
check_flower = "Jusmine" in flowers
print(check_flower)
if (check_flower):
    print(flowers.index("Jusmine"))
print(flowers)
flowers.clear()
print(flowers)
print(len(flowers))
