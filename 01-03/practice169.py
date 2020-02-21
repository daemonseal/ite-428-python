# Find the comment that contains rude word
rude_word = ["damn","hell","ass","piss","silly","idiotic","fuck"]
comment = input("Please comment our service : ")

def check_rude(comment, rude_word):
    words = [c.lower() for c in comment.split()]
    for w in words:
        if w in rude_word:
            return "Cannot show"
    return "Can show"

try:
    print("{} [{}]".format(check_rude(comment, rude_word), comment))
except:
    print("Please input a valid value eg. 'I really like your service'")
