def line():
    print("-"*30)

flowers = ["Sun flower","Ivy","Jusmine","Lily"]
for i, f in enumerate(sorted(flowers)):
    print("{}. {}".format(i+1, f))
line()
