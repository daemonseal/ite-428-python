wantedskill = {"C#" , "Python" , "Java" ,"PHP" , "SQL" , "Go"}
applicant1skill = {"VB","C","Ruby","Java","HTML"}
applicant2skill = {"C#","HTML","R","PHP","SQL","Swift","PHP"}
applicant3skill = {"Java","C++","Ruby","JavaScript","Objective-C","Go"}
applicant4skill = {"Java","Python","Go","SQL","Swift"}
applicant5skill = {"C++","C","C#","Objective-C","JavaScript","SQL"}

applicant = [applicant1skill, applicant2skill, applicant3skill, applicant4skill, applicant5skill]

def find_match(a, skills):
    return len(skills & a) / float(len(skills)) * 100

for i, a in enumerate(applicant):
    print('Applicant {} skill match : {:.2f}%'.format(i, find_match(a, wantedskill)))
