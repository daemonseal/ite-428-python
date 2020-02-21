import math
# Predefined data
weight = (62.5,78,50,42,84,65.5,48,53.5,43)

n = len(weight)
maximum  = max(weight)
minimum = min(weight)
average = sum(weight) / n
# Use list comprehension
ab = len([x for x in weight if x > average])
bl = len([x for x in weight if x < average])
eq = len([x for x in weight if x == average])

# OUTPUT
print("Maximum weight of {} persons = {}".format(n, maximum))
print("Minimum weight of {} persons = {}".format(n, minimum))
print("Average weight of {} persons = {}".format(n, average))
print("No. of weight above average = {}".format(ab))
print("No. of weight below average = {}".format(bl))
print("No. of weight equal average = {}".format(eq))
