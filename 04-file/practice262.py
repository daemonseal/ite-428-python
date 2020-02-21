# Find the comment that contains rude word


def check_word(comment, rude_word):
    comment = [c.lower().strip() for c in comment]
    rude_word = [r.lower().strip() for r in rude_word]
    can_show = [w for w in comment if showable(w, rude_word)]
    cannot_show = [w for w in comment if not showable(w, rude_word)]
    return (can_show, cannot_show)


def showable(w, rude_word):
    for l in w.split():
        if l in rude_word:
            return False
    return True


def read_file(f):
    with open(f, 'r') as fi:
        return [l for l in fi.read().splitlines()]


def write_file(f, d):
    with open(f, 'w') as fi:
        fi.write('\n'.join(d))


def feedback_pct(g, b):
    n = len(g) + len(b)
    return len(b) / n * 100


# Read from files
comment = read_file('practice262-files/practice-comment.txt')
rude_word = read_file('practice262-files/rude_word.txt')

# Check
can_show, cannot_show = check_word(comment, rude_word)

# Write to files
write_file('practice262-files/canshow.txt', can_show)
write_file('practice262-files/cannotshow.txt', cannot_show)
print("Bad Feedback = {:.2f}%".format(feedback_pct(can_show, cannot_show)))
