def demoDict():
    myDict = { "Name":"Adisak","Lastname" : "Suasaming", "Age": 40,"Mobile":"081-550-2041"}
    print (type(myDict))
    print (myDict)
    print (len(myDict))
    print (myDict["Name"], myDict["Mobile"])
    myDict["DOB"] = "30-11-1976" # Add new key "DOB" in dictionary
    myDict["Lastname"] = "Suasamings" # Update value at key "Lastname"
    del myDict["Age"] # Key is case-sensitive can not "age"
    print (myDict)
demoDict()

def kualalumpur2017():
    medal = {"mas":(145,92,86),"tha":[72,86,88 ]}
    print(medal["mas"])
    print(medal["mas"][0])
    #medal["mas"][0] = 12
    print(medal["tha"])
    print(medal["tha"][0])
    medal["tha"][0] = 190
    medal["tha"].insert(1,90)
    medal["tha"].remove(86)
    print(medal["tha"])
    print(medal["tha"][0]+ medal["tha"][1]+ medal["tha"][2])
kualalumpur2017()
