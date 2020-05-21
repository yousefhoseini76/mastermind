import random

colors = {
    1: "red",
    2: "blue",
    3: "green",
    4: "yellow",
    5: "white"
}

initial = []
while len(initial) < 4:
    r = random.randint(1,5)
    if r not in initial:
        initial.append(r)

print([colors[item] for item in initial])

guess = input()
guess = guess.split(",")
guess = [int(item) for item in guess]
print(guess)

black = 0
white = 0
for i in range(len(guess)):
    if initial[i] == guess[i]:
        black += 1
    elif guess[i] in initial:
        white += 1

print("black: {} , white: {}".format(black , white))